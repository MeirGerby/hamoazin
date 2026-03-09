from shared.db.elasticsearch import ElasticSingleton 
from shared.core.config import settings
from shared.logs.logs import Logger 
from ..service.handle_text import HandleText

logger = Logger.get_logger()

class ElasticSearchCalculateWords(ElasticSingleton):
    """elasticsearch crud operation (singleton)"""
    def __init__(self, handle_text: HandleText):
        self.check_text: dict = handle_text.get_words()
        self.danger_words: list = self.check_text['danger_words']
        self.less_danger: list = self.check_text['less_danger_words']
        self.less_danger_coupled: list = self.check_text['less_danger_coupled_words']
        self.danger_coupled_words: list = self.check_text['danger_coupled_words']

        if not hasattr(self, 'initiolized'):
            # this check is for avoid initiolization every time the class is getting called
            self.index_name = settings.ELASTIC_INDEX_NAME
            self.initiolized = True 

    def create_word_query(self, list_of_words: list, boost: int = 1, coupled: bool = False): 
        """create elasticsearch query for list of words""" 
        queries = [] 
        try:
            for i in list_of_words:
                if coupled:
                    query = {"match_phrase": {'text': {'query': i, 'boost': boost}}}
                else:
                    query = {"match": {'text': {'query': i, 'boost': boost}}}
                queries.append(query)
                logger.info(f"create a query from the text: {i}. \n   query: {query}.")
        except Exception as e:
            logger.exception(f"there is an error {e}. \n mayby you shuold check the type of the paramter")
        return queries

    async def calculate_words(self, queries: list): 
        """calculate the words include ranking from elasticsearch"""
        try:
            query = {'bool':{'should':queries}}
            logger.debug(f'create a query for searching in elasticsearch \n  query: {queries}')
            data = await self.client.search(
                index=self.index_name,
                query=query
            )
            response = data['hits']['hits'] 
            logger.info(f"search in index - {self.index_name} \n  response: {response}")

            for hit in response:  
                logger.info(f"Score: {hit['_score']}, text: {hit['_source']['text']}")
        except Exception as e:
            logger.exception(e)





