import asyncio

from shared.kafka.consumer import ConsumerMessages
from shared.core.config import settings 
from .elastic import ElasticSearch, Elasticsearch

class Manager:
    def __init__(self):
        self.bootstrap_servers = settings.BOOTSTRAP_SERVERS
        self.topics = [settings.METADATA_TOPIC]
        self.group_id = settings.PROCESSING_GROUP_ID 

        self.index_name = settings.ELASTIC_INDEX_NAME 
        self.elastic_url = settings.ELASTIC_URL

        self.consumer: ConsumerMessages = None   # type: ignore
        self.elastic_con: ElasticSearch = None  # type: ignore 
       

    async def setup(self):
        self.consumer = ConsumerMessages(
            bootstrap_servers=self.bootstrap_servers,
            group_id=self.group_id,
            topics=self.topics
        )
        
    
    async def manage_index(self, metadata_dict):
        self.elastic_con = ElasticSearch(
            index_name=self.index_name, 
            file_metadata=metadata_dict, 
            hosts=settings.ELASTIC_URL
        )
        """manage the ealsticsearch to add an index with document by id"""
        self.elastic_con.create_index()

    async def run(self):
        await self.setup()
        print("the program start ")

        await self.consumer.consumer_loop(self.manage_index)
    
    async def main(self):
        await self.run()

if __name__ == "__main__":
    manager = Manager()
    asyncio.run(manager.main())

        
