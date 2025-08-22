from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseClassFile(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_vacancies_in_file(self) -> None:
        """Метод для добавления вакансий в файл"""
        pass
    @abstractmethod
    def get_vacancies_from_file(self, params: Dict[str, Any]) -> list[dict]:
        """Метод получения данных из файла"""
        pass
    @abstractmethod
    def del_vacancies_from_file(self) -> None:
        """Метод для удаления информации о вакансии"""
        pass