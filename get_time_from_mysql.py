import mysql.connector
from mysql.connector import Error


def get_time_db():
    last_time = 0
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM exchange_test")
            row = cursor.fetchone()
            while row is not None:
                last_time = row[3]
                row = cursor.fetchone()
            conn.commit()
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
    return last_time
