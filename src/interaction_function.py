from src.hh_class import HeadHunterAPI
from src.vacancies_class_file import VacanciesFile
from src.vacancies_class import Vacancies

def user_interaction() -> None:
    """Функция для взаимодействия с пользователем"""
    hh_api = HeadHunterAPI()
    storage = VacanciesFile("vacancies.json")
    search_query = input("Введите поисковой запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для вывода вакансий: ").split()
    query_result = hh_api.get_vacancies(search_query)
    vacancies_objects = [Vacancies.cast_to_object(v) for v in query_result]
    top_vacancies = sorted(vacancies_objects, reverse=True)[:top_n]
    filtered_vacancies = storage.get_vacancies_from_file(filter_words)
    filtered_objects = [Vacancies.cast_to_object(v) for v in filtered_vacancies]
    print("\nТоп вакансий: ")
    if top_vacancies:
        for vac in top_vacancies:
            print(vac)
    else:
        print("Вакансии не найдены.")
    print("\nВакансии по ключевым словам: ")
    if filtered_vacancies:
        for vac in filtered_objects:
            print(vac)
    else:
        print("Нет совпадений.")


