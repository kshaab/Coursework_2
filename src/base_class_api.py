from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseClassAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def _connect_api(self, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Метод подключения к API"""
        ...

    @abstractmethod
    def get_vacancies(self, key_word: str) -> list:
        """Метод получения вакансий"""
        ...
