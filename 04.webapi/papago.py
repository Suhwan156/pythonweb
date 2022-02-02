import os
import sys
import urllib.request
from pprint import pprint
import json

client_id = "id"
client_secret = "pw"

encText = urllib.parse.quote("반갑습니다")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if(rescode == 200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
    res = json.loads(response_body)
    pprint(res)

else:
    print("Error Code:" + rescode)