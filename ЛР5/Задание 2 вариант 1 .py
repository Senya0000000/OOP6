class Fraction:
    def __init__(self, m, n):
        # Конструктор класса инициализирует поля числитель (m) и знаменатель (n) дроби.
        self.m = m
        self.n = n

    def multiply(self, other):
        # Метод для умножения двух дробей.
        result_m = self.m * other.m
        result_n = self.n * other.n
        return Fraction(result_m, result_n)

    def divide(self, other):
        # Метод для деления одной дроби на другую.
        result_m = self.m * other.n
        result_n = self.n * other.m
        return Fraction(result_m, result_n)

    def __str__(self):
        # Метод для представления дроби в виде строки (для удобства вывода).
        return f'({self.m}/{self.n})'

# Создание двух объектов дробей.
fraction1 = Fraction(3, 4)
fraction2 = Fraction(2, 5)

# Вызов метода умножения и вывод результата.
product = fraction1.multiply(fraction2)
print(f'{fraction1} * {fraction2} = {product.m}*{product.n}/{fraction1.n}*{fraction2.n}')

# Вызов метода деления и вывод результата.
quotient = fraction1.divide(fraction2)
print(f'{fraction1} / {fraction2} = {quotient.m}*{fraction2.n}/{fraction1.n}*{fraction2.m}')
