from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    # kafka configuration 
    KAFKA_ADVERTISED_LISTENERS:str = "PLAINTEXT://localhost:9092" 
    METADATA_TOPIC: str = "metadata_topic"
    # DATA 
    DATA_VOLUME: str = r"C:\Users\MEIRG\Downloads\podcasts\podcasts"
    


settings = Settings()