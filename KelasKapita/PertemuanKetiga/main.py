from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/hw', methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        return 'Hello, World! (POST)'
    else :
        return 'hello world!'

@app.route("/", methods=['GET', 'POST'] )
def index():
    if request.method == 'POST':
        nama = request.form['nama']
        usia = request.form['usia']
        return render_template('result.html', nama = nama, usia = usia)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True)