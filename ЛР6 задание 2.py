import random#ипмпортируем модуль рандом
class Student:#новый класс Student
    def init(self, name, group_number, academic_performance):#функция init c параметрами name, group_number, academic_performance
        self.name = name
        self.group_number = group_number
        self.academic_performance = academic_performance#инициализируем параметры
        self.gpa_scores = sum(self.academic_performance) / 5#
    def print_info(self):#функция print_info
        print(f'ФИ: {self.name}\n'#
        f' Номер группы: {self.group_number}\n'
        f' Успеваемость: {self.academic_performance}\n'
        f' Средний балл: {self.gpa_scores}\n')#выводим информацию
def byGPA_key(person):#функция
    return person.gpa_scores#возвращаем результат
students = [
Student(
input('Введите фамилию и имя студента: '),
input('Введите номер группы: '),#запрашиваем пользователя ввести информацию
[random.randint(1, 10) for i in range(5)]
)
for _ in range(10)#рандом оценок
]
students_sort = sorted(students, key=byGPA_key)#сортировка студентов
for student in students_sort:#для студента в сортированных
    student.print_info()#вывод информации студента