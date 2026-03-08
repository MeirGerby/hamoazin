from elasticsearch import Elasticsearch 
from shared.logs.logs import Logger 

logger = Logger.get_logger()


class ElasticSearchCrud:
    def __init__(self, index_name, hosts):
        self.es = Elasticsearch(hosts=[hosts], verify_certs=False) 
        self.index_name = index_name 


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
    

