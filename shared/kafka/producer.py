from confluent_kafka import Producer 
import json 
from shared.logs.logs import Logger 

logger = Logger.get_logger()
class ProducerMessages:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.conf = {"bootstrap.servers": bootstrap_servers}
        self.producer = Producer(self.conf)  # type: ignore
        self.topic = topic 

    def delivary_report(self, err, msg):
        """report whether the delively succeed or not"""
        if err is not None:
            # print(f"Delivary failed {err}")
            logger.error(f"Delivary failed {err}") 
        else:
            # print(f"the msg send successfully {msg.value().decode("utf-8")}")
            logger.info(f"the msg send successfully {msg.value().decode("utf-8")}")  
    
    async def send_messege(self, message: dict): 
        """end a messege to kafka """
        try:
            # print(f"send message to {self.topic}")
            logger.info(f"send message to {self.topic}")  

            self.producer.produce(
                topic=self.topic,
                value=json.dumps(message).encode('utf-8'),
                on_delivery=self.delivary_report
            )
            self.producer.poll(0) 
            logger.info(f"the message send successfully,\n file's metadata: {message} \n topic: {self.topic}")

        except Exception as e:
            logger.exception(e)
    
    def close(self):
        """close the connection to kafka"""
        remaining = self.producer.flush(10)
        if remaining > 0:
            # print(f"Warrning: {remaining} the messages were not delivered")
            logger.warning(f"Warrning: {remaining} the messages were not delivered")
        else:
            logger.info("all messages delivered successfully! ")
        

