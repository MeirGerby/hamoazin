import asyncio 

from shared.core.config import settings 
from shared.kafka.consumer import ConsumerMessages 
from shared.logs.logs import Logger 
from .service.handle_text import HandleText  
from .repository.calculate_words

logger = Logger()

class Manager:
    def __init__(self):     
        self.consumer = ConsumerMessages(
            group_id=settings.ROW_TEXT_GROUP_ID,
            topics=[settings.ROW_TEXT_TOPIC]
        )
        self.elastic = ElasticSearchGetData() 



    