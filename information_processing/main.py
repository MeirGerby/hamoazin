import asyncio

from shared.kafka.consumer import ConsumerMessages 
# from shared.kafka.producer import ProducerMessages
from shared.core.config import settings 
from shared.logs.logs import Logger 
from .elastic import ElasticSearch


logger = Logger.get_logger()
class Manager:
    def __init__(self):
        # kafka 
        self.bootstrap_servers = settings.BOOTSTRAP_SERVERS

        # kafka consumer
        self.consumer_topics = [settings.METADATA_TOPIC]    
        self.group_id = settings.PROCESSING_GROUP_ID 

        # # kafka producer
        # self.mongo_audio_topic = settings.MONGO_AUDIO_TOPIC
        
        # elastic 
        self.index_name = settings.ELASTIC_INDEX_NAME 
        self.elastic_url = settings.ELASTIC_URL

        self.consumer: ConsumerMessages = None   # type: ignore
        self.elastic_con: ElasticSearch = None  # type: ignore 
       

    async def setup(self):
        self.consumer = ConsumerMessages(
            bootstrap_servers=self.bootstrap_servers,
            group_id=self.group_id,
            topics=self.consumer_topics
        )
        self.elastic_con = ElasticSearch(
            index_name=self.index_name, 
            hosts=settings.ELASTIC_URL
        )
        # self.producer = ProducerMessages(self.bootstrap_servers, self.mongo_audio_topic) 
        
    
    async def manage_index(self, metadata_dict):
        """manage the ealsticsearch to add an index with document by id"""

        self.elastic_con.create_index(metadata_dict)
        # await self.producer.send_messege(metadata_dict)

    async def run(self):
        await self.setup()
        logger.info("the program start ")

        await self.consumer.consumer_loop(self.manage_index)
    
    async def main(self):
        await self.run()

if __name__ == "__main__":
    manager = Manager()
    asyncio.run(manager.main())

        
