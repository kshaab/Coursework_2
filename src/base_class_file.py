from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseClassFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancies_in_file(self, vacancy: Dict[str, Any]) -> None:
        """Метод для добавления вакансий в файл"""
        ...

    @abstractmethod
    def get_vacancies_from_file(self, keywords: list[str]) -> list[dict]:
        """Метод получения данных из файла"""
        ...

    @abstractmethod
    def del_vacancies_from_file(self) -> None:
        """Метод для удаления информации о вакансии"""
        ...
