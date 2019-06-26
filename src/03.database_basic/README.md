# 03. 데이터베이스 기본

## python의 다양한 모듈을 활용해 테이블에 정보를 입력해보자

### 실습내용

`https://github.com/leehaejoon/QA_INTERN_TEMP/tree/master/data/` 경로에 가보면,

`user_info.db` 라는 이름의 파일이 있습니다.

이는 sqlite db 파일로, `REGISTER_DATE` 라는 테이블이 생성되어있습니다.

테이블의 스키마는 다음과 같습니다.

```
REGISTER_DATE (
    USER_ID      TEXT,
    REG_YEAR     TEXT,
    REG_MONTH    TEXT,
    REG_DAY      TEXT,
    REG_HOUR     TEXT,
    REG_MIN      TEXT,
    REG_SEC      TEXT
)
```

`USER_ID` 컬럼은 중복되지 않는 사용자 고유 아이디입니다.

`REG_YEAR`부터 `REG_SEC` 까지는 각각 사용자가 DB에 등록된 연/월/일/시/분/초 를 의미합니다.

<br/>

프로그램 실행시 인자로 `USER_ID` 를 넘겨주면,

현재 시간을 기준으로 테이블에 값을 저장해주는 `register_user.py` 라는 프로그램을 만들어보세요.

db 파일(`user_info.db`)은 프로그램의 실행 경로와 같은 경로에 위치시켜 작업해주세요.

<br/>

#### 1. 프로그램 동작 예

```
$ python register_user.py haejoon
```

위와 같이 'haejoon' 이라는 인자를 주어 프로그램을 실행하면,

현재 시간인 2019, 07, 03, 14, 27, 30 이라는 숫자가 테이블의 각 컬럼에 들어가야합니다.

현재 시간이 2019년 7월 3일 오후 2시 27분 30초라고 가정한 것이고,

완성된 프로그램에서는 프로그램을 동작시키는 시점의 실제 시간이 들어가야합니다.

<br/>

데이터가 들어간 이후 테이블 상태는 다음과 같이 되겠죠.

```
USER_ID     REG_YEAR    REG_MONTH   REG_DAY     REG_HOUR    REG_MIN     REG_SEC
----------  ----------  ----------  ----------  ----------  ----------  ----------
haejoon     2019        07          03          14          28          30
```

또한, USER\_ID는 고유값이기때문에 이미 들어있는 값이 중복으로 들어가면 안됩니다.

<br/>

#### 2. sqlite3 모듈 활용 예

작업시간의 단축을 위해 파이썬에서 sqlite db를 사용하는 간단한 예제를 첨부하겠습니다.

`user_info.db`의 `REGISTER_DATE` 테이블에 저장된 모든 값을 조회하는 예제입니다.

```python
import sqlite3

db_path = "user_info.db"

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT * FROM REGISTER_DATE;")

results = cur.fetchall()
for result in results:
    print(result)

conn.close()
```

<br/>

#### 3. 제출방식

완성된 파일은 기존과 똑같이 현재 디렉토리 아래 각자 본인의 이름으로 만들어진 폴더에 넣어주시면 됩니다.

코드를 받아 바로 테스트 할 수 있게 작업하신 `user_info.db` 파일도 같이 넣어주세요.

<br/>

#### 4. 기타

혹시 위 프로그램 작성 후에 시간이 남는다면

등록된 유저의 생성시간을 출력해주는 "check\_register\_time.py" 라는 프로그램도 한 번 만들어보세요.

위 예제를 기준으로 다음과 같이 작동하면 됩니다.

```
$ python check_register_time.py haejoon
유저 haejoon 의 생성 시간은 2019년 07월 03일 오후 2시 28분 입니다.
```

화이팅!
