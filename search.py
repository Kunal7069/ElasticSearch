
from elasticsearch import Elasticsearch

# Credentials
username = "elastic"
password = "=xEYoi1zDUYfJT=T+9Ff"

# Connect to Elasticsearch (assuming it's running on localhost:9200)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}],http_auth=(username, password),verify_certs=True)

# Check if Elasticsearch is running
if es.ping():
    print("Connected to Elasticsearch")
else:
    print("Unable to connect to Elasticsearch")

# Example: Create an index
index_name = "my_index_3"
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)
    print(f"Index '{index_name}' created")

# Search an entry
query = {
    "query": {
        "bool": {
            "must": [
                {"match": {"name": "KUNAL JAIN"}},
                {"match": {"age" : 21}}
            ]
        }
    }
}   


# Delete the document   sUhkD4wBWMTfwZjkEGty  s0hqD4wBWMTfwZjkBGtT skhkD4wBWMTfwZjkeWuB
es.delete(index=index_name, doc_type='_doc', id="wrWFHIwBd1s5YqUxabjA")

# Example: Index a document
# document = [{"name": "AMAN", "age": 21 , "city":"Aligarh"},{"name": "AMAN 2", "age": 21 , "city":"Aligarh"}]
# es.index(index=index_name, body=document[2])
# print("Document indexed")

document = [{"name": "AMAN", "age": 21 , "city":"Aligarh"},{"name": "AMAN 2", "age": 21 , "city":"Aligarh"}]

# for entry in document:
#     es.index(index=index_name, body=entry)
    


# Example: Search for documents
result = es.search(index=index_name, body={"query": {"match_all": {}}})
print(result)

# print("Search Results:")
for hit in result["hits"]["hits"]:
    print(hit["_source"])

# Close the Elasticsearch connection
es.close()
