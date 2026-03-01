from confluent_kafka import Consumer 
import json 
import logging 

class ConsumerMessages:
    def __init__(self, bootstrap_servers: str, topics: list, group_id: str):
        self.conf = {
            "bootstrap.servers": bootstrap_servers,
            "group.id": group_id,
            "auto.reset.offset": "earlyest"
            }
        self.consumer = Consumer(self.conf)  # type: ignore
        self.topics = topics 
    
    async def consumer_loop(self, callback):
        """listening to kafka by topics"""
        self.consumer.subscribe(self.topics)
        try:
            while True:
                msg = self.consumer.poll(1.0) 
                if msg is None: continue 
                if msg.error():
                    logging.error(f"Consumer error {msg.error}") 
                    continue 
                data = json.loads(msg.value().decode('utf-8'))  # type: ignore 
                await callback(data)
        finally:
            self.consumer.close()