import pandas as pd
from elasticsearch import Elasticsearch, helpers, exceptions
global ES_CON

ELASTIC_PASSWORD = "<password>" #enter the password
numberOfRecords = '<Enter Number of Records to Fetch>' # enter integer value without quotes such as 10000
def connect_to_es():
    global ES_CON
    ES_CON = Elasticsearch('https://deployment-name-ce1e21.es.us-central1.gcp.cloud.es.io:portNumber', http_auth=(
        'elastic', ELASTIC_PASSWORD))

print('connected to elasticsearch!')

def get_logs(index_name, no_of_logs):
    global ES_CON
    logs = ES_CON.search(index=index_name, body={"size": no_of_logs, "query": {"match_all": {}}},timeout="10000s")
    logs = logs['hits']['hits']

    return pd.DataFrame([x['_source'] for x in logs])

connect_to_es()
df = get_logs('yourIndexId', numberOfRecords)

df.to_csv("myOutput.csv") #to save fetched data in a file
