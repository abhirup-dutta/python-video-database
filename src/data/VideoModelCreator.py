from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


class VideoModelCreator:
    def __init__(self, db):
        self.db = db

    def getVideoModelClass(self):
        db = self.db

        class VideoModel(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(100))
            views = db.Column(db.Integer)
            likes = db.Column(db.Integer)

            def __repr__(self):
                return f"Video(name = {VideoModel.name}, views = {VideoModel.views}, likes = {VideoModel.likes})"

        db.create_all()

        return VideoModel