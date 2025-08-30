from flask import Flask
from flask_restful import Api

from src.common.Globals import EXTENSION_VIDEOS
from src.common.VideoDatabaseAccessInitiator import VideoDatabaseAccessInitiator
from src.resources.VideoRESTEndpoint import VideoRESTEndpoint

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
video_REST_endpoint_creator = VideoDatabaseAccessInitiator(app)
db_access = video_REST_endpoint_creator.getDbAccess()


api.add_resource(VideoRESTEndpoint,
                 EXTENSION_VIDEOS,
                 resource_class_kwargs={ 'db_access': db_access })
api.add_resource(VideoRESTEndpoint,
                 EXTENSION_VIDEOS + "/<int:video_id>",
                 endpoint="/<int:video_id>",
                 resource_class_kwargs={ 'db_access': db_access })


if __name__ == "__main__":
    app.run(debug=True)