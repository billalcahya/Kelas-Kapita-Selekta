from flask import Flask, render_template, request, redirect, url_for, flash, make_response

app = Flask(__name__)
app.secret_key = 'your-secret-key'

users = {
    'admin': 'password123',
    'user': 'user123'
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    username_cookie = request.cookies.get('username')
    if username_cookie:
        # Jika sudah ada cookie, langsung ke dashboard
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            resp = make_response(redirect(url_for('dashboard')))
            resp.set_cookie('username', username, max_age=60*5)  # cookie 5 menit
            return resp
        else:
            flash('Username atau password salah')

    # Render login untuk GET atau POST gagal
    return render_template('login2.html')

@app.route('/dashboard')
def dashboard():
    username_cookie = request.cookies.get('username')
    if not username_cookie:
        return redirect(url_for('login'))
    
    return f'<h1>Selamat datang, {username_cookie}</h1><a href="/logout">Logout</a>'

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('login')))
    resp.delete_cookie('username')  # Hapus cookie
    return resp

if __name__ == '__main__':
    app.run(debug=True)
