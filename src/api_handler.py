import requests

class APIHandler:
    def __init__(self, url):
        self.url = url
    
    def get(self, endpoint):
        return requests.get(self.url + endpoint)
    