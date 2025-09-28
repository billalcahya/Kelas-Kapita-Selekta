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
        return jsonify({"error", "Butuh akses admin"}), 403
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

            flash("success", "Login berhasil")
            return redirect(url_for("index"))
        else:
            flash("Username atau password salah", "error")
            return redirect(url_for("login"))
    return render_template("login.html")
    pass


@app.route("/logout")
def logout():
    session.clear()
    flash("success", "Berhasil logout")
    return redirect(url_for("login"))
    pass


@app.route('/')
def index():
    auth_check = check_admin()
    if auth_check:
        return auth_check
    return render_template("index.html")
    pass


if __name__ == "__main__":
    app.run(debug=True)


