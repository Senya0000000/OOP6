class Counter:#создаем класс Counter
    def __init__(self):#функция __Init__
        self.value = 0#value по умолчанию 0
    def start_from(self, start_value=0):#определяем метод start_from
        self.value = start_value#необязательный аргумент по умолчанию 0
    def increment(self):#создаем метод display
        self.value += 1#увеличиваем на 1
    def display(self):#создаем метод display
        print('текущee значения счетчика: ', self.value)#вывод текущего значения счетчика self.value
    def reset(self):#создаем метод reset
        self.value = 0
counter = Counter()
counter.display()  #вывод текущего значения счетчика
counter.start_from(8)
counter.display()  #выводтекущего значения счетчика
counter.increment()
counter.display()  #вывд текущего значения счетчика
counter.reset()
counter.display()  #вывод текущего значения счетчика