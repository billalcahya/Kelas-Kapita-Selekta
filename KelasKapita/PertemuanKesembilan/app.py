from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    jsonify,
)
from flask_session import Session
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from config import (
    SECRET_KEY,
    MONGO_CONNECTION_STRING,
    MONGO_DATABASE_NAME,
    MONGO_COLLECTION_PRODUCTS,
    MONGO_COLLECTION_USER,
    SESSION_TYPE,
    SESSION_PERMANENT,
    SESSION_USE_SIGNER,
    SESSION_REDIS,
)

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Setup Mongodb
client = MongoClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DATABASE_NAME]
users = db[MONGO_COLLECTION_USER]
collections = db[MONGO_COLLECTION_PRODUCTS]

# Setup redis
app.config["SESSION_TYPE"] = SESSION_TYPE
app.config["SESSION_PERMANENT"] = SESSION_PERMANENT
app.config["SESSION_USE_SIGNER"] = SESSION_USE_SIGNER
app.config["SESSION_REDIS"] = SESSION_REDIS
Session(app)


def check_login():
    if "username" not in session:
        return redirect(url_for("login"))
    return None


def check_admin():
    login_check = check_login()
    if login_check:
        return login_check
    if session.get("role") != "admin":
        return jsonify({"error" : "Butuh akses admin"}), 403
    return None


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Username dan password wajib diisi", "error")

        user = users.find_one({"_id": username})

        if user and user.get("password") == password:
            session["username"] = user["_id"]
            session["role"] = user.get("role", "staff")

            flash("Login berhasil", "success")
            return redirect(url_for("index"))
        else:
            flash("Username atau password salah", "error")
            return redirect(url_for("login"))
    return render_template("login.html")
    pass


@app.route("/logout")
def logout():
    session.clear()
    flash("Berhasil Logout", "success")
    return redirect(url_for("login"))
    pass


@app.route('/')
def index():
    auth_check = check_admin()
    if auth_check:
        return auth_check
    return render_template("index.html", username = session["username"], role = session["role"])
    pass


@app.route('/api/data', methods=['GET'])
def get_all_products():
    auth_check = check_login()
    if auth_check:
        return auth_check

    products = list(db[MONGO_COLLECTION_PRODUCTS].find())
    for p in products:
        p["_id"] = str(p["_id"])
    return jsonify({"status": "success", "products": products}), 200


@app.route('/api/data/<string:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    auth_check = check_login()
    if auth_check:
        return auth_check

    product = db[MONGO_COLLECTION_PRODUCTS].find_one({"_id": product_id})
    if not product:
        return jsonify({"status": "error", "message": "Produk tidak ditemukan"}), 404

    product["_id"] = str(product["_id"])
    return jsonify({"status": "success", "product": product}), 200

@app.route('/api/data', methods=['POST'])
def add_products():
    try:
        auth_check = check_admin()
        if auth_check:
            return auth_check
        data = request.get_json()
        
        if not data :
            return jsonify({"status" : "error", "message" : "Request harus berupa JSON"}),400
        
        required_fields = ["name", "category", "stock", "price", "location"]
        for fields in required_fields:
            if fields not in data:
                return jsonify({"status" : "error", "message" : f"Field '{fields}' wajib diisi"}), 400
            
        try: 
            name = str(data.get("name", "")). strip()
            category = str(data.get("category","")).strip()
            stock = int(data.get("stock", 0))
            price = int(data.get("price", 0))
            location = str(data.get("location", "")).strip()
        except ValueError:
            return jsonify({"status" : "error", "message" : "Stock dan price harus berupa angka"}), 400
        
        if not name:
            return jsonify({"status" : "error", "message" : "Nama produk tidak boleh kosong"}), 400
        if stock < 0 :
            return jsonify({"status" : "error", "message" : "Stock tidak boleh negatif"}), 400
        if price < 0 :
            return jsonify({"status" : "error", "message" : "Harga tidak boleh negatif"}), 400
        
        products = db[MONGO_COLLECTION_PRODUCTS].find({}, {"_id" : 1}).sort("_id", 1)
        max_id = 0
        for item in products:
            try:
                num = int(str(item["_id"][3:]))
                if num > max_id:
                    max_id = num
            except (ValueError, KeyError):
                continue
            
        new_id = f"PRD{max_id + 1:03d}"
        
        new_product = {
            "_id" : new_id,
            "name" : name,
            "category" : category,
            "stock" : stock,
            "price" : price,
            "location" : location
        }
        
        try:
            result_insert = db[MONGO_COLLECTION_PRODUCTS].insert_one(new_product)
        except PyMongoError as e:
            return jsonify({"status":"error", "message":f"gagal menyimpan ke database : {str(e)}"}), 500
        
        return jsonify({
            "status" : "success",
            "inserted_id" : str(result_insert.inserted_id),
            "product" : new_product
        }), 201
        
    except Exception as e:
        return jsonify({"status" : "error", "message" : f"Terjadi kesalahan : {str(e)}"}), 500
    pass

@app.route('/api/data/<string:product_id>', methods=['PUT'])
def updated_product_id(product_id):
    try:
        auth_check = check_admin()
        if auth_check:
            return auth_check
        
        data = request.get_json()
        if not data :
            return jsonify({"status" : "error", "message" : "Request harus berupa JSON"}), 400
    
        required_fields = ["name", "category", "stock", "price", "location"]
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "status" : "error",
                    "message" : f"field '{field}' wajib diisi"
                }), 400
        
        try:
            name = str(data.get("name", "")).strip()
            category = str(data.get("category", "")).strip()
            stock = int(data.get("stock", 0))
            price = int(data.get("price", 0))
            location = str(data.get("location", "")).strip()
        except ValueError:
            return jsonify({
                "status" : "error",
                "message" : "Stock dan price harus berupa angka"
            }), 400
            
        if not name:
            return jsonify({"status" : "error", "message" : "Nama produk tidak boleh kosong"}), 400
        if stock < 0 :
            return jsonify({"status" : "error", "message" : "Stock tidak boleh negatif"}), 400
        if price < 0 :
            return jsonify({"status" : "error", "message" : "Harga tidak boleh negatif"}), 400
        
        
        update_data = {
            "name" : name,
            "category" : category,
            "stock" : stock,
            "price" : price,
            "location" : location
        }
        
        try:
            result = db[MONGO_COLLECTION_PRODUCTS].update_one({"_id" : product_id}, {"$set" : update_data})
        except PyMongoError as e:
            return jsonify({
                "status" : "error",
                "message" : f"gagal mengupdate ke database : {str(e)}"
            }), 500
            
        if result.matched_count == 0:
            return jsonify({
                "status" : "error",
                "message" : "produk tidak ditemukan"
            }), 404
            
        return jsonify({
            "status" : "success",
            "updated_id" : product_id,
            "modified_count" : result.modified_count
        }),200
        
    except Exception as e:
        return jsonify({
            "status" : "error",
            "message" : f"Terjadi kesalahan : {str(e)}"
        }), 500
    pass


