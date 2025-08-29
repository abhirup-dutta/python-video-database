from flask import Flask
from flask_restful import Api
from src.common.Globals import EXTENSION_VIDEOS
from src.resources.Video import Video

app = Flask(__name__)
api = Api(app)


api.add_resource(Video, EXTENSION_VIDEOS)
api.add_resource(Video, EXTENSION_VIDEOS + "/<int:video_id>", endpoint="/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)