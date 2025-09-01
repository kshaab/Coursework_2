import json
import os
from typing import Any, Dict, List, Union

from src.base_class_file import BaseClassFile


class VacanciesFile(BaseClassFile):
    """Класс для работы с JSON-файлами"""

    def __init__(self, filename: str = "vacancies.json"):
        """Инициализация атрибута с именем файла"""
        self.__filename = os.path.join("data", filename)

        if not os.path.exists(self.__filename):
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)

    @property
    def filename(self) -> str:
        """Геттер для имени файла"""
        return self.__filename

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

    def get_vacancies_from_file(self, keywords: list[str]) -> list[dict]:
        """Метод получения вакансий по ключевым словам"""
        with open(self.__filename, "r", encoding="utf-8") as f:
            data: list[dict] = json.load(f)

        if not keywords:
            return data

        result = []
        for vac in data:
            text = " ".join(
                [
                    str(vac.get("name", "")),
                    str(vac.get("requirements", "")),
                    str(vac.get("responsibility", "")),
                    str(vac.get("experience", "")),
                ]
            ).lower()

            if any(kw.lower() in text for kw in keywords):
                result.append(vac)
        return result

    def del_vacancies_from_file(self) -> None:
        """Метод для удаления всех вакансий"""
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
