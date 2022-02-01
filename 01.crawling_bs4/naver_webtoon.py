from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

# 웹페이지 열고 소스코드 읽어오기
html = requests.get('http://comic.naver.com/webtoon/weekday.nhn')
soup = bs(html.text, 'html.parser') # 응답받은 html 내용을 bs4 클래스의 객체로 생성/반환함
html.close()

# 월요웹툰영역 추출
data1_list = soup.findAll('div', {'class':'col_inner'})
# pprint(len(data1_list))

# 전체 웹툰 리스트
week_title_list = []

for data1 in data1_list:
    # 제목 포함 영역 추출
    data2=data1.findAll('a', {'class':'title'})

    title_list = [t.text for t in data2]
    # pprint(title_list)
    week_title_list.append(title_list)

pprint(week_title_list[0])
#data2 = data1.findAll('a', {'class':'title'})
# # print(data2)
#
# title_list = [t.text for t in data2]
#
# pprint(title_list)