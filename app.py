import os
from pymongo import MongoClient
from flask import Flask, request, render_template
from bson.json_util import dumps

app = Flask(__name__)

MONGO_URI = 'mongodb://sixsixone5:42577400Vj@ds133137.mlab.com:33137/heroku_mck6pbmw'
mongo = MongoClient(MONGO_URI)
mydb = mongo.heroku_mck6pbmw
mycol = mydb["products_548501935686874"]


# MONGO_URI = 'mongodb://sixsixone5:42577400Vj@ds133137.mlab.com:33137/heroku_mck6pbmw'
# mongo = MongoClient(MONGO_URI)
# mydb = mongo.heroku_mck6pbmw
# orderCollection = mydb.web_orders

# print("hello this is a value of customer_phones",mycol)

# @app.route('/')
# def hello():
#     return "Hello World!"

@app.route("/api/orders", methods = ['GET'])
def show():
    page_id = request.args.get('pageid')
    print("==> ", page_id)
    try:
        # phones = mydb.customer_phones.find( WHERE condition, selected_field ).limit(10)
        # selected_fields = {
        #     'PAGE_ID': 1,
        #     'PAGE_NAME': 1,
        #     '_id': 0
        # }
        # condition = {
        #     "PAGE_ID": page_id,
        # } if page_id else {}

        # var_name = value_if_CONDITION_is_true if CONDITION else value_if_CONDITION_is_false

        # orders = myCollection.find()
        orders = mycol.find()
        # for order in orders:
        #     print("-=-> ", order)

        data = {
            'orders': orders,
        }
    except Exception as e:
        print(e)
        return dumps("There is a problem")
    return dumps(data)


###### Page ######
@app.route('/')
def index():
    # get data
    customers_data = list(mycol.find())
    # for phone in phone_numbers:
    #     print(phone)
    return render_template('index.html', data=customers_data)

if __name__ == '__main__':
    app.run(debug=True)
