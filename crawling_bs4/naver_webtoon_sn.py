from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

# 웹페이지 열고 소스코드 읽기
html = requests.get('http://comic.naver.com/webtoon/weekday.nhn')
soup = bs(html.text, 'html.parser') # 응답받은 html 내용을 bs4 클래스의 객체로 생성/반환함
html.close()

# 요일별 웹툰영역 추출
data1_list = soup.findAll('div', {'class':'col_inner'})

# 전체 웹툰 리스트
li_list = []
for data1 in data1_list:
    li_list.extend(data1.findAll('li'))

# pprint(li_list)

# # 썸네일, 제목 추출
for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    print(title, img_src)