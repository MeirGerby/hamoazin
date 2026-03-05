from .transcription import SpeechManager
from shared.db.mongodb import MongoDB
from shared.kafka.consumer import ConsumerMessages 
from shared.core.config import settings 
from shared.logs.logs import Logger 


logger = Logger.get_logger()

class Manager:
    def __init__(self):
        self.mongo_db_name = settings.MONGO_DB 
        
        self.bootstrap_servers = settings.BOOTSTRAP_SERVERS
        self.metadata_topic = [settings.METADATA_TOPIC]
        self.group_id = settings.METADATA_GROUP_ID 

        self.convert_to_text = None
        self.consumer = None 


    async def setup(self):
        """setup the consumer for gettings the messages""" 
        self.consumer = ConsumerMessages(
            bootstrap_servers=self.bootstrap_servers,
            group_id=self.group_id,
            topics=self.metadata_topic
        )
        self.mongo_client = MongoDB()
        self.db = self.mongo_client.get_db(self.mongo_db_name)

    async def convert_file_to_text(self, path, speech_manager: SpeechManager):
        try:
            return speech_manager.recognition_from_file(path)
        except Exception as e:
            logger.error(e)

    async def manage_file(self, file_dict: dict):
        speech_manager = SpeechManager()

        id = file_dict.get('id', '')
        
        self.convert_to_text = await self.convert_file_to_text(file_path, speech_manager)

    async def run(self):
        await self.setup()
        logger.info("the program set up seccessfully")

        await self.consumer.consumer_loop(self.manage_file)  # type: ignore
        
    async def main(self):
        await self.run() 
