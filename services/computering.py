from flask import session
from services.database.database import Computer, DB


# функция добавления компьютера
# вернет:
# 0 - ОК
# 1 - все плохо
def compit(data: dict) -> int:
    pc = Computer(
        name=data.get("name"),
        price=data.get("price"),
        manufacturer=data.get("manufacturer"),
        date=data.get("date"),
        cpu=data.get("cpu"),
        sdd=data.get("sdd"),
        ram=data.get("ram"),
        gpu=data.get("gpu")
    )

    db : DB = DB()
    result_of_pc = db.append_pc(data=pc)

    if isinstance(result_of_pc, int):
        if result_of_pc == 0:
            return 0
        return 1
    return 1

# функция вывода всех компьютеров
# вернет:
# list - ОК
# 1 - все плохо
def all_pcs() -> int:
    db : DB = DB()
    result_of_pc = db.get_all_pcs()

    if isinstance(result_of_pc, list):
        return result_of_pc
    return 1