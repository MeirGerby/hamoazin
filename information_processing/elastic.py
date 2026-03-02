from elasticsearch import Elasticsearch
import json 

class ElasticSearch:
    def __init__(self, index_name, hosts: str):
        self.index_name = index_name 
        self.elastic = Elasticsearch(hosts=[hosts], verify_certs=False)

    def create_index(self, metadata: dict):
        id = metadata.get('id', '')
        index = self.elastic.index(index=self.index_name, document=metadata, id=id) 
        print(f"the index added successfully {str(index)} ")
        

