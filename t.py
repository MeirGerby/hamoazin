from elasticsearch import Elasticsearch, helpers

es = Elasticsearch("http://localhost:9200")

# קבלת כל האינדקסים בפורמט JSON
indices = es.cat.indices(format="json")

# הדפסת שמות האינדקסים בלבד
index_names = [index['index'] for index in indices]
print(index_names)



query = {"query": {"match_all": {}}}
documents = helpers.scan(es, index=index_names, query=query)
print(list(documents)[0])
# for doc in documents:
#     print(type(doc)) 