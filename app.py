import os
import json
from bson.json_util import dumps


import requests
from flask import Flask, request, url_for
from pymongo import MongoClient


app = Flask(__name__)

#Setting Environment for MongoDB
MONGO_URI = 'mongodb://dev:sousdey123@ds219676-a0.mlab.com:19676,ds219676-a1.mlab.com:19676/heroku_pkl108wc?replicaSet=rs-ds219676'
mongo = MongoClient(MONGO_URI)
db = mongo.heroku_pkl108wc  #connect with the database's name

# @app.route('/')
# def hello():
#     return "Hello World!"
#
#
# @app.route('/<name>')
# def hello_name(name):
#     return "Hello {}!".format(name)

@app.route("/api/phones", methods = ['GET'])
def show():
    page_id = request.args.get('pageid')
    print("==> ", page_id)
    try:
        # phones = db.customer_phones.find( WHERE condition, selected_field ).limit(10)
        selected_fields = {
            'PAGE_ID': 1,
            'PAGE_NAME': 1,
            '_id': 0
        }
        condition = {
            "PAGE_ID": page_id,
        } if page_id else {}

        # var_name = value_if_CONDITION_is_true if CONDITION else value_if_CONDITION_is_false

        phones = db.customer_phones.find(condition, selected_fields).limit(100)
        # for phone in phones:
        #     print("-=-> ", phone)

        data = {
            'phones': phones,
        }
    except Exception as e:
        print(e)
        return dumps("There is a problem")
    return dumps(data)


if __name__ == '__main__':
    app.run(debug=True)