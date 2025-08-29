import requests

from src.common.Globals import BASE, HELLO_WORLD

class HelloWorldTest:

    def __init__(self):
        self.base = BASE
        self.extension = HELLO_WORLD

    def testGet(self):
        response = requests.get(self.base + self.extension)
        print(response.json())

    def testPost(self):
        response = requests.post(self.base + self.extension)
        print(response.json())