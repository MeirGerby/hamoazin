from elasticsearch import Elasticsearch
import json 

class ElasticSearch:
    def __init__(self, index_name, file_metadata: str, hosts):
        self.index_name = index_name 
        self.metadata: dict = json.loads(file_metadata)
        self.elastic: Elasticsearch = Elasticsearch(hosts=hosts)

    def create_index(self, ):
        id = self.metadata.get('id', '')
        index = self.elastic.index(index=self.index_name, document=self.metadata, id=id) 
        print(f"the index added successfully {str(index)} ")
        

