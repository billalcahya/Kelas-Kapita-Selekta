from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
from config import MONGODB_COLLECTION_PRODUCTS,MONGODB_COLLECTION_USER,MONGODB_CONNECTION_STRING,MONGODB_DATABASE_NAME

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
