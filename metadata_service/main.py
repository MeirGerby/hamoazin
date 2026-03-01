from shared.core.config import settings
from shared.kafka.producer import Producer 
from .handle_file import FileMetadata 
class Manager:
    def __init__(self):
        self.folder = settings.DATA_VOLUME 

    
        

