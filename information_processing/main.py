import asyncio

from shared.kafka.consumer import ConsumerMessages 
from shared.core.config import settings 
from shared.logs.logs import Logger 
from shared.repository.elasticsearch.insert_data import ElasticSearchInsertData


logger = Logger.get_logger()
class Manager:
    def __init__(self):
        self.consumer_topics = [settings.METADATA_TOPIC]    
        self.group_id = settings.PROCESSING_GROUP_ID 
        self.index_name = settings.ELASTIC_INDEX_NAME 
        self.elastic_url = settings.ELASTIC_URL
        self.consumer: ConsumerMessages = None   # type: ignore
        self.elastic: ElasticSearchInsertData = None  # type: ignore 
       

    async def setup(self):
        self.consumer = ConsumerMessages(
            group_id=self.group_id,
            topics=self.consumer_topics
        )
        self.elastic = ElasticSearchInsertData()        
    
    async def manage_index(self, metadata_dict):
        """manage the ealsticsearch to add an index with document by id"""

        await self.elastic.create_index(metadata_dict)

    async def run(self):
        await self.setup()
        logger.info("the program start ")

        await self.consumer.consumer_loop(self.manage_index)
    
    async def main(self):
        await self.run()

if __name__ == "__main__":
    manager = Manager()
    asyncio.run(manager.main())

        
