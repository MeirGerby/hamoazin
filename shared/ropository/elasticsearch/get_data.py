from shared.db.elasticsearch import ElasticSingleton 
from shared.core.config import settings

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
        return data 

    async def get_audio_text(self):
        """get the text field content from the documents"""
        text = await self.client.search(
            index=self.index_name,
            query={
                'query_string': {"query": 'file id'}
            }
        )
        return text 
    
    async def insert_data_to_index(self, data):
        """insert data to elasticsearch index"""
        return await self.client.index(index=settings.ELASTIC_INDEX_NAME, document=data) 