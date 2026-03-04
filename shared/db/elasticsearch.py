from elasticsearch import AsyncElasticsearch 

from shared.core.config import settings 

class ElasticSingleton:
    _instance = None 
    _client: AsyncElasticsearch = None  # type: ignore

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ElasticSingleton, cls).__new__(cls)

            cls._instance._client = AsyncElasticsearch(
                hosts=settings.ELASTIC_URL
            )
        return cls._instance 
    
    @property 
    def client(self) -> AsyncElasticsearch:
        """get the AsyncElasticsearch client"""
        return self._client 
    
    async def close(self): 
        """close the elastic connection"""
        if self._client:
            await self._client.close()