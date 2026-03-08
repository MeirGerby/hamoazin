from shared.db.elasticsearch import ElasticSingleton 
from shared.core.config import settings
from shared.logs.logs import Logger 

logger = Logger.get_logger()

class ElasticSearchGetData(ElasticSingleton):
    """elasticsearch crud operation (singleton)"""
    def __init__(self):
        # this check is for avoid initiolization every time the class is getting called
        if not hasattr(self, 'initiolized'):
            self.index_name = settings.ELASTIC_INDEX_NAME
            self.initiolized = True  
        
    async def get_all_data(self):
        """get all documents from the index"""
        data = await self.client.search(
            index=self.index_name,
            query={
                'match_all': {}
            },
            pretty=True
        )
        logger.info(f"get all data from index {self.index_name}")
        return data 

    async def get_audio_text(self):
        """get the text field content from the documents"""
        text = await self.client.search(
            index=self.index_name,
            query={
                'query_string': {"query": 'file id'}
            }
        )
        logger.info(f"get all audio text from index {self.index_name}, text: {text}")
        return text 
    

    
