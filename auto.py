from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys, os

#경고창
from selenium.webdriver.common.alert import Alert
import time

# 옵션 생성
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

options.add_argument('--window-size=1024,768')
options.add_argument('--disable-gpu')

#pyinstaller
if  getattr(sys, 'frozen', False): 
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path,options=options)
else:
    driver = webdriver.Chrome("./chromedriver",options=options)

# driver 실행
#driver = webdriver.Chrome("./chromedriver",options=options)


alert = Alert(driver)

#홈페이지 접속
driver.get('')#로그인 페이지 url
driver.implicitly_wait(5)

#아이디/비밀번호 입력
driver.find_element(By.NAME,'id').send_keys('')#id 넣기
driver.find_element(By.NAME,'passwd').send_keys('')#비밀번호넣기

#로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="loginform"]/a').click()
driver.implicitly_wait(5)

#출석체크로 이동
driver.get('')#출석체크 페이지 url
driver.implicitly_wait(5)

#alert 제어 필요해 보임
try:
    driver.find_element(By.XPATH,'/html/body/div[8]/div[2]/div[6]/div[2]/div[1]/div/a/span').click()
    alert.accept()
    print('출석체크 완료!')
except Exception:
    print('이미 출석체크 했습니다.')

# 오류 출석체크 이미 했을때 와 안했을때 경고문구 출력아됨
# 해결책1) 딜레이 2) 문구 제거 굳이 필요하나 싶음
driver.implicitly_wait(30)

driver.quit()