@app.route('/api/data/<string:product_id>', methods=['PATCH'])
def update_stock(product_id):
    try:
        # cek admin
        auth_check = check_admin()
        if auth_check:
            return auth_check
        
        # cek request json valid
        data = request.get_json()
        if not data :
            return jsonify({
                "status" : "error",
                "message" : "request harus berupa JSON"
            }), 400
        
        # ambil dan validasi field wajib
        action = data.get("action")
        if action not in ["add", "subtract"]:
            return jsonify({
                "status" : "error",
                "message" : "field action wajib diisi dengan add atau sub"
            }), 400
            
        # validasi qty
        try:
            qty = int(data.get("quantity", 1))
        except ValueError:
            return jsonify({
                "status" : "error",
                "message" : "field qty harus berupa angka"
            }), 400
        
        if qty <= 0:
            return jsonify({
                "status" : "error",
                "message" : "qty harus lebih besar dari 0"
            }), 400
            
        # cek produk ada 
        product = db[MONGO_COLLECTION_PRODUCTS].find_one({"_id" : product_id})
        if not product:
            return jsonify({
                "status" : "error",
                "message" : "produk tidak ditemukan"
            }), 404
        
        # ambil stok
        try:
            current_stock = int(product.get("stock", 0))
        except ValueError:
            return jsonify({
                "status" : "error",
                "message" : "data stok di database tidak valid"
            }), 500
            
        # hitung stok baru
        if action == "add" :
            new_stock = current_stock + qty
        elif action == "subtract" :
            if current_stock - qty < 0:
                return jsonify({
                    "status" : "error",
                    "message" : "stok tidak cukup untuk dikurangi"
                }), 400
            new_stock = current_stock - qty
        
        # update ke db
        try:
            result = db[MONGO_COLLECTION_PRODUCTS].update_one({"_id" : product_id}, {"$set" : {"stock" : new_stock}})
        except PyMongoError as e:
            return jsonify({
                "status" : "error",
                "message" : f"gagal mengupdate ke db {str(e)}"
            }), 500

        # sukses
        return jsonify({
            "status" : "success",
            "message" : "stok berhasil diperbaharui",
            "updated_id" : product_id,
            "old_stock" : current_stock,
            "new_stock" : new_stock,
            "modified_count" : result.modified_count
        }), 200
    
    except Exception as e:
        return jsonify({
            "status" : "error",
            "message" : f"terjadi kesalahan {str(e)}"
        }), 500            
    pass


@app.route('/api/data/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        # cek admin
        auth_check = check_admin()
        if auth_check:
            return auth_check
        
        # validasi input
        if not product_id or not product_id.strip():
            return jsonify({
                "status": "error",
                "message": "Product ID tidak boleh kosong"
            }), 400

        # hapus produk dari database
        try:
            result = db[MONGO_COLLECTION_PRODUCTS].delete_one({"_id": product_id})
        except PyMongoError as e:
            return jsonify({
                "status": "error",
                "message": f"Gagal menghapus produk dari database: {str(e)}"
            }), 500

        # cek produk
        if result.deleted_count == 0:
            return jsonify({
                "status": "error",
                "message": "Produk tidak ditemukan"
            }), 404

        # success notif
        return jsonify({
            "status": "success",
            "message": "Produk berhasil dihapus",
            "deleted_id": product_id,
            "deleted_count": result.deleted_count
        }), 200

    except Exception as e:
        # handle error
        return jsonify({
            "status": "error",
            "message": f"Terjadi kesalahan: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)


