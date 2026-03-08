from shared.db.elasticsearch import ElasticSingleton 
from shared.core.config import settings
from shared.logs.logs import Logger 

logger = Logger.get_logger()

class ElasticSearchInsertData(ElasticSingleton):
    """elasticsearch crud operation (singleton)"""
    def __init__(self):
        # this check is for avoid initiolization every time the class is getting called
        if not hasattr(self, 'initiolized'):
            self.index_name = settings.ELASTIC_INDEX_NAME
            self.initiolized = True  

    async def insert_text_to_index(self, text):
        """insert data to elasticsearch index""" 
        try:
            data = {"text": text}
            response = await self.client.index(index=self.index_name, document=data) 
            logger.info(f"insert data into the index {self.index_name}, data: {str(data)}, response {str(response)}")
            return response  
        except Exception as e:
            logger.error(e)
    
    async def create_index(self, metadata: dict):
        try:
            id = metadata.get('id')
            index = await self.client.index(index=self.index_name, document=metadata, id=id) 
            logger.info(f"the index added successfully {str(index)} ")
            # return {"index": str(index)}
        except Exception as e:
            logger.error(f"the id doesn't exist {e}") 