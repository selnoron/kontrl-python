# флаг для создания таблицы при старте
CREATE_TABLES = True


# Таблица пользователей
# id - int
# логин - str 32
# пароль - str 32
# версия операционной системы - str 64
# почта - str 64
TABLE_USERS = '''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(32) NOT NULL,
    password VARCHAR(32) NOT NULL,
    os_version VARCHAR(64) NOT NULL,
    email VARCHAR(64) NOT NULL
)
'''

# Таблица пользователей
# id - int
# цена - int
# название - str 32
# производитель - str 64
# дата производства - str 64
# процессор - str 64
# память - int
# оперативка - int 
# видеокарта - str 64
TABLE_COMPUTERS = '''
CREATE TABLE pcs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    price INTEGER NOT NULL,
    name VARCHAR(32) NOT NULL,
    manufacturer VARCHAR(32) NOT NULL,
    date VARCHAR(64) NOT NULL,
    cpu VARCHAR(64) NOT NULL,
    sdd INTEGER NOT NULL,
    ram INTEGER NOT NULL,
    gpu VARCHAR(64) NOT NULL
)
'''

# Таблица пользователей
# id - int
# логин юзера - str 32
# название компьютера - str 32
# его цена - str 32
# его производитель - str 32
TABLE_CARTS = '''
CREATE TABLE carts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_login VARCHAR(32) NOT NULL,
    comp_name VARCHAR(32) NOT NULL,
    comp_price VARCHAR(32) NOT NULL,
    comp_manufacturer VARCHAR(32) NOT NULL
)
'''

