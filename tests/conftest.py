from pathlib import Path

import pytest

from src.vacancies_class import Vacancies
from src.vacancies_class_file import VacanciesFile


@pytest.fixture
def vacancy() -> Vacancies:
    return Vacancies(
        "Python Developer Senior",
        "https://hh.ru/vacancy",
        "5/2",
        "от 3-х лет",
        "Опыт работы с реляционными и нереляционными базами данных: PostgreSQL, Redis.",
        "Проектирование, разработка и поддержка backend-сервисов, телеграм ботов и API.",
        200000,
    )


@pytest.fixture
def other_vacancy() -> Vacancies:
    return Vacancies(
        "Python Developer",
        "https://hh.ru/vacancy",
        "2/2",
        "от 5-ти лет",
        "Опыт работы с реляционными и нереляционными базами данных: PostgreSQL, Redis.",
        "Проектирование, разработка и поддержка backend-сервисов, телеграм ботов и API.",
        150000,
    )


@pytest.fixture
def storage(tmp_path: Path) -> VacanciesFile:
    tmp_file = tmp_path / "test_vacancies.json"
    storage = VacanciesFile(filename=str(tmp_file))
    return storage
