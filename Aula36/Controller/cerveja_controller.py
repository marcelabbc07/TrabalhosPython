from flask_restful import Resource

class CervejaController(Resource):
    def get(self):
        return 'Acessando controladora pelo método HTTP GET'
    
    def post(self):
        return 'Acessando controladora pelo método HTTP POST'

    def put(self):
        return 'Acessando controladora pelo método HTTP PUT'

    def delete(self):
        return 'Acessando controladora pelo método HTTP DELETE'