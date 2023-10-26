from train import Train
def find_trains_to_destination(trains, destination):
    """
    Выводит список поездов, следующих до заданного пункта назначения.
    :param trains: Массив объектов поездов.
    :param destination: Пункт назначения.
    """
    matching_trains = [train for train in trains if train.destination == destination]
    if not matching_trains:
        print(f"Нет поездов, идущих до {destination}.")
    else:
        print(f"Список поездов, следующих до {destination}:")
        for train in matching_trains:
            train.print_info()
            print("\n")
if __name__ == "__main__":
    # Создаем массив объектов Train
    trains = [
        Train("Москва", "123", "08:00", 200, 10, 50),
        Train("Санкт-Петербург", "456", "09:30", 150, 5, 30),
        Train("Казань", "789", "10:45", 180, 8, 40),
    ]
    # Заданный пункт назначения
    destination = "Москва"
    find_trains_to_destination(trains, destination)