from abc import ABC, abstractmethod

class BaseClassAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def __connect_api(self):
        """Метод подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, key_word):
        """Метод получения вакансий"""
        pass

