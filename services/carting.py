from flask import session
from services.database.database import Cart, DB


# функция добавления в корзину
# вернет:
# 0 - ОК
# 1 - все плохо
def carte(data: dict, user_login: str) -> int:
    crt = Cart(
        user_login=user_login,
        comp_name=data.get("comp_name"),
        comp_price=data.get("comp_price"),
        comp_manufacturer=data.get("comp_manufacturer"),
    )

    db : DB = DB()
    result_of_cart = db.cart_append(data=crt)

    if isinstance(result_of_cart, int):
        if result_of_cart == 0:
            return 0
        return 1
    return 1

# функция вывода корзины пользователя
# вернет:
# list - ОК
# 1 - все плохо
def all_user_carts(data: str) -> int or list:
    db : DB = DB()
    result_of_cart = db.get_carts(data=data)

    if isinstance(result_of_cart, list):
        return result_of_cart
    return 1

# функция удаления продукта из корзины 
# вернет:
# 0 - ОК
# 1 - все плохо
def delete_cart(data: int) -> int:
    db : DB = DB()
    result_of_delete = db.delete_cart(data)
    print(result_of_delete, 'DELETE')
    if result_of_delete == 0:
        return 0
    return 1
    