import logging
import requests
import json
logging.basicConfig(level=logging.INFO)
r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2")
logging.info(json.dumps(r.json(),indent=2))