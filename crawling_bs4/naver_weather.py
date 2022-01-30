from pprint import pprint
from bs4 import BeautifulSoup as bs
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
#pprint(html.text)

soup = bs(html.text, 'html.parser')
# pprint(soup)

data1 = soup.find('div', {'class':'weather_graphic'}) # 영역 추출
# pprint(data1)

data2 = data1.findAll('div')
# pprint(data2[0])

find_dust = data2[0].find('span', {'class':'blind'}).text # text부분만 호출
print(find_dust)