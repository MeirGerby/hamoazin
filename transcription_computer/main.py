import os
from motor.motor_asyncio import AsyncIOMotorClient 

from .transcription import SpeechManager
from .gridfs import MongoDB
# from shared.kafka.producer import ProducerMessages
from shared.kafka.consumer import ConsumerMessages 
from shared.core.config import settings 
from shared.logs.logs import Logger 


logger = Logger.get_logger()

class Manager:
    def __init__(self):
        self.mongo_db_name = settings.MONGO_DB
        self.mongo_url = settings.MONGODB_URL 
        self.bootstrap_servers = settings.BOOTSTRAP_SERVERS
        self.mongo_audio_topic = [settings.MONGO_AUDIO_TOPIC]
        self.group_id = settings.MONGO_AUDIO_GROUP_ID 

        self.mongo_client: AsyncIOMotorClient = None  # type: ignore
        self.convert_to_text = None
        self.consumer = None 
        self.speech_manager: SpeechManager = None   # type: ignore
        self.mongo_do: MongoDB = None    # type: ignore


    async def setup(self):
        """setup the consumer for gettings the messages""" 
        self.consumer = ConsumerMessages(
            bootstrap_servers=self.bootstrap_servers,
            group_id=self.group_id,
            topics=self.mongo_audio_topic
        )
        # self.producer = ProducerMessages(self.bootstrap_servers, self.metadata_topic) 
        self.mongo_client = AsyncIOMotorClient(self.mongo_url)
        self.db = self.mongo_client[self.mongo_db_name]
        self.collection = self.db.get_collection(settings.MONGO_COLLECTION)
        self.speech_manager = SpeechManager()
        self.mongo_db = MongoDB(self.db)

    async def convert_file_to_text(self, path, speech_manager: SpeechManager):
        try:
            return speech_manager.recognition_from_file(path)
        except Exception as e:
            logger.error(e)

    async def manage_file(self, file_dict: dict):
        
        try:
            filename = file_dict.get('filename')
            local_path = f"temp/{filename}" 
            await self.mongo_db.get_file(local_path, filename) 
            os.remove(local_path)
            
            self.convert_to_text = await self.convert_file_to_text(local_path, self.speech_manager)
        except Exception as e:
            logger.error(e)

    async def run(self):
        await self.setup()
        logger.info("the program set up seccessfully")

        await self.consumer.consumer_loop(self.manage_file)  # type: ignore
        
    async def main(self):
        await self.run() 

if __name__ == "__main__":
    import asyncio
    manager = Manager()
    asyncio.run(manager.main())