from elasticsearch import Elasticsearch
import json 

class ElasticSearch:
    def __init__(self, index_name, file_metadata: dict, hosts: str):
        self.index_name = index_name 
        self.metadata: dict = file_metadata
        self.elastic = Elasticsearch(hosts=[hosts], verify_certs=False)

    def create_index(self, ):
        id = self.metadata.get('id', '')
        index = self.elastic.index(index=self.index_name, document=self.metadata, id=id) 
        print(f"the index added successfully {str(index)} ")
        

