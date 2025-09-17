# Користувацький виняток
class GroupLimitError(Exception):
    """Виняток, якщо у групі більше 10 студентів"""
    pass


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} y.o."


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, record book: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError(f"У групі {self.number} вже 10 студентів! Неможливо додати {student.first_name}.")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(s) for s in self.group)
        return f'Group: {self.number}\n{all_students}'


# --- Перевірка ---
st_list = [
    Student('Male', 20, 'Name', f'Lastname{i}', f'RB{i}')
    for i in range(1, 12)
]

gr = Group('PD1')

for st in st_list:
    try:
        gr.add_student(st)
    except GroupLimitError as e:
        print("❌ Помилка:", e)

print("\n📋 Склад групи:")
print(gr)
