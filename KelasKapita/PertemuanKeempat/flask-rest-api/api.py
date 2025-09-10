from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"messages": "Hello world from GET"}
    
    def post(self):
        data = request.form
        return {"you_sent" : data}, 200
    
class TrainingPython(Resource):
    def get(self):
        return {"course" : "Python REST API"}
    
    def post(self):
        data = request.get_json() or request.form
        return {"training" : data}, 200
    
class Messages(Resource):
    def get(self, name):
        return {"messages" : f"hello{name}, this is parameter end point"}
    
api.add_resource(HelloWorld, '/HelloWorld')
api.add_resource(TrainingPython, '/TrainingPython')
api.add_resource(Messages, '/Messages/<string:namSe>')

if __name__ == '__main__':
    app.run(debug=True, port=5001)