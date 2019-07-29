import os
from pymongo import MongoClient
from flask import Flask, request

app = Flask(__name__)

#Setting Environment for MongoDB
MONGO_URI = 'mongodb://dev:sousdey123@ds219676-a0.mlab.com:19676,ds219676-a1.mlab.com:19676/heroku_pkl108wc?replicaSet=rs-ds219676'
mongo = MongoClient(MONGO_URI)
db = mongo["heroku_pkl108wc"]  #connect with the database's name

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()