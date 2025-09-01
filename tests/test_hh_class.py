from unittest.mock import Mock, patch

import requests

from src.hh_class import HeadHunterAPI


def test_hh_class() -> None:
    hh = HeadHunterAPI()
    assert hh._HeadHunterAPI__base_url == "https://api.hh.ru/vacancies"


@patch("requests.get")
def test_connect_api(mock_get: Mock) -> None:
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"items": [{"id": 1, "name": "Python Developer"}]}
    mock_get.return_value = fake_response
    hh = HeadHunterAPI()
    vacancies = hh.get_vacancies("Python")
    assert isinstance(vacancies, list)
    assert len(vacancies) == 1
    assert vacancies[0]["name"] == "Python Developer"


@patch("requests.get")
def test_connect_api_failure(mock_get: Mock) -> None:
    fake_response = Mock()
    fake_response.status_code = 404
    fake_response.reason = "Указанная вакансия не существует"
    mock_get.return_value = fake_response
    hh = HeadHunterAPI()
    vacancies = hh.get_vacancies("Python")
    assert vacancies == []


@patch("requests.get")
def test_connect_api_error(mock_get: Mock) -> None:
    mock_get.side_effect = requests.RequestException("Ошибка сетевого подключения")
    hh = HeadHunterAPI()
    vacancies = hh.get_vacancies("Python")
    assert vacancies == []
