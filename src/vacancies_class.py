class Vacancies:
    """Класс для работы с вакансиями"""
    __slots__ = ("name", "url", "schedule", "experience", "requirements", "responsibility", "__salary")

    def __init__(self, name: str, url: str, schedule: str, experience: str, requirements: str, responsibility: str, salary: int) -> None:
        """Инициализация атрибутов"""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Вакансии не найдены")
        if not url.startswith("http"):
            raise ValueError("Несуществующая ссылка")
        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self.name = name
        self.url = url
        self.schedule = schedule
        self.experience = experience
        self.requirements = requirements
        self.responsibility = responsibility
        self.__salary = salary

    def __str__(self) -> str:
        """Метод для вывода вакансий в строку"""
        return (f"{self.name}({self.url}), {self.salary}, {self.schedule}, {self.experience}: "
                f"\n{self.requirements if self.requirements else " "}. {self.responsibility if self.responsibility else " "}").strip()

    @property
    def salary(self) -> int:
        """Геттер з/п"""
        return self.__salary

    @salary.setter
    def salary(self, value: int) -> None:
        """Валидация з/п"""
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        else:
            self.__salary = value

    @classmethod
    def cast_to_object(cls, data: dict) -> "Vacancies":
        """Метод преобразования данных в объект класса"""
        salary_data = data.get("salary", {})
        if isinstance(salary_data, dict):
            salary = salary_data.get("from") or salary_data.get("to") or 0
        else:
            salary = salary_data or 0

        snippet = data.get("snippet", {})
        work_schedule_by_days = data.get("work_schedule_by_days", [])
        get_experience = data.get("experience", {})

        schedule = work_schedule_by_days[0]["name"] if work_schedule_by_days else ""

        return cls(
            name=data.get("name", "Без названия"),
            url=data.get("url", ""),
            salary=salary,
            schedule=schedule,
            experience=get_experience.get("name", ""),
            requirements=snippet.get("requirement", "Нет требований"),
            responsibility=snippet.get("responsibility", "")
        )

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






