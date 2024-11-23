#--------------- H O M E  W O R K  (M O D U L E _ 10 _ 4) ---------------


import random
import time
from threading import Thread
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # Ожидание случайное время от 3 до 10 секунд
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()                   # Очередь гостей
        self.tables = tables              # Список столов

    def guest_arrival(self, *guests):
        for guest in guests:

            free_table = next((table for table in self.tables if table.guest is None), None)  # Проверяем наличие свободного стола
            if free_table:
                free_table.guest = guest                        # Сажаем гостя за стол
                guest.start()                                       # Запускаем поток гостя
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)                        # Добавляем гостя в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                    if not self.queue.empty():                          #если очередь не пуста
                        next_guest = self.queue.get()                   #берём следующего из очереди
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")




if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]


    guests = [Guest(name) for name in guests_names]     # Создание гостей
    cafe = Cafe(*tables)             # Заполнение кафе столами
    cafe.guest_arrival(*guests)         #Приём гостей
    cafe.discuss_guests()          #Обслуживание гостей