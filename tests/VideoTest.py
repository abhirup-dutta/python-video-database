import requests
from urllib.error import HTTPError

from src.common.Globals import BASE_URL, EXTENSION_VIDEOS

class VideoTest:

    def __init__(self):
        self.base = BASE_URL
        self.extension = EXTENSION_VIDEOS
        self.video_id = 3434

    def testGet(self):
        response = requests.get(self.base + self.extension + "/" + str(self.video_id))
        print(response.json())

    def testPut(self):
        update_video_id = self.video_id
        update_video_data = {
            "name" : "Focus music for working",
            "views" : 11034,
            "likes" : 9034
        }
        response = requests.put(self.base + self.extension + "/" + str(update_video_id),
                                 update_video_data)
        print(response.json())

    def testPost(self):
        create_video_param = {
            "id" : self.video_id,
            "name": "Focus music for working",
            "views": 10034,
            "likes": 8034
        }
        response = requests.post(self.base + self.extension,
                                 create_video_param)
        print(response.json())

    def testDelete(self):
        response = requests.delete(self.base + self.extension + "/" + str(self.video_id))
        print(response.json())
