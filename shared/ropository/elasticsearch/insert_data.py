from shared.db.elasticsearch import ElasticSingleton 
from shared.core.config import settings

class ElasticSearchInsertData(ElasticSingleton):
    """elasticsearch crud operation (singleton)"""
    def __init__(self):
        # this check is for avoid initiolization every time the class is getting called
        if not hasattr(self, 'initiolized'):
            self.index_name = settings.ELASTIC_INDEX_NAME
            self.initiolized = True  

    async def insert_data_to_index(self, data):
        """insert data to elasticsearch index"""
        return await self.client.index(index=settings.ELASTIC_INDEX_NAME, document=data) 