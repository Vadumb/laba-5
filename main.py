from person import Student, StudentCollection

# Загрузка данных из файла
file_path = "studentsDB.csv"
students = StudentCollection.load_from_file(file_path)

# Примеры работы:
print("=== Все студенты ===")
for student in students:
    print(f"Студент №{student.number}: {student.surname} {student.first_name}")

print("\n=== Сортировка по имени ===")
sorted_students = students.sort_by_string_field("first_name")
for student in sorted_students:
    print(student.first_name)

# Добавление нового студента
new_student = Student(
    number=21,
    surname="Пиписонов",
    first_name="Антропомен",
    patronymic="Артурович",
    email="pipison16@example.com",
    group="УИДбд-21"
)
students.add_student(new_student)

# Фильтрация по группе
print("\n=== Студенты группы УИДбд-21 ===")
for s in students.filter_by_group('УИДбд-21'):
    print(f"{s.surname}, группа: {s.group}")