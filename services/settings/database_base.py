# флаг для создания таблицы при старте
CREATE_TABLES = True


# Таблица пользователей
# id - int
# логин - str 32
# пароль - str 32
# версия операционной системы - str 64
TABLE_USERS = '''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(32) NOT NULL,
    password VARCHAR(32) NOT NULL,
    os_version VARCHAR(64) NOT NULL,
    email VARCHAR(64) NOT NULL
)
'''

TABLE_USERS = '''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(32) NOT NULL,
    password VARCHAR(32) NOT NULL,
    os_version VARCHAR(64) NOT NULL,
    email VARCHAR(64) NOT NULL
)
'''
