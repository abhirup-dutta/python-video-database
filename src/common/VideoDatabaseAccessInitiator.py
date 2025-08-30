from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from src.data.VideoModelCreator import VideoModelCreator
from src.data.VideoDatabaseAccess import VideoDatabaseAccess

class VideoDatabaseAccessInitiator:
    def __init__(self, app):
        self.db = SQLAlchemy(app)

        video_model_creator = VideoModelCreator(self.db)
        self.VideoModelClass = video_model_creator.getVideoModelClass()

        self.db_access = VideoDatabaseAccess(self.VideoModelClass, self.db)


    def getDbAccess(self):
        return self.db_access



