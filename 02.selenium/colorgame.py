from selenium import webdriver
from pprint import pprint
import time
from collections import Counter

driver = webdriver.Chrome('./driver/chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(300)

# //*[@id="grid"]/div[1]
btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')
#print(len(btns))

def analysis():
    btns_rgba = [ btn.value_of_css_property('background-color') for btn in btns]
    #pprint(btns_rgba)

    result = Counter(btns_rgba)
    pprint(result) #여기서 value가 1인게 정답

    #value가 1인 것 탐색
    for key, value in result.items():
        if value == 1:
            answer = key
            break
    else:
        answer = None
        print("정답을 찾을 수 없습니다.")

    if answer:
        index = btns_rgba.index(answer)
        btns[index].click()

start = time.time()
while time.time() - start <= 60:
    analysis()