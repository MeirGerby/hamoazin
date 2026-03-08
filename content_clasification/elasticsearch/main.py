from elasticsearch import Elasticsearch 
from shared.core.config import settings 


class ElasticSearchCrud:
    def __init__(self):
        self.es = Elasticsearch(hosts="http://localhost:9200") 
        self.index_name = 'podcasts'

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
    


es = Elasticsearch(hosts=["http://localhost:9200"]) 
index_name = 'podcasts'
def get_audio_text():
    """get the text field content from the documents"""
    text = es.search(
        index=index_name,
        query={
            'query_string': {"query": 'file id'}
        }
    )
    return text 
data = get_audio_text()
print(data)
    

