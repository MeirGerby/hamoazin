from confluent_kafka import Consumer 
import json
from shared.logs.logs import Logger 

logger = Logger.get_logger()

class ConsumerMessages:
    def __init__(self, bootstrap_servers: str, topics: list, group_id: str):
        self.conf = {
            "bootstrap.servers": bootstrap_servers,
            "group.id": group_id,
            "auto.offset.reset": "earliest"
            }
        self.consumer = Consumer(self.conf)  # type: ignore
        self.topics = topics 
    
    async def consumer_loop(self, callback):
        """listening to kafka by topics"""
        self.consumer.subscribe(self.topics)
        logger.info(f"Consumer started. Listening to topics: {self.topics}...")
        try:
            while True:
                msg = self.consumer.poll(1.0) 
                if msg is None: continue 
                if msg.error():
                    # logging.error(f"Consumer error {msg.error}") 
                    logger.error(f"Consumer error {msg.error}") 
                    continue 
                try:
                    row_data = msg.value().decode('utf-8')  # type: ignore 
                    data: dict = json.loads(row_data)  
                    logger.info(f"Message received from topic {msg.topic()}: {data.get('filename', 'unknown file')}")

                    await callback(data)
                
                except json.JSONDecodeError:
                    logger.error(f"faild to decode the message")
                except Exception as e:
                    logger.exception(e)
        except KeyboardInterrupt:
            logger.warning('the consumer stoped by the user')

        finally:
            logger.info("close the connection")
            self.consumer.close()