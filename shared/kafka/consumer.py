from confluent_kafka import Consumer 
import json 

class ConsumerMesseges:
    def __init__(self, bootstrap_servers: str, topics: list, group_id: str):
        self.conf = {
            "bootstrap.servers": bootstrap_servers,
            "group.id": group_id,
            "auto.reset.offset": "earlyest"
            }
        self.topics = topics 
    
    