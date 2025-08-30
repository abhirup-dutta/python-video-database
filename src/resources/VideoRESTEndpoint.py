from flask_restful import Resource, reqparse

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy



class VideoRESTEndpoint(Resource):
    def __init__(self, **kwargs):
        self.db_access = kwargs['db_access']

        self.video_put_args = reqparse.RequestParser()
        self.video_put_args.add_argument("name", type=str, help="Name of the video")
        self.video_put_args.add_argument("views", type=int, help="Number of views of the video")
        self.video_put_args.add_argument("likes", type=int, help="Number of likes on the video")

        self.video_post_args = reqparse.RequestParser()
        self.video_post_args.add_argument("id", type=int, help="Unique ID of the video")
        self.video_post_args.add_argument("name", type=str, help="Name of the video")
        self.video_post_args.add_argument("views", type=int, help="Number of views of the video")
        self.video_post_args.add_argument("likes", type=int, help="Number of likes on the video")


    def get(self, video_id):
        print("REST GET BEGIN")
        video_result = self.db_access.read(video_id)
        print("REST Get: " + str(video_result))
        if not self.db_access.isValid(video_result):
            get_failure_msg_object = {
                "message" : "Requested video not found in the store.",
                "id" : video_id
            }
            print("REST GET END")
            return get_failure_msg_object, 404
        else:
            print("REST GET END")
            return video_result, 200


    def put(self, video_id):
        print("REST PUT BEGIN")
        args = self.video_put_args.parse_args()
        video_result = self.db_access.read(video_id)
        if not self.db_access.isValid(video_result):
            update_failure_msg_object = {
                "message": "Requested video not found in the store.",
                "id": video_id
            }
            print("REST PUT END")
            return update_failure_msg_object, 404
        else:
            self.db_access.update(video_id, args)
            video_result = self.db_access.read(video_id)
            update_success_msg_object = {
                "message": "Successfully updated video details.",
                "id": video_id,
                "data": video_result
            }
            print("REST PUT END")
            return update_success_msg_object, 200


    def post(self):
        print("REST POST BEGIN")
        args = self.video_post_args.parse_args()
        video_id = args["id"]
        video_result = self.db_access.read(video_id)
        if self.db_access.isValid(video_result):
            create_failure_msg_object = {
                "message" : "Resource with this id already exists. Use PUT to update the existing resource, or DELETE to remove it first.",
                "id" : video_id
            }
            print("REST POST END")
            return create_failure_msg_object, 400
        else:
            self.db_access.create(args)
            video_result = self.db_access.read(video_id)
            create_success_msg_object = {
                "message" : "Created new video details successfully.",
                "id" : video_id,
                "data" : str(video_result)
            }
            print("REST POST END")
            return create_success_msg_object, 200


    def delete(self, video_id):
        print("REST DELETE BEGINNING")
        video_result = self.db_access.read(video_id)
        if not self.db_access.isValid(video_result):
            delete_nonexistent_msg_object = {
                "message": "Requested video to be deleted did not exist.",
                "id": video_id
            }
            print("REST DELETE END")
            # still a success, to take care of duplicate deletes due to network issues
            return delete_nonexistent_msg_object, 200
        else:
            self.db_access.delete(video_id)
            delete_success_msg_object = {
                "message": "Deleted video details successfully.",
                "id": video_id
            }
            print("REST DELETE END")
            return delete_success_msg_object, 200






