from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


class VideoDatabaseAccess:
    def __init__(self, VideoModel, db):
        self.VideoModel = VideoModel
        self.db = db
        self.INVALID_ID = 0

    def isValid(self, result):
        print("IS VALID")
        print(result)
        return result is not None

    def convertResultProxytoSimpleObject(self, resultproxy):
        results_list = [dict(rowproxy) for rowproxy in resultproxy]
        if not results_list:
            return None
        else:
            result = results_list[0]
            return {
                "id" : result["video_model_id"],
                "name" : result["video_model_name"],
                "views" : result["video_model_views"],
                "likes" : result["video_model_likes"]
            }


    def create(self, video_data):
        new_video = self.VideoModel(id = video_data["id"],
                        name = video_data["name"],
                        views = video_data["views"],
                        likes = video_data["likes"]
                    )
        self.db.session.add(new_video)
        self.db.session.commit()


    def read(self, video_id):
        # result = self.db.session.query(self.VideoModel).filter_by(id=video_id)
        #query = self.db.select(self.VideoModel).filter_by(id=video_id)
        # result = self.VideoModel.query.filter_by(id=video_id)
        query = self.db.session.query(self.VideoModel).filter(self.VideoModel.id == video_id)
        resultproxy = self.db.session.execute(query)
        return self.convertResultProxytoSimpleObject(resultproxy)



    def update(self, video_id, video_data):
        query = self.db.session.query(self.VideoModel).filter(self.VideoModel.id == video_id)
        query.update(video_data)
        self.db.session.commit()


    def delete(self, video_id):
        data = self.VideoModel.query.get(video_id)
        self.db.session.delete(data)
        self.db.session.commit()