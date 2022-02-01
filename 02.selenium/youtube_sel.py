from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.get("https://www.youtube.com/")

time.sleep(10)

#검색어 창을 찾아 search 변수에l 저장
# 기존 xpath 는 //*[@id="search"] 였는데 동작 X
search = driver.find_element_by_name("search_query")
# search = driver.find_element_by_xpath('//input[@id="search"]')

#search 변수에 저장된 곳에 값을 전송
search.send_keys('반원 코딩')
time.sleep(1)

#search 변수에 저장된 곳에 엔터를 입력
search.send_keys(Keys.ENTER)
"""
Keys.ARROW_DOWN , Keys.ARROW_LEFT , Keys.ARROW_RIGHT
Keys.ARROW_UP , Keys.BACK_SPACE , Keys.CONTROL
Keys.ALT , Keys.DELETE , Keys.ENTER , Keys.SHIFT
Keys.SPACE , Keys.TAB , Keys.EQUALS , Keys.ESCAPE
Keys.HOME , Keys.INSERT , PgUp Key  Keys.PAGE_UP
Keys.PAGE_DOWN , Keys.F1 , Keys.F2 , Keys.F3 , Keys.F4
Keys.F5 , Keys.F6 , Keys.F7 , Keys.F8 , Keys.F9 , Keys.F10
Keys.F11 , Keys.F12
"""