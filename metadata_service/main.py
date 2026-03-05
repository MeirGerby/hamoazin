import os 
import asyncio
from uuid import uuid4 

from shared.core.config import settings
from shared.kafka.producer import ProducerMessages  
from .handle_file import FileMetadata 
from shared.logs.logs import Logger 

logger = Logger.get_logger()
class Manager:
    def __init__(self):
        self.folder = settings.DATA_VOLUME 
        self.metadata_topic = settings.METADATA_TOPIC
        self.bootstrap_servers = settings.BOOTSTRAP_SERVERS
        self.producer: ProducerMessages = None  # type: ignore
        self.handle_file: FileMetadata = None  # type: ignore

    def setup(self):
        """create the producer instance"""
        self.producer = ProducerMessages(self.bootstrap_servers, self.metadata_topic) 

    async def run(self):
        try:
            for i in os.listdir(self.folder):
                absulut_path = os.path.join(self.folder, i)

                self.handle_file = FileMetadata(absulut_path)
                file_metadata = self.handle_file.add_metadata()

                file_metadata["path"] = absulut_path 
                file_metadata['_id'] = str(uuid4())
                file_metadata['filename'] = i

                await self.producer.send_messege(file_metadata)

        except FileNotFoundError as f:
            print(f)
        finally:
            self.producer.close()
        
    async def main(self):
        self.setup()
        await self.run()

    
if __name__ == "__main__":
    manager = Manager()
    asyncio.run(manager.main())
    

    

        

