# 04. 웹 스크래핑

## python의 웹스크래핑 모듈을 활용해 알림 기능을 만들어보자

### 실습내용

좋아하는 아티스트의 공연을 예매하거나, 한정판 상품의 판매 개시를 기다리느라

웹페이지에서 무한정 F5를 누르며 새로고침 해본 경험이 있으신가요?

파이썬으로 우리 대신 주기적으로 확인해주는 프로그램을 만들어서 

자동으로 웹페이지를 읽고, 추가된 내용이 있을 경우 메일로 알림을 보내는 프로그램을 만들어 볼 수 있습니다.

python의 selenium 이라는 모듈은 웹브라우저 자동화 도구로서 

프로그래밍을통해 브라우저를 제어할 수 있습니다.

브라우저의 각 개발사에서 제공하는 드라이버를 다운받아 사용할 수 있습니다.

```
ex) chrome 브라우저
https://github.com/mozilla/geckodriver/releases
```

- 예시
```
from selenium import webdriver

# 위 사이트에서 각각의 OS환경에 맞춰 다운받은 드라이버 파일의 경로 입력
driver = webdriver.Chrome('lib/chromedriver.exe')

driver.get("https://www.naver.com")
```

추가로 파이썬의 BeautifulSoup 모듈은 selenium으로 받아온 웹브라우저의 데이터중에

원하는 정보를 손쉽게 가져오는데 도움을 줍니다


- 예시
```
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')
```

참고 URL : https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/

이러한 기술을 활용해서 

우리는 1년에 한번씩 열리는 파이썬 (덕후들의) 축제인 "파이콘"의 

튜토리얼 티켓 예매 모니터링 프로그램을 만들어 볼 것입니다.

https://www.pycon.kr/ticket/overview

위 사이트에 들어가 보시면 컨퍼런스 일반 티켓까지는 구매가 가능하지만, 

아직 튜토리얼은 구매가 불가능합니다.

주기적으로 1시간마다 웹페이지의 데이터를 불러와서 튜토리얼 티켓이 오픈된것이 확인되면

메일로 서로의 메일에 알람을 보내는 프로그램을 작성하시면 됩니다.



#### 1. 프로그램 동작 예

```
$ python web_monitor.py
```

이 프로그램의 핵심 기능 요소 입니다.

1) 주기적으로(1시간 마다) 백그라운드 프로세스로 실행

2) 웹브라우저 데이터 조회 후 원하는 부분의 정보 조회 및 확인

3) 2번 단계에서 취득한 데이터를 통한 이메일 전송 기능

일단 1번 부분은 고려하지 않도록 하겠습니다. 

작성한 프로그램을 수행하면 바로 웹브라우저의 데이터를 긁어와서 튜토리얼이 열렸는지 확인후에,

메일을 보내야하면 보내는 기능이 필요합니다

파이썬 메일보내기 기능은 구글에서 "파이썬 메일 알람"으로 검색해서 나오는 코드를 복사해서 사용하시면
됩니다

메일의 제목은 "[파이콘튜토리얼 티켓 오픈 알림] {본인 이름}-{현재시간}"
메일 내용은 https://www.pycon.kr/ticket/overview 웹 주소
메일 받는 사람은 leehaejoon@mobigen.com, cleanby@mobigen.com 두 메일을 포함하여 자기 자신의 메일 이렇게 3명한테 알림을 보내면 됩니다


<br/>

#### 2. 제출방식

완성된 파일은 현재 디렉토리 아래 각자 본인의 이름으로 만들어진 폴더에 넣어주시면 됩니다.

완성 후 시간이 남으면 주기적으로(1시간 마다) 백그라운드 프로세스로 실행하는 방법을 찾아보시면 좋을것
같습니다. 화이팅^_^
