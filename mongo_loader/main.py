import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

from shared.kafka.producer import ProducerMessages
from shared.kafka.consumer import ConsumerMessages 
from shared.core.config import settings 
from shared.logs.logs import Logger 
from shared.repository.mongodb.gridfs import MongoDBHandler

logger = Logger.get_logger()
class Manager:
    def __init__(self):
        self.mongo_url = settings.MONGODB_URL 
        self.mongo_db_name = settings.MONGO_DB 
        self.bootstrap_servers = settings.BOOTSTRAP_SERVERS
        self.metadata_topic = [settings.METADATA_TOPIC]
        self.group_id = settings.METADATA_GROUP_ID 
        self.mongo_audio_topic = settings.MONGO_AUDIO_TOPIC
        self.mongo_loader = None
        self.consumer = None 
        self.db = None 


    async def setup(self):
        """setup the consumer for gettings the messages""" 
        self.consumer = ConsumerMessages(
            group_id=self.group_id,
            topics=self.metadata_topic
        )
        self.producer = ProducerMessages(self.mongo_audio_topic)
        self.mongo_client = AsyncIOMotorClient(self.mongo_url)
        self.db = self.mongo_client[self.mongo_db_name]

    async def manage_file(self, file_dict: dict):
        try:
            self.mongo_loader = MongoDBHandler(
                # file_path=file_dict.get('path'), 
                filename=file_dict.get('filename')
                )
            id = file_dict.get('id')

            await self.mongo_loader.send_file(id)
            await self.producer.send_messege(file_dict)

        except Exception as e:
            logger.error(e)

        finally:
            self.producer.close()


    async def run(self):
        await self.setup()
        logger.info("the program set up seccessfully")

        await self.consumer.consumer_loop(self.manage_file)  # type: ignore
        
    async def main(self):
        await self.run() 

if __name__ == "__main__":
    manager = Manager()
    asyncio.run(manager.main())