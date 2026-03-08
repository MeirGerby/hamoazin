from elasticsearch import Elasticsearch 
from shared.core.config import settings 


class ElasticSearchCrud:
    def __init__(self):
        self.es = Elasticsearch(hosts=[settings.ELASTIC_URL]) 
        self.index_name = settings.ELASTIC_INDEX_NAME

    def get_all_data(self):
        """get all documents from the index"""
        data = self.es.search(
            index=self.index_name,
            query={
                'match_all': {}
            },
            pretty=True
        )
        return data 

    def get_audio_text(self):
        """get the text field content from the documents"""
        text = self.es.search(
            index=self.index_name,
            query={
                'query_string': {"query": 'file id'}
            }
        )
        return text 
    


es = ElasticSearchCrud()


data = es.get_audio_text()
print(data)
    

