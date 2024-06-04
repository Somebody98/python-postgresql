# SQL-запрос для создания новой таблицы
# creates_table_query = '''CREATE TABLE mobile2
#                       (ID SERIAL PRIMARY KEY     NOT NULL,
#                       MODEL           TEXT    NOT NULL,
#                       PRICE         REAL); '''

# SQL-запрос для создания новой базы данных
# TEST66 = 'sv5'
# create_database_query = f"""
# CREATE DATABASE {TEST66} ;
# """


# SQL-запрос для заполнения таблицы данными
# INSERT INTO Users VALUES ({i},'{imya}', '{passwd}')

# INSERT INTO public.shop_category(
# id, name)
# VALUES (1, 'Телевизоры'),
# (2, 'Холодильники'),
# (3, 'Ноутбуки'),
# (4, 'Кофемашины'),
# (5, 'Проекторы'),
# (6, 'Флешки');


# UPDATE Products
# SET Price = Price + 3000;

# UPDATE Products
# SET Manufacturer = 'Samsung Inc.'
# WHERE Manufacturer = 'Samsung';

# UPDATE Products
# SET Manufacturer = 'Samsung',
#     ProductCount = ProductCount + 3
# WHERE Manufacturer = 'Samsung Inc.';

# Очищение всех данных из таблицы
# DELETE FROM имя_таблицы

# DELETE FROM Products
# WHERE Manufacturer='Apple';

# Сортировка по возрастанию
# SELECT ProductName, Manufacturer
# FROM Products
# ORDER BY Manufacturer DESC;

# Сортировка по убыванию
# SELECT ProductName, Manufacturer
# FROM Products
# ORDER BY Manufacturer ASC;

# Например, выберем товары, у которых производитель либо Samsung, либо Xiaomi, либо Huawei:
# SELECT * FROM Products
# WHERE Manufacturer IN ('Samsung', 'HTC', 'Huawei');

# Оператор LIKE
# SELECT * FROM Products
# WHERE ProductName LIKE 'iPhone%';

# ================================================================================================================================================
# Создание пользователя с паролем
# CREATE USER danil WITH PASSWORD '123';

# Удаление пользователя
# drop user user1;


# Задаем привилегиями базе данных database1 пользователю - user123
# GRANT ALL PRIVILEGES ON DATABASE "database1" to user123;

# Если мы хотим дать максимальные права на базу данных, то можно сделать пользователя ее владельцем:
# ALTER DATABASE database1 OWNER TO dmosk;

# Также можно дать доступ к базе для определенных таблиц:
# database1=# GRANT ALL PRIVILEGES ON TABLE table1 IN SCHEMA public TO "dmosk";