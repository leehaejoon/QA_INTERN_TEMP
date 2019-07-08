import smtplib
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from email.message import EmailMessage
import datetime

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

def check_the_button():
    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(3)
    driver.get('https://www.pycon.kr/ticket/overview')
    check_num = 0
    try:
        driver.find_element_by_xpath('//*[@id="__next"]/main/div/table/tbody/tr[3]/td[4]/a').click()
        # tr[2,3,4] 의 순서 = 개인후원, 일반 ,튜토리얼 이 순서
    except NoSuchElementException:
        check_num = 1
    return check_num


def send_Email(check_num):
    if check_num == 0:# 이거 처리할 방법 찾아보기
        smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_gmail.ehlo()
        smtp_gmail.starttls()
        smtp_gmail.login('개인메일주소', '개인비밀번호') # 중간 삭제!!
        msg = EmailMessage()
        dt = datetime.datetime.now()
        msg['Subject'] = "[파이콘튜토리얼 티켓 오픈 알림] {고승범}-{"+dt.strftime('%Y-%m-%d %H:%M')+"}"
        # 제목
        msg.set_content("https://www.pycon.kr/ticket/overview")
        # 내용
        msg['from'] = 'vkdkf55@gmail.com'
        #msg['to'] = 'vkdkf55@gmail.com', 'vkdkf55@naver.com'
        msg['to'] = 'vkdkf55@gmail.com', 'cleanby@mobigen.com', 'leehaejoon@mobigen.com'
        smtp_gmail.send_message(msg)

def not_yet(check_num):  # 1.2.1
    if check_num == 1:
        print("not yet") #굳이 넣을 필요는 없을듯 한데.

if __name__ == "__main__":
    check_num = check_the_button()
    send_Email(check_num)
    not_yet(check_num)