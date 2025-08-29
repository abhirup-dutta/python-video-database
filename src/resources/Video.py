from functools import update_wrapper

from flask_restful import Resource, reqparse

videos = {}


class Video(Resource):
    def __init__(self):
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
        if video_id not in videos:
            get_failure_msg_object = {
                "message" : "Requested video not found in the store.",
                "id" : video_id
            }
            return get_failure_msg_object, 404
        else:
            return videos[video_id], 200


    def put(self, video_id):
        args = self.video_put_args.parse_args()
        if video_id not in videos:
            update_failure_msg_object = {
                "message": "Requested video not found in the store.",
                "id": video_id
            }
            return update_failure_msg_object, 404
        else:
            videos[video_id] = args
            update_success_msg_object = {
                "message": "Successfully updated video details.",
                "id": video_id,
                "data": args
            }
            return update_success_msg_object, 200


    def post(self):
        args = self.video_post_args.parse_args()
        video_id = args["id"]
        if video_id in videos:
            create_failure_msg_object = {
                "message" : "Resource with this id already exists. Use PUT to update the existing resource, or DELETE to remove it first.",
                "id" : video_id
            }
            return create_failure_msg_object, 400
        else:
            video_data = {
                "name" : args["name"],
                "views" : args["views"],
                "likes" : args["likes"]
            }
            videos[video_id] = video_data
            create_success_msg_object = {
                "message" : "Created new video details successfully.",
                "id" : video_id,
                "data" : videos[video_id]
            }
            return create_success_msg_object, 200


    def delete(self, video_id):
        if video_id not in videos:
            delete_nonexistent_msg_object = {
                "message": "Requested video to be deleted did not exist.",
                "id": video_id
            }
            # still a success, to take care of duplicate deletes due to network issues
            return delete_nonexistent_msg_object, 200
        else:
            videos.pop(video_id)
            delete_success_msg_object = {
                "message": "Deleted video details successfully.",
                "id": video_id
            }
            return delete_success_msg_object, 200






