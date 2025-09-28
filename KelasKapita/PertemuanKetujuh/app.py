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

        user = mongo.find(MONGODB_COLLECTION_USER, {"_id": username}, multi=False)

        if user.get("status") and user.get("data"):
            db_user = user["data"]
            # Cek password
            if password == db_user["password"]:
                session["username"] = db_user["_id"]
                session["role"] = db_user["role"]
                flash("Login berhasil", "success")
                return redirect(url_for("index"))
            else:
                flash("Password salah", "error")
        else:
            flash("Username tidak ditemukan", "error")

        return render_template("login.html")
    return render_template("login.html")


@app.route("/api/products", methods=["GET"])
def get_products():
    auth_check = check_login()
    if auth_check:
        return auth_check

    result_products = mongo.find(MONGODB_COLLECTION_PRODUCTS, {}, multi=True)
    return result_products


@app.route("/api/products/<string:product_id>", methods=["GET"])
def get_product(product_id):
    product = mongo.find(MONGODB_COLLECTION_PRODUCTS, {"_id": product_id}, multi=False)
    if product.get("status") and product.get("data"):
        return jsonify(product["data"])
    return jsonify({"error": "Product not found"}), 404


@app.route("/api/products/<string:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    update_data = {
        "name": data["name"],
        "category": data["category"],
        "stock": int(data["stock"]),
        "price": int(data["price"]),
        "location": data["location"],
    }
    result = mongo.update(MONGODB_COLLECTION_PRODUCTS, {"_id": product_id}, update_data)
    if result.get("status"):
        return jsonify({"message": "Product updated", "data": update_data})
    return jsonify({"error": "Product not found"}), 404


@app.route("/api/products/<string:product_id>/stock", methods=["PATCH"])
def update_stock(product_id):
    data = request.get_json()
    qty = data.get("quantity", 1)
    action = data.get("action")

    product = mongo.find(MONGODB_COLLECTION_PRODUCTS, {"_id": product_id}, multi=False)
    if not product.get("status") or not product.get("data"):
        return jsonify({"error": "Product not found"}), 404

    current_stock = int(product["data"]["stock"])
    if action == "add":
        new_stock = current_stock + qty
    elif action == "subtract":
        new_stock = max(0, current_stock - qty)
    else:
        return jsonify({"error": "Invalid action"}), 400

    result = mongo.update(
        MONGODB_COLLECTION_PRODUCTS, {"_id": product_id}, {"stock": new_stock}
    )
    return jsonify({"message": "Stock updated", "new_stock": new_stock})


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


@app.route("/api/products/<string:product_id>", methods=["DELETE"])
def delete_products(product_id):
    result = mongo.delete(MONGODB_COLLECTION_PRODUCTS, {"_id": product_id})
    if result.get("status"):
        return jsonify({"message": "Product deleted"})
    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
