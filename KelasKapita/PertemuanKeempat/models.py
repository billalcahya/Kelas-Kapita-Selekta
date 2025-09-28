from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('number', required=True, type=int, help='Number must fill')

class HelloWorld(Resource):
    def get(self):
        return {'hello' : 'world'}
    
    def post(self):
        data = parser.parse_args()
        return {'hello' : 'world post', 'data' : 'data'}

