import requests
import logging
import pytest
import json
logging.basicConfig(level=logging.INFO)
class TestRequest(object):
    url = "https://testerhome.com/api/v3/topics.json?limit=2"
    def test_get(self):
        r = requests.get(self.url,verify=False)
        print(json.dumps(r.json(),indent=2))
    def test_post(self):
        r = requests.post(url=self.url,data={"a":"1","b":"2"},proxies={"https":"http://127.0.0.1:8888","http":"http://127.0.0.1:8888"},verify=False)
        print(r.url)
        print(r.text)




