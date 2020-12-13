from pymongo import MongoClient, errors
import json

#mongo conn
def mongo_conn(PORT=27017, HOST='localhost'):
    try:
# pass 'host' variables when calling MongoClient()
        client = MongoClient( host = [str(HOST) + ":" + str(PORT)],
                              serverSelectionTimeoutMS = 3000
                            )
    except errors.ServerSelectionTimeoutError as err:
        print("Error trying to connect to mongo")
    
    return client

#mongo save_data
def save_data(conn, data):
    db = conn['sojadb']
    col = db['sojacol']

    _ = col.insert_one(data)

#mongo get_data
def show_data(conn):
    db = conn['sojadb']
    col = db['sojacol']

    docs = col.find()

    results = []

    for doc in docs:
        results.append({
            'id': str(doc['_id']),
            'temperatura': doc['temperatura'],
            'umidade': doc['umidade'],
            'ph': doc['ph'],
            'vento': doc['vento']
        })
    
    return json.dumps(results, indent=4)