import sqlite3
import datetime
import sys

def input_db(string,db_path):
    sql = "INSERT INTO REGISTER_DATE VALUES (?,?,?,?,?,?,?)"
    dt = datetime.datetime.now()
    data = string, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    USER_ID = string
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
    cur.execute("SELECT * FROM REGISTER_DATE")
    results = cur.fetchall()
    conn.close()
    return results

if __name__ == '__main__':
    db_path = "user_info.db"
    if(len(sys.argv) == 2):
        input_db(sys.argv[1],db_path)
    elif(len(sys.argv) == 1):
        print("Doesn't exist USER_ID")
    else:
        print(sys.argv[2])
        print("invalid Command")
