import psycopg2, random
from psycopg2 import Error

# Ошибка при работе с PostgreSQL 'utf-8' codec can't decode byte 0xc2 in position 61: invalid continuation byte
# Если такая ошибка значит не может подключиться к бд, возможно не правильный пароль, пароль должен быть 123.
# И в конце название базы данных, если ее нету, то нужно создать.
# conn = psycopg2.connect('postgresql://postgres:123@localhost:5432/demo')

# 1.1 задача==============================================================================================================================
def zad11():
    import random

    for i in range(1, 11):
        imya = 'user' + str(i)
        print(i)
        teststr = '123456789101112131415161718192021222324252627282930QWERTYUIOPASDFGHJZXCVBNMQWERTYUIOPASDFGHJZXCVBNMQWERTYUIOPASDFGHJZXCVBNM'
        psw = ''.join([random.choice(teststr) for x in range(5)])
        passwd = psw
        print('Имя пользователя -', imya)
        print('Пароль пользователя -', passwd)
        conn = psycopg2.connect('postgresql://postgres:123@localhost:5432/demo')
        conn.autocommit = True
        # Создаем курсор для выполнения операций с базой данных
        cursor = conn.cursor()
        postgreSQL_create_bd = f"CREATE USER {imya} WITH PASSWORD '{passwd}';"
        cursor.execute(postgreSQL_create_bd)
        print('Успешно создан пользователь')
        cursor.close()
        conn.close()


# zad11()

# 1.2 задача==============================================================================================================================
def zadch12():
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect('postgresql://postgres:123@localhost:5432/demo')
        conn.autocommit = True
        print('успешно')
        # Создайте курсор для выполнения операций с базой данных
        cursor = conn.cursor()

        for i in range(1, 11):
            imya = 'BD' + str(i)
            create_database_query = f"""
            CREATE DATABASE {imya} ;
            """
            cursor.execute(create_database_query)
            print('Успешно')

        # Выполнение команды
        # cursor.execute(create_database_query)

        conn.commit()
        cursor.close()
        conn.close()
        print("Действие выполнено в PostgreSQL")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print("Скрипт окончен")


# zadch12()

# 1.3 задача==============================================================================================================================
# настроить права доступа пользователей к базам данных.
# Пользователь user1 имеет доступ только к базе данных BD1, user2 имеет
# доступ только к базе данных BD2 и т. д.
def zadch13():
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect('postgresql://postgres:123@localhost:5432/demo')
        conn.autocommit = True
        print('успешно')
        # Создайте курсор для выполнения операций с базой данных
        cursor = conn.cursor()

        for i in range(1, 11):
            user = 'user' + (str(i))
            bd = 'bd' + str(i)
            create_database_query = f"""
            GRANT ALL PRIVILEGES ON DATABASE "{bd}" to {user};
            """
            cursor.execute(create_database_query)
            print('Успешно')

        conn.commit()
        cursor.close()
        conn.close()
        print("Действие выполнено в PostgreSQL")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print("Скрипт окончен")

# zadch13()

# Создание пользователей, создал таблицу, добавил в нее данные пользователей===================================================================================================
def zadchtest4():
    try:
        conn2 = psycopg2.connect('postgresql://postgres:123@localhost:5432/bd')
        conn2.autocommit = True
        cursor2 = conn2.cursor()

        for i in range(1, 11):
            imya = 'user' + str(i)
            # print(i)
            teststr = '123456789101112131415161718192021222324252627282930QWERTYUIOPASDFGHJZXCVBNMQWERTYUIOPASDFGHJZXCVBNMQWERTYUIOPASDFGHJZXCVBNM'
            psw = ''.join([random.choice(teststr) for x in range(5)])
            passwd = psw
            # print('Имя пользователя -', imya)
            # print('Пароль пользователя -', passwd)
            postgreSQL_create_bd = f"CREATE USER {imya} WITH PASSWORD '{passwd}';"
            cursor2.execute(postgreSQL_create_bd)
            print('Успешно создан пользователь')
            if i == 1:
                creates_table_query = '''CREATE TABLE Users
                                      (ID SERIAL PRIMARY KEY,
                                      name           TEXT    NOT NULL,
                                      password         TEXT NOT NULL); '''

                cursor2.execute(creates_table_query)
                conn2.commit()

            creates_table_query4 = f'''
                INSERT INTO Users VALUES ({i},'{imya}', '{passwd}')
            '''
            cursor2.execute(creates_table_query4)
            conn2.commit()

            if i == 10:
                print('Последнее')
                cursor2.execute("SELECT * FROM Users")
                print(cursor2.fetchall())
                print('==============')

        print("Действие выполнено в PostgreSQL")
        cursor2.close()
        conn2.close()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print("Скрипт окончен")


# zadchtest4()
