from flask import session
from services.database.database import User, DB


# функция авторизации пользователя
# вернет:
# 0 - ОК
# 1 - все плохо
def authorize(data: dict) -> int:
    user = {
        'login': data.get("login"),
        'password': data.get("password")
    }

    db: DB = DB()

    result_of_authorization = db.authorization(data=user)
    if result_of_authorization == 0:
        session['logged_in'] = True
        session["login"] = user.get('login')
        return 0 
    
    return 1