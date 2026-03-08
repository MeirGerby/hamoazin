from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    # kafka configuration 
    BOOTSTRAP_SERVERS: str = "localhost:9092"
    METADATA_TOPIC: str = "metadata_topic"
    METADATA_GROUP_ID: str = "metadata_consumer_group"
    PROCESSING_GROUP_ID: str = "infomation_processing"
    MONGO_AUDIO_TOPIC: str = "mongo_audio"
    MONGO_AUDIO_GROUP_ID: str = "mongo_audio"

    # DATA 
    # DATA_VOLUME: str = "C:/Users/MEIRG/Downloads/podcasts_extracted/podcasts"
    DATA_VOLUME: str = "/data/podcasts"

    # MONGODB 
    MONGODB_URL: str = "mongodb://localhost:27017/" 
    MONGO_DB: str = 'podcasts_db'
    MONGO_COLLECTION: str = "podcasts" 


    # elasticsearch 
    ELASTIC_URL: str = "http://localhost:9200" 
    # ELASTIC_URL: str = "http://elasticsearch:9200" 
    ELASTIC_INDEX_NAME: str = 'podcasts' 
    ELASTIC_INDEX_LOGS: str = "index_logs"
    
    # logs 
    LOGGER_NAME: str = "app.log"


settings = Settings()
    


