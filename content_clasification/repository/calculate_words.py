from shared.db.elasticsearch import ElasticSingleton 
from shared.core.config import settings
from shared.logs.logs import Logger 
from service.handle_text import HandleText

logger = Logger.get_logger()

class ElasticSearchColculateWords(ElasticSingleton):
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

    def create_word_query(self, list_of_words: list, boost=1): 
        """create elasticsearch query for list of words""" 
        queries = [] 
        for i in list_of_words:
            query = {"match": {'text': i, 'boost': boost}}
            queries.append(query)
            logger.info(f"create a query from the text: {i}. \n   query: {query}.")
        return queries
        

    async def colculate_words(self, queries: list): 
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
                score = hit.get('_score', 0)
                text = hit.get('_source', {}).get('text', 'not text found')
                logger.info(f"Score: {hit[score]}, text: {hit['_source'][text]}")
        except Exception as e:
            logger.exception(e)





