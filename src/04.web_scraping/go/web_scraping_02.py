import smtplib
import datetime
import threading
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from email.message import EmailMessage

class Task:
    def check_the_button(self):
        driver = webdriver.Chrome('chromedriver')
        driver.get('https://www.pycon.kr/ticket/overview')
        try:
            driver.find_element_by_xpath('//*[@id="__next"]/main/div/table/tbody/tr[4]/td[4]/a').click()
        except NoSuchElementException: 
            print("not yet")
            driver.close()
            threading.Timer(3600, self.check_the_button).start()

    def send_Email(self):
        smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_gmail.ehlo()
        smtp_gmail.starttls()
        smtp_gmail.login('아이디!', '비밀번호!')
        msg = EmailMessage()
        msg['Subject'] = "[파이콘튜토리얼 티켓 오픈 알림] {고승범}-{"+dt.strftime('%Y-%m-%d %H:%M')+"}"
        msg.set_content("https://www.pycon.kr/ticket/overview")
        msg['from'] = 'vkdkf55@gmail.com'
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
