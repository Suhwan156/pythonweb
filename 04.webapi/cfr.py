import os
import sys
import requests
from pprint import pprint
import json
client_id = "id"
client_secret = "pw"

# url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

files = {'image': open('dami.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

response = requests.post(url,  files=files, headers=headers)
rescode = response.status_code

if(rescode == 200):
    data = json.loads(response.text)
    pprint(data)
    pprint(type(data))
    print(data['info']['size']['height'])
else:
    print("Error Code:" + rescode)