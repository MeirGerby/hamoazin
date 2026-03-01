from shared.kafka.consumer import Consumer
from shared.core.config import settings 

class Manager:
    def __init__(self):
        self.bootstrap_servers = settings.BOOTSTRAP_SERVERS
        self.topics = settings.METADATA_TOPIC 
        self.group_id = settings.KAFKA_GROUP_ID
        
