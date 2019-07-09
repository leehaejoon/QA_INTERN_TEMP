from bs4 import BeautifulSoup
from selenium import webdriver
from six.moves import urllib

driver = webdriver.Chrome('C:\chromedriver.exe')

fp = driver.get('http://monaco.mobigen.com/pms/monaco/login/login.jsp')
''
driver.find_element_by_name('j_userid').send_keys('0330')
driver.find_element_by_name('j_password').send_keys('1')
driver.find_element_by_xpath('/html/body/form/div/div[2]/div/div[2]/div/button').click()
driver.switch_to.frame('frm_top')
driver.find_element_by_xpath('//*[@id="navigation"]/div/ul/li[1]/a').click() # Schedule 클릭
driver.switch_to.default_content()
driver.switch_to.frame('frm_left')
driver.find_element_by_xpath('//*[@id="SCH_001"]/a').click() # 일정관리 클릭
driver.implicitly_wait(50)
driver.find_element_by_xpath('//*[@id="childMenu2_SCH_04"]').click() # 일정목록 클릭
driver.implicitly_wait(50)
driver.switch_to.default_content()
driver.switch_to.frame('frm_work')
driver.implicitly_wait(50)
driver.find_element_by_xpath('//*[@id="stDate"]').click() # 기간 조회 설정, 7월 1일로
driver.implicitly_wait(50)
driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[2]/a').click()
driver.implicitly_wait(50)
driver.find_element_by_xpath('//*[@id="sc"]').click()
driver.implicitly_wait(50)


if __name__  == "__main__":
    soup = BeautifulSoup(driver.page_source, 'html.parser') # 페이지 내 모든 요소를 파싱
    result_date = soup.select('html table b') # 모든 날짜가 리스트로 나와야하는데 첫 날짜만 갖는, 크기가 1인 리스트로 파싱됨 -- 문제
    result_team = soup.findAll('td', attrs={"aria-describedby" : "dataGrid_deptNm"})[0] # 부서명 파싱
    result_name = soup.findAll('td', attrs={"aria-describedby" : "dataGrid_empNm"})[0] # 사원명 파싱
    result_time = soup.findAll('td', attrs={"aria-describedby" : "dataGrid_comment"}) # 모든 출근 시간이 리스트로 나와야하는데 첫 날 출근시간만 갖는, 크기가 1인 리스트로 파싱됨 -- 문제
    for i in result_date:
        print(i.text)
    print(result_team.text)
    print(result_name.text)
    for i in result_time:
        print(i.text)
