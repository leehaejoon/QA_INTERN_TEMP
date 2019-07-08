import smtplib
import datetime
import threading
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from email.message import EmailMessage


'''
1. 버튼이 떴는지 안떳는지 check
    1.1 버튼 유무 확인 완료
        1.1 try에서 처리가 되면 떳다는 경우
        1.2 exception으로 전달 되었을 경우 이것은 아직 안떳다는 것
    1.2 버튼 유무에 따른 정보 전달
        1.2.1 있을 경우 go 2
        1.2.2 없을 경우 아직 안떳다는 메세지 출력(이메일 XX)
2. check 유무에 따라 email 발송
'''
count = 0
class Task:
    def check_the_button(self):
        driver = webdriver.Chrome('chromedriver')
        driver.get('https://www.pycon.kr/ticket/overview')
        try:
            driver.find_element_by_xpath('//*[@id="__next"]/main/div/table/tbody/tr[4]/td[4]/a').click()
            # tr[2,3,4] 의 순서 = 개인후원, 일반 ,튜토리얼 이 순서
        except NoSuchElementException: # 안된 경우
            print("not yet")
            driver.close()
            threading.Timer(3600, self.check_the_button).start()

    def send_Email(self):
        smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_gmail.ehlo()
        smtp_gmail.starttls()
        smtp_gmail.login('아이디!', '비밀번호!') # 중간 삭제!!
        msg = EmailMessage()
        msg['Subject'] = "[파이콘튜토리얼 티켓 오픈 알림] {고승범}-{"+dt.strftime('%Y-%m-%d %H:%M')+"}"
        # 제목
        msg.set_content("https://www.pycon.kr/ticket/overview")
        # 내용
        msg['from'] = 'vkdkf55@gmail.com'
        #msg['to'] = 'vkdkf55@gmail.com'
        msg['to'] = 'vkdkf55@gmail.com', 'cleanby@mobigen.com', 'leehaejoon@mobigen.com'
        smtp_gmail.send_message(msg)

def main():
    Start_Task = Task()
    Start_Task.check_the_button()
    Start_Task.send_Email()

if __name__ == "__main__":
    dt = datetime.datetime.now()
    td = dt + datetime.timedelta(minutes= 60)
    print("check "+dt.strftime('%Y-%m-%d %H:%M'))
    print("next check : "+ td.strftime('%Y-%m-%d %H:%M'))
    main()
