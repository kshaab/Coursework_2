class Vacancies():
    """Класс для работы с вакансиями"""
    __slots__ = ("name", "url", "description", "requirements", "__salary")

    def __init__(self, name: str, url: str, description: str, requirements: str, salary: int) -> None:
        """Инициализация атрибутов"""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Вакансии не найдены")
        if not url.startswith("http"):
            raise ValueError("Несуществующая ссылка")
        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self.name = name
        self.url = url
        self.description = description
        self.requirements = requirements
        self.__salary = salary

    @property
    def salary(self) -> int:
        """Геттер з/п"""
        return self.__salary

    @salary.setter
    def salary(self, value: int) -> None:
        """Валидаци з/п"""
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        else:
            self.__salary = value

    def __lt__(self, other: "Vacancies") -> bool:
        """Метод для операции сравнения меньше"""
        return self.salary < other.salary

    def __le__(self, other: "Vacancies") -> bool:
        """Метод для операции сравнения меньше или равно"""
        return self.salary <= other.salary

    def __gt__(self, other: "Vacancies") -> bool:
        """Метод для операции сравнения больше"""
        return self.salary > other.salary

    def __ge__(self, other: "Vacancies") -> bool:
        """Метод для операции сравнения больше или равно"""
        return self.salary >= other.salary

if __name__ == "__main__":
    vacancy_1 = Vacancies("Python Developer Senior", "https://hh.ru/vac1",
                          "Разработка приложений", "Знание ООП",
                          200000)
    vacancy_2 = Vacancies("Python Developer Junior", "https://hh.ru/vac2",
                          "Разработка ПО", "Знание ООП",
                          120000)
    print(vacancy_1)
    print(vacancy_2)

    print(vacancy_1 > vacancy_2)
    print(vacancy_1 < vacancy_2)
    print(vacancy_1 >= vacancy_2)
    print(vacancy_1 <= vacancy_2)




