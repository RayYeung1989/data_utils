import json
import requests

# HTTP工具类
class HttpUtils:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, headers=None):
        return self.session.get(url, params=params, headers=headers)

    def post(self, url, data=None, headers=None):
        return self.session.post(url, data=data, headers=headers)

# url = 'http://XXXXXXXXXXXXXXXXXX//'
# headers = {'content-type': "application/json"}
# body = {
#     "query": [
#         "车",
#         "厘",
#         "子",
#         "的",
#         "爱",
#         "烧",
#         "烤",
#         "烤"
#     ]
# }

# response = requests.post(url, data=json.dumps(body), headers=headers)
# dic_info = json.loads(response.content)
#
# import pandas as pd
# queryEmbeddingDict = {}
# for i in range(len(dic_info)):
#     queryEmbeddingDict.update({dic_info[i]['query']:dic_info[i]['embedding']})
# queryEmbeddingDf = pd.DataFrame(queryEmbeddingDict).T
# queryEmbeddingDf