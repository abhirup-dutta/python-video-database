from flask import Flask
from flask_restful import Api
from src.resources.HelloWorld import HelloWorld
from src.common.Globals import HELLO_WORLD

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, HELLO_WORLD)

if __name__ == "__main__":
    app.run(debug=True)