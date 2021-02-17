import mysql.connector
from mysql.connector import Error


def get_rates_db():
    rates = {}
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM exchange_test")
            row = cursor.fetchone()
            while row is not None:
                rates[row[1]] = row[2]
                row = cursor.fetchone()
            conn.commit()
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
    return rates
