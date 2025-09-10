from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

products = [
    {"id" : 1, "name" : "Laptop Dell", "category" : "Elektronik", "stock" : 15, "price" : 8500000, "location" : "A1-01"}, 
    {"id" : 2, "name" : "Mouse Wireless", "category" : "Aksesoris", "stock" : 50, "price" : 150000, "location" : "B2-05"}, 
    {"id" : 3, "name" : "Keyboard Mechanical", "category" : "Aksesoris", "stock" : 25, "price" : 750000, "location" : "B1-03"}, 
    {"id" : 4, "name" : "Monitor 24 inch", "category" : "Elektronik", "stock" : 8, "price" : 2500000, "location" : "A1-02"} 
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    for product in products:
        if product["id"] == product_id:
            product["name"] = data["name"]
            product["category"] = data["category"]
            product["stock"] = data["stock"]
            product["price"] = data["price"]
            product["location"] = data["location"]
            return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/api/products/<int:product_id>/stock', methods=['PATCH'])
def update_stock(product_id):
    data = request.get_json()
    for product in products:
        if product["id"] == product_id:
            qty = data.get("quantity", 1)
            if data["action"] == "add":
                product["stock"] += qty
            elif data["action"] == "subtract":
                product["stock"] = max(0, product["stock"] - qty)
            return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/api/products', methods=['POST'])
def add_products():
    data = request.get_json()
    # Mencari ID terbesar
    max_id = 0
    for product in products:
        if product['id'] > max_id:
            max_id = product['id']
            
    new_id = max_id + 1
    
    new_product = {
        "id" : new_id,
        "name" : data['name'],
        "category" : data['category'],
        "stock" : data['stock'],
        "price" : data['price'],
        "location" : data['location']
    }
    
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_products(product_id):
    global products
    
    #Tahap 4 : Menghapus produk dengan loop dan list baru
    new_products = []
    for product in products:
        if product['id'] != product_id:
            new_products.append(product)
            
    products = new_products
    return jsonify({"message" : "Product deleted"})

if __name__ == '__main__':
    app.run(debug=True)