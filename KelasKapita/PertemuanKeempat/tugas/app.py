from flask import Flask, flash, render_template, request,url_for,redirect, session

app = Flask(__name__)
app.secret_key = 'secretke123'

users = {
    'admin' : 'admin',
    'user' : 'user'
}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('username atau password salah')
            
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session :
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Anda telah logout')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)