#
# octronic/uib-project-template/model/Main.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from flask import Flask
from pymongo import MongoClient

api_host         = '127.0.0.1'
api_port         = 9090
app              = Flask(__name__)

mongo_host       = '127.0.0.1'
mongo_port       = 27017
database_str     = "UIB_Template_Project_DB"
collection_str   = "UIB_Template_Project_Collection"
mongo_client     = MongoClient(host=mongo_host,port=mongo_port)
mongo_db         = mongo_client[database_str]
mongo_collection = mongo_db[collection_str]

@app.route('/api/route',methods=['GET'])
def api_route():
    return "<html><head><title>Hello API</title></head><body><h3>Hello /api/route!</h3></body></html>"

if __name__ == '__main__':
    app.run(host=api_host,port=api_port)
