import smtplib
import time
import sqlite3
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

path = 'https://www.google.com/'
driver = webdriver.Chrome('chromedriver')

class monaco:
    def monaco_find_page_source(self):
        driver.get('http://monaco.mobigen.com/pms/')
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('/html/body/form/div/div[2]/div/div[2]/div/div[1]/input').send_keys('vkdkf')
        driver.find_element_by_xpath('/html/body/form/div/div[2]/div/div[2]/div/div[2]/input').send_keys('1\n')
        driver.implicitly_wait(3)
        driver.switch_to.frame('frm_top')
        driver.find_element_by_xpath('//*[@id="navigation"]/div/ul/li[5]/a/span').click()  # information
        driver.implicitly_wait(3)
        driver.switch_to.default_content()
        driver.switch_to.frame('frm_left')
        driver.find_element_by_xpath('//*[@id="BASE_003"]/a/span[1]').click() # 기초자료관리
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('//*[@id="childMenu2_BASE_14"]/span').click()  # 사원관리
        driver.implicitly_wait(3)
        driver.switch_to.default_content()
        driver.switch_to.frame('frm_work')
        time.sleep(1)
        return driver.page_source

    def monaco_Transformation(self,page_source): # 확실히 알겠는 걸로 명시할것
        soup = BeautifulSoup(page_source, 'html.parser')
        tr_elements = soup.find(attrs={"class": "ui-widget-content jqgrow ui-row-ltr"})
        range_elements = len(soup.find_all(attrs={"class": "ui-widget-content jqgrow ui-row-ltr"}))
        list = []
        for num in range(range_elements):
            titles = []  # 이거를 직원 정보로 refac할것
            for tr_element in tr_elements:
                titles.append(tr_element.get('title'))
            list.append(titles)
            del titles
            tr_elements = tr_elements.next_sibling
        driver.close()
        return list

    def monaco_save(self, list):
        db_path = "emp_info.db"
        sql = "INSERT INTO empinfo VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        for num in range(len(list)):
            data = ()
            data += tuple(list[num])
            cur.execute(sql, data)
            conn.commit()
            del data

    # db파일 생성 체크용
    def monaco_mkDB(self):
        db_file = "emp_info.db" #제대로 명시
        if os.path.isfile(db_file) == False:  # 파일이 이미 존재하는 경우를 위한 예외처리
            conn = sqlite3.connect(db_file)
            cur = conn.cursor()
            cur.execute('''CREATE table empinfo(depNm,position,rank,emp_cd,empNm,phone,inner_phone,email,entDate,space,empTypeNm,workType,empCd,loginTy,workspace,monaco)''')
            conn.close()
            return 1
        else:
            print("alreay exist")

    # check for a DBfile
    def check_db(self):
        db_path = 'emp_info.db'
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM empinfo")
        len_list = len(cur.fetchall())
        cur.execute("SELECT * FROM empinfo")
        for num in range(len_list): # 여기에 174는 횟원의 정보수 즉 len(list)
            print(cur.fetchone())

if __name__ == "__main__":
    monaco_login = monaco()
    string = monaco_login.monaco_find_page_source()
    list = monaco_login.monaco_Transformation(string)
    check_num = monaco_login.monaco_mkDB()
    if check_num == 1:
        monaco_login.monaco_save(list)
    # monaco_login.check_db()
