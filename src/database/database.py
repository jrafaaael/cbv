import json
from typing import List
from os import getcwd


class Database:
    def __init__(self, db_name: str):
        self.__db_path = f"{getcwd()}/database/{db_name}.json"

    def __open(self):
        with open(self.__db_path) as db:
            data = json.load(db)
            db.close()
            return data

    def __save(self, data):
        with open(self.__db_path, "w+") as db:
            data = json.dumps(data, indent=2, separators=(",", ": "))
            db.write(data)
            db.close()

    def find(self, field, value):
        db: List = self.__open()
        data = next((object for object in db if object[field] == value), None)
        return data

    def create(self, data):
        db: List = self.__open()
        db.append(data)
        self.__save(db)
        return data

    def update(self, field, data, where):
        db: List = self.__open()

        for object in db:
            if object[where["field"]] == where["value"]:
                if type(object[field]) is list:
                    object[field].append(data)

        self.__save(db)
