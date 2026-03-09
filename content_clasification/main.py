import asyncio 

from shared.core.config import settings 
from shared.kafka.consumer import ConsumerMessages 
from shared.logs.logs import Logger 
from .service.handle_text import HandleText  
from .service.decode_words import Decoder
from .repository.calculate_words import ElasticSearchCalculateWords

logger = Logger.get_logger()

class Manager:
    def __init__(self):     
        self.consumer = ConsumerMessages(
            group_id=settings.ROW_TEXT_GROUP_ID,
            topics=[settings.ROW_TEXT_TOPIC]
        )
        self.elastic: ElasticSearchCalculateWords = self.set_up()   # type: ignore

    def set_up(self):
        """
        this func sets up all the dependecies of this service. 
        """
        try:
            decoder = Decoder()
            self.handle_text = HandleText(decoder)
            elastic = ElasticSearchCalculateWords(self.handle_text) 

            logger.info("the program set up successfully!")
            return elastic
        except Exception as e:
            logger.exception(f"there's a problam while the program sets up, {e}")

    async def manager(self, data: dict):
        """
        this func contains all the functionality of this service.
        """
        try:

            words: dict = self.handle_text.get_words()
            lst = []
            for k,v in words.items():
                if k == 'danger_coupled_words' or k == 'less_danger_coupled_words':
                    query = self.elastic.create_word_query(v, boost=2, coupled=True)
                    lst.extend(query)  # type: ignore
                    logger.debug(f"create coupled text query. query {v}")
                elif k == "danger_words" or k == "less_danger_words":
                    query = self.elastic.create_word_query(v)
                    lst.extend(query)    # type: ignore
                    logger.debug(f"create single word query. query: {v}") 
            await self.elastic.calculate_words(queries=lst)
            
                
        except Exception as e:
            logger.exception(f"there is an error while combining all the functionality of the service {e}")


    async def run(self):
        try:
            await self.consumer.consumer_loop(self.manager)
        finally:
            await self.elastic.close()

if __name__ == "__main__":
    manager = Manager()
    asyncio.run(manager.run())