import json
import requests

# HTTP工具类
class HttpUtils:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, headers=None):
        return self.session.get(url, params=params, headers=headers)

    def post(self, url, data=None, json=None, headers=None):
        return self.session.post(url, data=data, json=json, headers=headers)

url = 'http://10.233.130.158:5000/get_query_embeddings'
headers = {'content-type': "application/json"}
body = {
    "query": [
        "车",
        "厘",
        "子",
        "的",
        "爱",
        "烧",
        "烤",
        "烤"
    ]
}

# response = requests.post(url, data=json.dumps(body), headers=headers)
# dic_info = json.loads(response.content)
#
# print(dic_info)