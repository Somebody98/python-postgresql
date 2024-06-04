import psycopg2, random
from psycopg2 import Error
import hashlib


# Ошибка при работе с PostgreSQL 'utf-8' codec can't decode byte 0xc2 in position 61: invalid continuation byte
# Если такая ошибка значит не может подключиться к бд, возможно не правильный пароль, пароль должен быть 123
# И в конце название базы данных, если ее нету, то нужно создать.
# conn = psycopg2.connect('postgresql://postgres:123@localhost:5432/demo')

# 1.4 задача==============================================================================================================================
# создать базу данных BD и таблицу Users, для хранения
# пользователей и их паролей;

def zadch14():
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect('postgresql://postgres:123@localhost:5432/demo')
        conn.autocommit = True
        # conn.execution_options(isolation_level="AUTOCOMMIT").execute(query)
        print('успешно')
        # Создайте курсор для выполнения операций с базой данных
        cursor = conn.cursor()

        create_database_query1 = '''
        CREATE DATABASE bd ;
        '''
        cursor.execute(create_database_query1)

        conn2 = psycopg2.connect('postgresql://postgres:123@localhost:5432/bd')
        conn2.autocommit = True
        cursor2 = conn2.cursor()

        creates_table_query = '''CREATE TABLE Users
                              (ID SERIAL PRIMARY KEY,
                              name           TEXT    NOT NULL,
                              password         TEXT NOT NULL); '''

        cursor2.execute(creates_table_query)

        for i in range(1, 11):
            imya = 'user' + str(i)
            print(i)
            teststr = '123456789101112131415161718192021222324252627282930QWERTYUIOPASDFGHJZXCVBNMQWERTYUIOPASDFGHJZXCVBNMQWERTYUIOPASDFGHJZXCVBNM'
            psw = ''.join([random.choice(teststr) for x in range(5)])
            passwd = psw
            creates_table_query4 = f'''
                INSERT INTO Users VALUES ({i},'{imya}', '{passwd}')
            '''
            cursor2.execute(creates_table_query4)
            print('данные успешно заполнены')

        print("Действие выполнено в PostgreSQL")
        cursor.close()
        conn.close()
        cursor2.close()
        conn2.close()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print("Скрипт окончен")


# zadch14()

# Заполнение данных в таблице
def zadchtest():
    try:
        conn2 = psycopg2.connect('postgresql://postgres:123@localhost:5432/bd')
        conn2.autocommit = True
        cursor2 = conn2.cursor()
        bob = ("Bob", 42)
        cursor2.execute("INSERT INTO users(id, name, password) VALUES (100, %s, %s)", bob)
        # people = [("Sam", 28), ("Alice", 33), ("Kate", 25)]
        # cursor.executemany("INSERT INTO people (name, age) VALUES (%s, %s)", people)

        print('Успешно данные заполнены')
        print("Действие выполнено в PostgreSQL")
        cursor2.close()
        conn2.close()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print("Скрипт окончен")


# zadchtest()

# Шифровка и расшифровка паролей
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(stored_password, provided_password):
    return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()


# Пример использования Шифровки и расшифровки паролей
def zadchtest2():
    try:
        conn2 = psycopg2.connect('postgresql://postgres:123@localhost:5432/bd')
        conn2.autocommit = True
        cursor2 = conn2.cursor()
        cursor2.execute("SELECT * FROM users")
        test4 = cursor2.fetchall()
        for i in test4:
            print(i[2])
            # Пример использования
            stored_password = hash_password(i[2])
            print(stored_password)
            test5 = check_password(stored_password, i[2])
            if test5 == True:
                print('true')
                print('======================================')
            else:
                print('not')
                print('======================================')

        print("Действие выполнено в PostgreSQL")
        cursor2.close()
        conn2.close()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print("Скрипт окончен")


# zadchtest2()


# Изучение функций fetchall, executemany
def zadchtest3():
    try:
        conn2 = psycopg2.connect('postgresql://postgres:123@localhost:5432/bd')
        conn2.autocommit = True
        cursor2 = conn2.cursor()
        # Удаляем строки, где name = Bob
        cursor2.execute("DELETE FROM people WHERE name=%s", ("Bob",))
        conn2.commit()

        # удаляем строки с id =3 и id=5
        people = [(3,), (5,)]
        cursor.executemany("DELETE FROM people WHERE id=%s", people)
        conn.commit()

        # проверяем
        cursor.execute("SELECT * FROM people")
        print(cursor.fetchall())  # [(1, 'Tomas', 38), (4, 'Alice', 33)]

        print("Действие выполнено в PostgreSQL")
        cursor2.close()
        conn2.close()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print("Скрипт окончен")


# zadchtest3()
