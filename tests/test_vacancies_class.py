from src.vacancies_class import Vacancies
import pytest


def test_vacancies_class(vacancy: Vacancies) -> None:
    assert vacancy.name == "Python Developer Senior"
    assert vacancy.url == "https://hh.ru/vacancy"
    assert vacancy.schedule == "5/2"
    assert vacancy.experience == "от 3-х лет"
    assert vacancy.requirements == "Опыт работы с реляционными и нереляционными базами данных: PostgreSQL, Redis."
    assert vacancy.responsibility == "Проектирование, разработка и поддержка backend-сервисов, телеграм ботов и API."
    assert vacancy.salary == 200000

def test_vacancies_class_name_error() -> None:
    with pytest.raises(ValueError):
        Vacancies(" ", "https://hh.ru/vacancy",
                     "5/2", "от 3-х лет",
                     "Опыт работы с реляционными и нереляционными базами данных: PostgreSQL, Redis.",
                     "Проектирование, разработка и поддержка backend-сервисов, телеграм ботов и API.",
                     200000)

def test_vacancies_class_url_error() -> None:
    with pytest.raises(ValueError):
        Vacancies("Python Developer Senior", "htt://hh.ru/vacancy",
                     "5/2", "от 3-х лет",
                     "Опыт работы с реляционными и нереляционными базами данных: PostgreSQL, Redis.",
                     "Проектирование, разработка и поддержка backend-сервисов, телеграм ботов и API.",
                     200000)

def test_vacancies_class_salary_error() -> None:
    with pytest.raises(ValueError):
        Vacancies("Python Developer Senior", "https://hh.ru/vacancy",
                     "5/2", "от 3-х лет",
                     "Опыт работы с реляционными и нереляционными базами данных: PostgreSQL, Redis.",
                     "Проектирование, разработка и поддержка backend-сервисов, телеграм ботов и API.",
                     -200000)


def test_vacancies_property(vacancy: Vacancies) -> None:
    assert vacancy.salary == 200000


def test_vacancies_property_setter(vacancy: Vacancies) -> None:
    with pytest.raises(ValueError):
        Vacancies("Python Developer Senior", "https://hh.ru/vacancy",
                     "5/2", "от 3-х лет",
                     "Опыт работы с реляционными и нереляционными базами данных: PostgreSQL, Redis.",
                     "Проектирование, разработка и поддержка backend-сервисов, телеграм ботов и API.",
                     -200000)
    assert vacancy.salary == 200000

def test_cast_to_object() -> None:
    data = {
        "name": "Python Developer",
        "url": "https://hh.ru/vacancy",
         "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
        "experience": {"name": "1-3 года"},
        "snippet": {
            "requirement": "умение писать на Python",
            "responsibility": "Проектирование"
        },
        "salary": 200000
    }

    vac = Vacancies.cast_to_object(data)

    assert isinstance(vac, Vacancies)
    assert vac.name == "Python Developer"
    assert vac.salary == 200000
    assert vac.experience == "1-3 года"
    assert vac.requirements == "умение писать на Python"
    assert vac.responsibility == "Проектирование"
    assert vac.schedule == "5/2"


def test_vacancies_lt(vacancy: Vacancies, other_vacancy: Vacancies) -> None:
    assert (vacancy.salary < other_vacancy.salary) == False

def test_vacancies_le(vacancy: Vacancies, other_vacancy: Vacancies) -> None:
    assert (vacancy.salary <= other_vacancy.salary) == False

def test_vacancies_gt(vacancy: Vacancies, other_vacancy: Vacancies) -> None:
    assert (vacancy.salary > other_vacancy.salary) == True

def test_vacancies_ge(vacancy: Vacancies, other_vacancy: Vacancies) -> None:
    assert (vacancy.salary >= other_vacancy.salary) == True
