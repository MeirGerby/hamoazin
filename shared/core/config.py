from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    # kafka configuration 
    BOOTSTRAP_SERVERS: str = "localhost:9092"
    METADATA_TOPIC: str = "metadata_topic"
    # DATA 
    DATA_VOLUME: str = r"C:\Users\MEIRG\Downloads\podcasts_extracted\podcasts"

    # MONGODB 
    MONGODB_URL: str = "mongodb://localhost:27017/" 
    


settings = Settings()