from typing import Any, Dict, List, cast

import requests

from src.base_class_api import BaseClassAPI


class HeadHunterAPI(BaseClassAPI):
    """Класс для работы с API hh.ru"""

    def __init__(self) -> None:
        """Инициализация приватного атрибута класса"""
        self._HeadHunterAPI__base_url = None
        self.__base_url = "https://api.hh.ru/vacancies"

    def _connect_api(self, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Метод подключения к API"""
        try:
            response = requests.get(self.__base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                items = data.get("items", [])
                return cast(List[Dict[str, Any]], items)
            else:
                print(f"Запрос неуспешен: {response.status_code}: {response.reason}")
                return []
        except requests.RequestException as e:
            print(f"Ошибка при подключении к API: {e}")
            return []

    def get_vacancies(self, key_word: str) -> List[Dict[str, Any]]:
        """Метод получения вакансий по ключевому слову"""
        params = {"text": key_word, "per_page": 50, "page": 0}
        return self._connect_api(params)
