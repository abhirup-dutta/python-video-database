from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {
            "request_type" : "GET",
            "data" : "Hello World !!!"
        }

    def post(self):
        return {
            "request_type" : "POST",
            "data" : "posted"
        }