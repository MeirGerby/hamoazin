from confluent_kafka import Producer 
import json 

class ProducerMessages:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.conf = {"bootstrap.servers": bootstrap_servers}
        self.producer = Producer(self.conf)  # type: ignore
        self.topic = topic 

    def delivary_report(self, err, msg):
        """report whether the delively succeed or not"""
        if err is not None:
            print(f"Delivary failed {err}")
        else:
            print(f"the msg send successfully {msg}")
    
    async def send_messege(self, messege: dict): 
        """end a messege to kafka """
        try:
            print(f"send message to {self.topic}")

            self.producer.produce(
                topic=self.topic,
                value=json.dumps(messege).encode('utf-8'),
                on_delivery=self.delivary_report
            )
            self.producer.poll(0) 

        except Exception as e:
            print(e)
    
    def close(self):
        """close the connection to kafka"""
        remaining = self.producer.flush(10)
        if remaining > 0:
            print(f"Warrning: {remaining} the messages were not delivered")
        else:
            print("all messages delivered successfully! ")
        

