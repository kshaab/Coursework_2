
import pytest
from src.vacancies_class import Vacancies

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