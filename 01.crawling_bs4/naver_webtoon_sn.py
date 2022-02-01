import errno

from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests, re, os
from urllib.request import urlretrieve

try:
    if not (os.path.isdir('image')):    # isdir(path), 존재하는 디렉터리면 True 반환
        os.makedirs(os.path.join('image'))    # dir 생성,
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패")
        exit()

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
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)    # 해당 영역 글자 아니면 ''로 치환
    print(title, img_src)
    urlretrieve(img_src, './image/'+title+'jpg')    # 주소, 파일경로+파일명+확장자
