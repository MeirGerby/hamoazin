from elasticsearch import Elasticsearch
import json 

class ElasticSearch:
    def __init__(self, index_name, file_metadata: str):
        self.index_name = index_name 
        self.metadata: dict = json.loads(file_metadata)

    def create_index(self, elastic: Elasticsearch):
        id = self.metadata.get('id', '')
        index = elastic.index(index=self.index_name, document=self.metadata, id=id) 
        print(f"the index added successfully {str(index)} ")
        

