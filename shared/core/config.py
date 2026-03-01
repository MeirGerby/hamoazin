from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    # kafka configuration 
    KAFKA_ADVERTISED_LISTENERS:str = "PLAINTEXT://localhost:9092"
    