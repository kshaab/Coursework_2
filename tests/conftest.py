from pathlib import Path

import pytest
from src.vacancies_class import Vacancies
from src.vacancies_class_file import VacanciesFile

@pytest.fixture
def vacancy() -> Vacancies:
    return Vacancies("Python Developer Senior", "https://hh.ru/vacancy",
                     "Разработка приложений", "Знание ООП",
                     200000)

@pytest.fixture
def other_vacancy() -> Vacancies:
    return Vacancies("Python Developer Junior", "https://hh.ru/vac2",
                          "Разработка ПО", "Знание ООП",
                          120000)

@pytest.fixture
def storage(tmp_path: Path) -> VacanciesFile:
    tmp_file = tmp_path / "test_vacancies.json"
    storage = VacanciesFile(filename=str(tmp_file))
    return storage