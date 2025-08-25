import json

from src.vacancies_class_file import VacanciesFile


def test_add_vacancy(storage: VacanciesFile) -> None:
    vacancy = {"name": "Python Developer", "url": "http://test.com/1"}
    storage.add_vacancies_in_file(vacancy)
    with open(storage.filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["name"] == "Python Developer"


def test_add_duplicate_vacancies(storage: VacanciesFile) -> None:
    vacancy = {"name": "Python Developer", "url": "http://test.com/1"}
    storage.add_vacancies_in_file(vacancy)
    storage.add_vacancies_in_file(vacancy)
    with open(storage.filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1


def test_add_several_vacancies(storage: VacanciesFile) -> None:
    vacancies = [
        {"name": "Python Developer", "url": "http://test.com/1"},
        {"name": "Python Developer Senior", "url": "http://test.com/2"},
    ]
    storage.add_vacancies_in_file(vacancies)
    with open(storage.filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 2
    assert any(v["name"] == "Python Developer" for v in data)


def test_get_vacancies_from_file(storage: VacanciesFile) -> None:
    vacancies = [
        {"name": "Python Developer", "url": "http://test.com/1"},
        {"name": "Python Developer Senior", "url": "http://test.com/2"},
    ]
    storage.add_vacancies_in_file(vacancies)
    result = storage.get_vacancies_from_file([])
    assert len(result) == 2


def test_get_vacancies_from_file_filter(storage: VacanciesFile) -> None:
    vacancies = [
        {"name": "Python Developer", "url": "http://test.com/1"},
        {"name": "Java Developer", "url": "http://test.com/2"},
    ]
    storage.add_vacancies_in_file(vacancies)
    result = storage.get_vacancies_from_file(["Java"])
    assert len(result) == 1
    assert result[0]["name"] == "Java Developer"


def test_del_vacancies_from_file(storage: VacanciesFile) -> None:
    vacancies = [
        {"name": "Python Developer", "url": "http://test.com/1"},
        {"name": "Java Developer", "url": "http://test.com/2"},
    ]
    storage.add_vacancies_in_file(vacancies)
    storage.del_vacancies_from_file()
    with open(storage.filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data == []
