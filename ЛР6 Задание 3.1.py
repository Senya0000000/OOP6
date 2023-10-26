class Train:
    """
    Класс, представляющий информацию о поезде.
    """
    def __init__(self, destination, train_number, departure_time, total_seats, compartments, reserved_seats):
        """
        Инициализирует объект Train.
        :param destination: Пункт назначения поезда.
        :param train_number: Номер поезда.
        :param departure_time: Время отправления.
        :param total_seats: Число общих мест.
        :param compartments: Число купейных мест.
        :param reserved_seats: Число мест в плацкарте.
        """
        self.destination = destination
        self.train_number = train_number
        self.departure_time = departure_time
        self.total_seats = total_seats
        self.compartments = compartments
        self.reserved_seats = reserved_seats
    def print_info(self):
        """
        Выводит информацию о поезде.
        """
        print(f"Поезд номер {self.train_number} следует до {self.destination}.")
        print(f"Время отправления: {self.departure_time}")
        print(f"Общие места: {self.total_seats}")
        print(f"Купейные места: {self.compartments}")
        print(f"Плацкартные места: {self.reserved_seats}")