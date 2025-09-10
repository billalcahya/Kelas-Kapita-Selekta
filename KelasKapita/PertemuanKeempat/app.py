from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your-secrey-key'

# Data user sederhana (dalam praktik nyata gunakan database)

users = {
    'admin' : 'admin123',
    'user' : 'user123'
}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Jika sudah login, langsung ke dashboard
    if 'username' in session :
        return redirect (url_for('dashboard'))
    
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password :
            session['username'] = username # menyimpan session
            return redirect(url_for('dashboard'))
        else :
            flash('Username atau password salah')
        
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    return f'<h1>Selamat datang, {username}! </h1><a href="/logout">logout</a>'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
