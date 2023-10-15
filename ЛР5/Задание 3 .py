class student:#создаем класс student
    def __init__(self, name, group, yspev): #функция __init__ с параметрами self, name , qroup, yspev
        self.name = name#инициализируем name
        self.group = group#инициализируем group
        self.yspev = yspev#инициализируем yspev
    def print_info(self):#функция print_info с параметрами self
        print(f'ФИ:{self.name},группа:{self.group},успеваемость:{self.yspev}')

student1 = student('Емельянович Арсений', '21ПО', '10')
student2 = student('Побединский Архип', '21ПО', '3')
student3 = student('Данишевский Даниил', '21ПО', '8')
student4 = student('Сурвило Артем ', '21ПО', '9')
student5 = student('Жук Никита', '21ПО', '3')
student6 = student('Мишенков Иван', '21ПО', '8')
student7 = student('Страшкевич Даниил', '21ПО', '9')
student8 = student('Тополь Алексей', '21ПО', '9')
student9 = student('Поляк Илья', '21ПО', '10')
student10 = student('Чайка Игорь', '21ПО', '10')# данные студентов
st_list = [student1, student2, student3 ,student4 ,student5,student6,student7,student8,student9,student10]#создаем список студентов
for st in st_list:
    st.print_info()