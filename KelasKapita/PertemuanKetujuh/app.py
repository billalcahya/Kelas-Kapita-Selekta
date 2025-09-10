from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    session,
    flash,
    redirect,
    url_for,
    get_flashed_messages,
)

from common.mongo_connection import MongoConnection
from config import (
    MONGODB_COLLECTION_PRODUCTS,
    MONGODB_COLLECTION_USER,
    MONGODB_CONNECTION_STRING,
    MONGODB_DATABASE_NAME,
)

app = Flask(__name__)
app.secret_key = "demo_session_kapita"

mongo = MongoConnection(
    connection_string=MONGODB_CONNECTION_STRING, db_name=MONGODB_DATABASE_NAME
)

users = {
    "admin": {"password": "admin123", "role": "admin"},
    "staff": {"password": "staff123", "role": "staff"},
}


@app.route("/")
def index():
    auth_check = check_login()
    if auth_check:
        return auth_check
    return render_template(
        "index.html", username=session["username"], role=session["role"]
    )


def check_login():
    if "username" not in session:
        return redirect(url_for("login"))
    return None


def check_admin():
    login_check = check_login()
    if login_check:
        return login_check
    if session.get("role") != "admin":
        return jsonify({"error": "Butuh akses admin!"}), 403
    return None


@app.route("/logout")
def logout():
    session.clear()
    flash("Logout berhasil!", "success")
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and password == users[username]["password"]:
            session["username"] = username
            session["role"] = users[username]["role"]
            flash("Login berhasil", "success")
            return redirect(url_for("index"))

        else:
            flash("Username atau password salah", "error")
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/api/products", methods=["GET"])
def get_products():
    auth_check = check_login()
    if auth_check:
        return auth_check

    result_products = mongo.find(MONGODB_COLLECTION_PRODUCTS, {}, multi=True)
    return result_products


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404


@app.route("/api/products/<int:product_id>", methods=["PUT"])
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


@app.route("/api/products/<int:product_id>/stock", methods=["PATCH"])
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


# POST - Menambah produk baru
@app.route("/api/products", methods=["POST"])
def add_products():
    auth_check = check_admin()
    if auth_check:
        return auth_check

    data = request.get_json()

    # Ambil semua _id produk, karena _id berupa string (PRDxxx) jadi harus dicari angka terbesarnya
    products = mongo.find(
        MONGODB_COLLECTION_PRODUCTS,
        {},
        project={"_id": 1},
        sort=[("_id", 1)],
        multi=True,
    )

    max_id = 0
    if products.get("status") and products.get("data"):
        for item in products["data"]:
            try:
                # Ambil angka setelah prefix "PRD"
                num = int(str(item["_id"])[3:])
                if num > max_id:
                    max_id = num
            except:
                continue

    # Buat ID baru berdasarkan angka terbesar
    new_id = f"PRD{max_id + 1:03d}"

    new_product = {
        "_id": new_id,
        "name": data["name"],
        "category": data["category"],
        "stock": int(data["stock"]),
        "price": int(data["price"]),
        "location": data["location"],
    }

    result_insert = mongo.insert(MONGODB_COLLECTION_PRODUCTS, new_product)

    return jsonify(result_insert), 201


@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_products(product_id):
    global products

    # Tahap 4 : Menghapus produk dengan loop dan list baru
    new_products = []
    for product in products:
        if product["id"] != product_id:
            new_products.append(product)

    products = new_products
    return jsonify({"message": "Product deleted"})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
