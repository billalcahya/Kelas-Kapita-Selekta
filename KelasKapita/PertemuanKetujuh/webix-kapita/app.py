from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from config import MONGODB_COLLECTION_PRODUCTS,MONGODB_COLLECTION_USER,MONGODB_CONNECTION_STRING,MONGODB_DATABASE_NAME

app = Flask(__name__)
app.secret_key = "demo_session_kapita"

client = MongoClient(MONGODB_CONNECTION_STRING)
db = client[MONGODB_DATABASE_NAME]
collection = db[MONGODB_COLLECTION_PRODUCTS]

@app.route("/")
def index():
    return render_template("index.html")
    pass


@app.route("/api/data", methods=['GET'])
def get_all_data():
    documents = list(collection.find())
    return jsonify(documents)
    pass

@app.route('/api/data', methods=['POST'])
def add_products():
    data = request.get_json()
    
    products = db[MONGODB_COLLECTION_PRODUCTS].find(
            {},
            {"_id": 1}
        ).sort("_id", 1)
        
    max_id = 0
    for item in products:
        try:
            num = int(str(item["_id"])[3:])
            if num > max_id:
                max_id = num
        except:
            continue
            
    new_id = f"PRD{max_id + 1:03d}"
    
    new_product = {
        "_id" : new_id,
        "name" : data["name"],
        "category" : data["category"],
        "stock" : int(data["stock"]),
        "price" : int(data["price"]),
        "location" : data["location"]
    }
    
    result_insert = db[MONGODB_COLLECTION_PRODUCTS].insert_one(new_product)
    
    return jsonify({
        "status" : "success",
        "inserted_id" : str(result_insert.inserted_id),
        "product" : new_product
    })
    pass


if __name__ == "__main__":
    app.run(debug=True)
