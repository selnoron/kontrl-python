# sqlite3 позволяет работать с БД
# в режиме файловой системы
# без панели администратора и т.д.
import sqlite3
# Позволяет работать с датами
import datetime
# Для работы с json строками и различным
# преоразованием 
import json
# настройки для БД
from services.settings.database_base import TABLE_USERS, TABLE_COMPUTERS, TABLE_CARTS, CREATE_TABLES
# подключение именованных кортежей
from typing import NamedTuple



# Модель пользователя User
class User(NamedTuple):
    login      : str
    email      : str
    password   : str
    os_version : str


# Модель корзины Cart
class Cart(NamedTuple):
    user_login        : str
    comp_name         : str
    comp_price        : str
    comp_manufacturer : str


# Модель компьютера Computer
class Computer(NamedTuple):
    name         : str
    price        : int
    manufacturer : str
    date         : str
    cpu          : str
    sdd          : int
    ram          : int
    gpu          : str


# Предназначен для более простой работы
# с БД и хранению процедур, подключению и т.д.
class DB:
    def __init__(self) -> None:
        global CREATE_TABLES
        # имя БД
        self.basename = "sqlite.db"
        # объект подключения к БД
        self.connection = sqlite3.connect(self.basename)
        # Объект - указатель
        self.cursor = self.connection.cursor()
        if CREATE_TABLES:
            self.create_all_tables(
                TABLE_USERS
            )
            self.create_all_tables(
                TABLE_COMPUTERS
            )
            self.create_all_tables(
                TABLE_CARTS
            )
            CREATE_TABLES = False
    

    def execute(self, query: str, is_commit: int = 0) -> object:
        try:
            result = self.cursor.execute(query)
            if is_commit == 1:
                self.connection.commit()
                return 0
            else:
                return result.fetchall()
        except Exception as e:
            print(f" --- EXCEPTION: <{e}> --- ")
            return 1
    
    # Метод создает все таблицы для БД
    # Нужно при старте работы с БД
    def create_all_tables(self, *tables: list[str]) -> None:
        for table in tables:
            self.execute(query=table, is_commit=1)
    

    # Метод для внесения записи о пользователе
    def registrate_user(self, data: User) -> int:
        user_exists = self.execute(
            query=f'''
                SELECT id FROM users
                WHERE login='{data.login}'
                AND
                password='{data.password}'
            '''
        )
        print(user_exists, "EXISTS")
        if len(user_exists) > 0:
            return 1

        result = self.execute(
            query=f'''
                INSERT INTO users (login, password, os_version, email)
                VALUES ('{data.login}','{data.password}','{data.os_version}', '{data.email}')
            ''',
            is_commit=1
        )

        return 0


    # Метод получения всех пользователей
    def get_all_users(self) -> list:
        result = self.execute(
            query='''
                SELECT * FROM users
            '''
        )

        return result
    
    # Метод получения всех компьютеров
    def get_all_pcs(self) -> list:
        result = self.execute(
            query='''
                SELECT * FROM pcs
            '''
        )

        return result
    
    # Метод получения всех элементов из корзины
    # одного юзера
    def get_carts(self, data: str) -> list:
        result = self.execute(
            query=f'''
            SELECT * FROM carts WHERE 
                user_login='{data}'
            '''
        )

        return result
    

    # Метод для авторизации пользователя
    def authorization(self, data: dict) -> int:

        is_exists = self.execute(query=f'''
            SELECT id FROM users WHERE 
            login='{data.get('login')}' AND password='{data.get('password')}'
        ''')
        print(is_exists, '222')
        if isinstance(is_exists, list) or isinstance(is_exists, tuple):
            if len(is_exists) > 0:
                return 0
            else:
                return 1
        return 1


    # Метод для внесения записи о компьютере
    def append_pc(self, data: Computer) -> int:
        pc_exists = self.execute(
            query=f'''
                SELECT id FROM pcs
                WHERE name='{data.name}'
                AND
                manufacturer='{data.manufacturer}'
            '''
        )
        print(pc_exists, "EXISTS")
        if len(pc_exists) > 0:
            return 1

        result = self.execute(
            query=f'''
                INSERT INTO pcs (name, price, manufacturer, date, cpu, sdd, ram, gpu)
                VALUES ('{data.name}', '{data.price}','{data.manufacturer}','{data.date}', '{data.cpu}', '{data.sdd}', '{data.ram}', '{data.gpu}')
            ''',
            is_commit=1
        )

        return 0
    
    # Метод для внесения продукта в корзину
    def cart_append(self, data: Cart) -> int:
        cart_exists = self.execute(
            query=f'''
                SELECT id FROM carts
                WHERE user_login='{data.user_login}'
                AND
                comp_name='{data.comp_name}'
            '''
        )
        print(cart_exists, "EXISTS")
        if len(cart_exists) > 0:
            return 1
        print(data.comp_name)
        result = self.execute(
            query=f'''
                INSERT INTO carts (user_login, comp_name, comp_price, comp_manufacturer)
                VALUES ('{data.user_login}', '{data.comp_name}','{data.comp_price}','{data.comp_manufacturer}')
            ''',
            is_commit=1
        )

        return 0
    
    # Метод для удаления записи о продукте из корзины
    def delete_cart(self, data: int) -> int:
        cart_exists = self.execute(
            query=f'''
                SELECT * FROM carts
                WHERE id={data}
            '''
        )
        print(cart_exists, "EXISTS")
        if not len(cart_exists) > 0:
            return 1

        result = self.execute(
            query=f'''
                DELETE FROM carts WHERE id={data}; 
            ''',
            is_commit=1
        )

        return 0
