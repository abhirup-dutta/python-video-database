import requests

from src.common.Globals import BASE_URL, EXTENSION_HELLO_WORLD

class HelloWorldTest:

    def __init__(self):
        self.base = BASE_URL
        self.extension = EXTENSION_HELLO_WORLD

    def testGet(self):
        response = requests.get(self.base + self.extension)
        print(response.json())

    def testPost(self):
        response = requests.post(self.base + self.extension)
        print(response.json())