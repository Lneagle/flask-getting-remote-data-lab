import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        return requests.get(self.url).content

    def load_json(self):
        return requests.get(self.url).json()
    
if __name__ == '__main__':
    URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

    print(GetRequester(URL).get_response_body())
    print(GetRequester(URL).load_json())