

from flask import Flask, request, abort
from mock_data import catalog
import json
import random
from config import db
from flask_cors import CORS 


app = Flask(__name__)
CORS(app) # *DANGER* anyone can connect to this server

me = {
        "name": "Mike",
        "last": "Mckitrick",
        "age": "37",
        "hobbies": [],
        "address": {
            "street": "Evergreen",
            "number": 42,
            "city":"Springfield"
        }
    }

@app.route("/")
def home():
    return "Hello from Python"

@app.route("/test")
def any_name():
    return "I'm a test function"

@app.route("/about")
def about():
    return me["name"]+" "+ me["last"]


#*********************************************
#***************API ENDPOINTS****************
#*********************************************



@app.route("/api/catalog")
def get_catalog():
    test = db.products.find({})
    print(test)

    return json.dumps(catalog)

@app.route("/api/catalog", methods=["post"])
def save_product():
    product = request.get_json()
    print (product)

    if not 'title' in product or len(product["title"]) < 5:
        return abort(400,"title is required, and should be at least 5 chars long")

    if not "price" in product:
        return abort(400, "Price is required")

    if not isinstance(product["price"], float) and not isinstance(product["price"], int):
        return abort(400, "Price should be a valid number")



    if product["price"]<= 0:
        return abort(400,"Price should be greater than zero")


   
    db.products.insert_one(product)

    print("----SAVED------")
    print(product)

    return json.dumps(product)

    return "OK"


@app.route("/api/cheapest")
def get_cheapest():
    cheap = catalog[0]
    for product in catalog:

        if product["price"] < cheap["price"]:
            cheap = product
    #find the cheapest products in catalog list
    return json.dumps(cheap)

@app.route("/api/product/<id>")
def get_product(id):
    #find the product whose _id is equal to id
    for product in catalog:
        if product["_id"] == id:
            return json.dumps(product)

    return "NOT FOUND"


    # return it as json
    
#end point to retrieve all products by catagory

@app.route("/api/catalog/<category>")
def get_by_category(category):
    result = []
    category = category.lower()
    for product in catalog:
        if product["category"].lower == category:
            result.append(product)

    return json.dumps(result)

@app.route("/api/categories")
def get_by_categories():
    result = []
    category = category.lower()
    for product in catalog:
        cat = product["category"]
        if cat not in result:
            result.append(cat)

    return json.dumps(result)

    

# GET /api/reports/prodCount
@app.route("/api/reports/prodCount")
def get_prod_count():
    count = len(catalog)
    return json.dumps(count)


@app.route("/api/reports/total")
def get_total():
    total = 0

    # print the title of each product
    for prod in catalog:
        
       
     # total is equal to current total plus (price times stock of current prod)
    
        totalProd= prod["price"] * prod["stock"]
        total += totalProd
        

    return json.dumps(total)

    # /api/reports/highestInvestment
@app.route("/api/reports/highestInvestment")
def get_highest_investment():
    highest = catalog[0]

    for prod in catalog:
        prod_invest = prod["price"] * prod["stock"]
        high_invest = highest["price"] * highest["stock"]

        if prod_invest > high_invest:
                highest = prod

    return json.dumps(highest)
#start the server
app.run(debug=True)