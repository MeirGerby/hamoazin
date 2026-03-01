from shared.core.config import settings
from shared.kafka.producer import ProducerMessages  
from .handle_file import FileMetadata 
class Manager:
    def __init__(self):
        self.folder = settings.DATA_VOLUME 
        self.metadata_topic = settings.METADATA_TOPIC
        self.bootstrap_servers = settings.BOOTSTRAP_SERVERS
        self.producer: ProducerMessages = None  # type: ignore

    async def setup(self):
        """create the producer instance"""
        self.producer = ProducerMessages(self.bootstrap_servers, self.metadata_topic)

    

        

