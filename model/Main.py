# Main.py

# API Main Runner

from flask import Flask
from pymongo import MongoClient

api_port     = 20202
host         = '127.0.0.1'
app          = Flask(__name__)

mongo_port   = 27017
database_str = "BTProject2016_DB"
collection_str = "BTProject2016_Collection"
mongo_client = MongoClient(host=host,port=mongo_port)
mongo_db     = mongo_client[database_str]
mongo_collection = mongo_db[collection_str]

@app.route('/api/route',methods=['GET'])
def api_route():
    return "<html><head><title>Hello API</title></head><body><h3>Hello /api/route!</h3></body></html>"

app.run(host='0.0.0.0',port=20202)
