from motor.motor_asyncio import AsyncIOMotorClient

from shared.core.config import settings
from shared.logs.logs import Logger 

logger = Logger.get_logger()
class MongoDB:
    _instance = None 
    _client: AsyncIOMotorClient  = None   # type: ignore

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MongoDB, cls).__new__(cls)

            mongodb_url = settings.MONGODB_URL
            cls._instance._client = AsyncIOMotorClient(mongodb_url)
        return cls._instance
    
     
    def get_db(self, db_name):
        """get the mongodb db"""
        logger.info("get the mongodb db name")
        return self._client.get_database(db_name)

    @property  
    def client(self) -> AsyncIOMotorClient:
        """get the mongodb client"""
        logger.info("get the mongodb client")
        return self._client
        
    async def close(self):
        """close the AsyncMotorClient connection"""
        if self._client:
            self._client.close()
            self._instance = None 
            self._client = None   # type: ignore
            logger.info("close the mongodb connection")
