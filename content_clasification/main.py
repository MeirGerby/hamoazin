from shared.core.config import settings 
from shared.repository.elasticsearch.get_data import ElasticSearchGetData 
from shared.kafka.consumer import ConsumerMessages 
from shared.logs.logs import Logger 
from .utils.decode_words import most_danger_words, less_danger_words

logger = Logger()

class Manager:
    def __init__(self): 
        self.consumer_topics = [settings.ROW_TEXT_TOPIC]
        self.group_id = settings.ROW_TEXT_GROUP_ID 

    