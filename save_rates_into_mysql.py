import mysql.connector
from mysql.connector import Error


def save_rates(dict_rates):
    try:
        conn = mysql.connector.connect(user='root',
                                       host='localhost',
                                       database='mysql')

        if conn.is_connected():
            clear_table = "DELETE FROM exchange_test"
            cursor = conn.cursor()
            cursor.execute(clear_table)

            new_rates = "INSERT INTO exchange_test" \
                        "(key_forex, value_forex) VALUES(%s,%s)"
            cursor = conn.cursor()
            for k, v in dict_rates.items():
                cursor.execute(new_rates, (k, v))
            if cursor.lastrowid:
                print('успешно добавлена запись. id пользователя: ',
                      cursor.lastrowid)
            else:
                print('какая-то ошибка...')

            conn.commit()
    except Error as error:
        print(error)
    finally:
        conn.close()
        cursor.close()
