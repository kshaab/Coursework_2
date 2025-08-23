import os
import json
from typing import Dict, Any, List, Union

from src.base_class_file import BaseClassFile
from src.hh_class import HeadHunterAPI

class VacanciesFile(BaseClassFile):
    """Класс для работы с JSON-файлами"""

    def __init__(self, filename: str = "vacancies.json"):
        """Инициализация атрибута с именем файла"""
        self.__filename = os.path.join("../data", filename)

        if not os.path.exists(self.__filename):
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)


    def add_vacancies_in_file(self, vacancies: Union[Dict[str, Any], list[Dict[str, Any]]]) -> None:
        """Метод для добавления вакансий в файл"""
        with open(self.__filename, "r", encoding="utf-8") as f:
            data: List[Dict[str, Any]] = json.load(f)


        if isinstance(vacancies, dict):
            vacancies = [vacancies]


        for vacancy in vacancies:
            if not any(v.get("url") == vacancy.get("url") for v in data):
                data.append(vacancy)


        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_vacancies_from_file(self, params: Dict[str, Any] | None = None) -> List[Dict[str, Any]]:
        """Метод получения данных из файла по фильтрам"""
        with open(self.__filename, "r", encoding="utf-8") as f:
            data: List[Dict[str, Any]] = json.load(f)

        if not params:
            return data

        return [vac for vac in data if all(str(value).lower() in str(vac.get(key, "")).lower() for key, value in params.items())]

    def del_vacancies_from_file(self) -> None:
        """Метод для удаления всех вакансий"""
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    hh = HeadHunterAPI()
    vacancies_data = hh.get_vacancies("Python")
    storage = VacanciesFile("vacancies.json")
    storage.add_vacancies_in_file(vacancies_data)
    print(storage.get_vacancies_from_file({}))
