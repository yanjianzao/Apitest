import requests
import logging
import pytest
import json
logging.basicConfig(level=logging.INFO)
class TestRequest(object):
    def test_get(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
        print(json.dumps(r.json(),indent=2))




