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
    data = USER_ID, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    Exist_ecept = 0
    cur.execute("SELECT * FROM REGISTER_DATE")
    results = cur.fetchall()

    if len(results) == 0:
        cur.execute(sql, data)
        conn.commit()
    elif(len(results[0]) != 7) :
        print("It's different DB_file.")
    else :
        for result in results:
            if USER_ID == result[0]:
                print("USER_ID already exist")
                Exist_ecept= 1
        if Exist_ecept != 1:
            cur.execute(sql, data)
            conn.commit()
    conn.close()

if __name__ == '__main__':
    try:
        if(len(sys.argv) == 2):
            input_db(sys.argv[1])
        else:#강제 Error 발생
            input_db(sys.argv)
    except:
        if (len(sys.argv) == 1):
            print("Doesn't exist USER_ID")
        else:
            print("invalid Command")