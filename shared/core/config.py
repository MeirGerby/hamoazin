from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    # kafka configuration 
    BOOTSTRAP_SERVERS: str = "localhost:9092"
    METADATA_TOPIC: str = "metadata_topic"
    KAFKA_GROUP_ID: str = ""
    
    # DATA 
    DATA_VOLUME: str = r"C:\Users\MEIRG\Downloads\podcasts_extracted\podcasts"

    # elasticsearch 
    ELASTIC_URL: str = "http://localhost:9200" 
    ELASTIC_INDEX_NAME: str = '' 
    
    


settings = Settings()