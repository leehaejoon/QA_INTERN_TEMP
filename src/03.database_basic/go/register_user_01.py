import sqlite3
import datetime
import sys

def input_db(string):

    db_path = "user_info.db"
    USER_ID = string
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = "INSERT INTO REGISTER_DATE VALUES (?,?,?,?,?,?,?)"
    dt = datetime.datetime.now()

    #여기서 USER_NAME을 갖고와서, 지금의 USER_ID랑 비교하면 될 듯 하다?\
    cur.execute("SELECT * FROM REGISTER_DATE")
    results = cur.fetchall()
    Exist_ecept = 0

    if len(results) == 0:
        cur.execute(sql, (USER_ID, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))
        conn.commit()
        cur.execute("SELECT * FROM REGISTER_DATE")
        result = cur.fetchall()
        print(result[0])
    else :
        for result in results:
            if USER_ID == result[0]:
                print("USER_ID already exist")
                Exist_ecept= 1
        if Exist_ecept != 1:
            cur.execute(sql, (USER_ID, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))
            conn.commit()
            cur.execute("SELECT * FROM REGISTER_DATE")
            results = cur.fetchall()
            for result in results:
                print(result)

    conn.close()

if __name__ == '__main__':

    input_db(sys.argv[1])




