from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import jwt
from datetime import datetime, timedelta
from functools import wraps

# Inisialisasi Aplikasi
app = Flask(__name__)
api = Api(app)
CORS(app)  # Mengizinkan Cross-Origin Resource Sharing

# Kunci rahasia untuk enkripsi JWT
app.config['SECRET_KEY'] = 'kunci-rahasia-super-aman-milikmu'

# Database pengguna sederhana (sekarang bisa diubah)
users = {
    'admin': 'password123',
    'user': 'user123'
}

# ----------------- DECORATOR UNTUK PROTEKSI ROUTE (SUDAH DIPERBAIKI) -----------------
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            token = auth_header.split(" ")[1]

        if not token:
            return {'message': 'Token tidak ditemukan!'}, 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            return {'message': 'Token sudah kedaluwarsa!'}, 401
        except jwt.InvalidTokenError:
            return {'message': 'Token tidak valid!'}, 401
        
        return f(*args, current_user, **kwargs)

    return decorated

# ----------------- RESOURCE UNTUK LOGIN -----------------
class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username tidak boleh kosong')
        parser.add_argument('password', type=str, required=True, help='Password tidak boleh kosong')
        data = parser.parse_args()

        username = data['username']
        password = data['password']

        if username in users and users[username] == password:
            token = jwt.encode({
                'username': username,
                'exp': datetime.utcnow() + timedelta(minutes=30)
            }, app.config['SECRET_KEY'], algorithm="HS256")
            return jsonify({'token': token})
        
        return {'message': 'Username atau password salah'}, 401

# ----------------- RESOURCE YANG DIPROTEKSI -----------------
class Dashboard(Resource):
    @token_required
    def get(self, current_user):
        return jsonify({'message': f'Selamat datang di dashboard, {current_user}!'})

# --- BARU: RESOURCE UNTUK MANAJEMEN PENGGUNA (CREATE & READ ALL) ---
class UserManagement(Resource):
    @token_required
    def get(self, current_user):
        # Mengembalikan daftar username (tanpa password demi keamanan)
        return jsonify(list(users.keys()))

    @token_required
    def post(self, current_user):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username diperlukan')
        parser.add_argument('password', type=str, required=True, help='Password diperlukan')
        data = parser.parse_args()

        if data['username'] in users:
            return {'message': 'Pengguna sudah ada'}, 400

        users[data['username']] = data['password']
        return {'message': 'Pengguna berhasil dibuat'}, 201

# --- BARU: RESOURCE UNTUK PENGGUNA SPESIFIK (UPDATE & DELETE) ---
class UserResource(Resource):
    @token_required
    def put(self, current_user, username):
        parser = reqparse.RequestParser()
        parser.add_argument('password', type=str, required=True, help='Password baru diperlukan')
        data = parser.parse_args()

        if username not in users:
            return {'message': 'Pengguna tidak ditemukan'}, 404

        users[username] = data['password']
        return {'message': 'Password pengguna berhasil diperbarui'}, 200

    @token_required
    def delete(self, current_user, username):
        if username not in users:
            return {'message': 'Pengguna tidak ditemukan'}, 404
        
        if username == current_user:
            return {'message': 'Anda tidak dapat menghapus diri sendiri'}, 400

        del users[username]
        return {'message': 'Pengguna berhasil dihapus'}, 200

# Menambahkan Resource ke API
api.add_resource(Login, '/login')
api.add_resource(Dashboard, '/dashboard')
# --- BARU: Menambahkan endpoint CRUD ---
api.add_resource(UserManagement, '/users')
api.add_resource(UserResource, '/users/<string:username>')

if __name__ == '__main__':
    app.run(debug=True, port=5000)