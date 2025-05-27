import re

class Person:
    def __init__(self, first_name, surname, patronymic, email):
        """
        Инициализирует объект Person.

        :param first_name: Имя человека.
        :param surname: Фамилия человека.
        :param patronymic: Отчество человека.
        :param email: Электронная почта человека.
        """
        setattr(self, "first_name", first_name)
        setattr(self, "surname", surname)
        setattr(self, "patronymic", patronymic)
        setattr(self, "email", email)

    def __repr__(self):
        """
        Возвращает строковое представление объекта Person.

        :return: Строка в формате "Person(surname=..., first_name=..., patronymic=..., email=...)".
        """
        return f"Person(surname={self.surname}, first_name={self.first_name}, patronymic={self.patronymic}, email={self.email})" 

    def __setattr__(self, name, value):
        """
        Устанавливает атрибут объекта. Если атрибут — email, проверяет его корректность.

        :param name: Имя атрибута.
        :param value: Значение атрибута.
        :raises ValueError: Если email некорректен.
        """
        if name == "email":
            # Проверка корректности email
            if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
                raise ValueError(f"Некорректный email: {value}")
        super().__setattr__(name, value)  # Устанавливаем атрибут
        
class Student(Person):
    def __init__(self, number, first_name, surname, patronymic, email, group):
        """
        Инициализирует объект Student.

        :param number: Номер студента.
        :param first_name: Имя студента.
        :param surname: Фамилия студента.
        :param patronymic: Отчество студента.
        :param email: Электронная почта студента.
        :param group: Группа студента.
        """        
        super().__init__(first_name, surname, patronymic, email)
        setattr(self, "number", number)
        setattr(self, "group", group)

    def __repr__(self):
        """
        Возвращает строковое представление объекта Student.

        :return: Строка в формате "Student(number=..., surname=..., first_name=..., patronymic=..., email=..., group=...)".
        """        
        return f"Student(number={self.number}, surname={self.surname}, first_name={self.first_name}, patronymic={self.patronymic}, email={self.email}, group={self.group})"

class StudentCollection:
    def __init__(self, students=None):
        """
        Инициализирует объект StudentCollection.

        :param students: Список студентов (по умолчанию пустой).
        """
        if students is None:
            self.students = []
        else:
            self.students = students
            
    def __iter__(self):
        """
        Возвращает итератор для коллекции студентов.

        :return: Итератор.
        """
        self.index = 0
        return self
        
    def __next__(self):
        """
        Возвращает следующего студента в коллекции.

        :return: Следующий студент.
        :raises StopIteration: Если достигнут конец коллекции.
        """        
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        else:
            raise StopIteration
    
    def __getitem__(self, index):
        """
        Возвращает студента по индексу.

        :param index: Индекс студента.
        :return: Студент.
        """
        return self.students[index]

    def __repr__(self):
        """
        Возвращает строковое представление объекта StudentCollection.

        :return: Строка в формате "StudentCollection(students=...)".
        """
        return f"StudentCollection(students={self.students})"

    def add_student(self, student):
        """
        Добавляет студента в коллекцию.

        :param student: Объект Student.
        :raises ValueError: Если студент уже существует или передан не Student.
        """
        if not isinstance(student, Student):
            raise ValueError("Вы пытаетесь добавить не студента")
        #Проверка уникальности номера и электронной почты студента
        if not self.is_valid_student_number(student.number):
            raise ValueError(f"Некорректный номер студента: {student.number}")
        if any(s.number == student.number for s in self.students):
            raise ValueError(f"Студент с номером {student.number} уже существует")
        if any(s.email == student.email for s in self.students):
            raise ValueError(f"Студент с почтой {student.email} уже существует")
        self.students.append(student)

    def add_students(self, students):
        """
        Добавляет несколько студентов в коллекцию.

        :param students: Список студентов.
        """
        for student in students:
            self.add_student(student)

    @staticmethod
    def is_valid_student_number(number):
        """
        Проверяет, является ли номер студента корректным.

        :param number: Номер студента.
        :return: True, если номер корректен, иначе False.
        """
        return isinstance(number, int) and number > 0
        
    def remove_student(self, number):
        """
        Удаляет студента из списка по номеру.
        :param number: Номер студента, которого нужно удалить.
        """        
        for student in self.students:
            if student.number == number:
                self.students.remove(student)

    def filter_by_group(self, group):
        """
        Фильтрует студентов по группе.

        :param students: Список студентов.
        :param group: Группа для фильтрации.
        :return: Отфильтрованный список студентов.
        """
        return [student for student in self.students if student.group == group]

    def sort_by_string_field(self, field):
        """
        Сортирует студентов по строковому полю.
        :param field: Название поля (например, "surname").
        :return: Отсортированный список студентов.
        """
        return sorted(self.students, key=lambda x: getattr(x, field))

    def sort_by_numeric_field(self, field):
        """
        Сортирует студентов по числовому полю.
        :param field: Название поля (например, "number").
        :return: Отсортированный список студентов.
        """
        return sorted(self.students, key=lambda x: int(getattr(x, field)))

    def save_to_file(self, filename):
        """
        Сохраняет список студентов в файл.

        :param filename: Имя файла.
        """
        with open(filename, "w") as file:
            for student in self.students:
                file.write(f"{student}\n")

    @staticmethod
    def load_from_file(filename):
        """
        Загружает список студентов из файла.

        :param filename: Имя файла.
        :return: Объект StudentCollection.
        """
        students = []
        with open(filename, "r", encoding='utf-8') as file:
            next(file) #пропускаем заголовки
            for line in file:
                data = line.strip().split(",")
                number = int(data[0])
                surname = data[1]
                first_name = data[2]
                patronymic = data[3]
                email = data[4]
                group = data[5]
                students.append(Student(number, first_name, surname, patronymic, email, group))
        return StudentCollection(students)

    def generate_students_by_group(self, group):
        """
        Генерирует студентов по группе.

        :param group: Группа для фильтрации.
        :return: Генератор студентов.
        """
        for student in self.students:
            if student.group == group:
                yield student#изменения в файле person.py
