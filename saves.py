import json


def getDict(type: str):
    """
    Получение словаря из файла
    """
    with open("company.json") as file:
        clean = json.load(file)
    with open("snow.json") as file:
        snow = json.load(file)
    if type == "company":
        return clean
    if type == "snow":
        return snow


def makeSave(type: str, used_type: str, count: int | str, coins: int | str):
    """
    Делает сейв в файл
    """
    user_dict = {"type": type, "used_type": used_type, "count": count, "coins": coins}
    with open("save.json", "w") as json_file:
        json.dump(user_dict, json_file)


def readSave():
    """
    Читает сейв из файла
    """
    with open("save.json") as file:
        save = json.load(file)
    return save["type"], save["used_type"], save["count"], save["coins"]
