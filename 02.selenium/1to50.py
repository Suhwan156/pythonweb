from selenium import webdriver

driver = webdriver.Chrome('./driver/chromedriver')
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

#전역변수
#현재 찾아야될 숫자
num = 1

def clickBtn():
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

    for btn in btns:
        if btn.text == str(num):
            btn.click()
            num += 1
            return

while num<=50:
    clickBtn()