#coding: utf-8
import requests
import logging
import pytest
import json
handleapp = {
    "Host":"gatewaytest.jinlingkeji.cn",
    "Connection": "keep-alive",
    "Content type":"application/x-www-form-urlencoded;charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-cn",
    "User-Agent":"%E7%BD%91%E4%B8%8A%E8%80%81%E5%B9%B4%E5%A4%A7%E5%AD%A6/2.8 CFNetwork/1128.0.1 Darwin/19.6.0",
    "app-version":"2.3.0",
    "source-type": "IOS",
    "Authorization":"eyJhbGciOiJIUzUxMiJ9.eyJ1aWQiOjM0OTE5OCwibG9naW5UaW1lIjoiMTYxNjEzODMwNDQzOSIsInBob25lIjoiMTUzNjE1NjA4ODgiLCJ0eXBlIjoiMCIsImV4cCI6MTYyMzkxNDMwNH0.f6vRDL5yYMQ6M7WepfjwqGEqejht1LYLhfDfv2ECQGrLuRWBL4jUYTNgDeSTSdCS6YzZXqFqxmMGiSP9RAj_Hg"
}
class TestRequest(object):
    url = "https://testerhome.com/api/v3/topics.json?limit=2"
    logging.basicConfig(level=logging.INFO)
    def test_get(self):
        r = requests.get(self.url,verify=False)
        # logging.info(json.dumps(r.json(),indent=2))
    def test_post(self):
        res2 = requests.post(url='https://gatewaytest.jinlingkeji.cn/v9/message/live/hot/list',
                             json={"pageSize": "8", "pageNum": "1", "type": "1"}, headers=handleapp)
        logging.info(json.dumps(res2.json(),indent=2))



