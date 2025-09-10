from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    val_param = "Test data yang dikirimkan melalui jinja"
    return render_template('index.html', key_param = val_param) 

if __name__ == '__main__':
    app.run(debug=True)
