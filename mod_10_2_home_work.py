#--------------- H O M E  W O R K  (M O D U L E _ 10 _ 2) ---------------

import threading
import time

class Knight (threading.Thread):
    def __init__(self, name, power):   #что нам нужно передавать
        super().__init__()
        self.name = name
        self.power = power          #не нужно передавать
        self.enemies = 100           #враги
        self.days = 0
        self.victory = False

    def run(self):
        print(f'{self.name}, на нас напали!')

        while self.enemies > 0:
            time.sleep(1)         # 1 сек = 1 день
            self.days += 1
            self.enemies -= self.power

            if self.enemies < 0:
                self.enemies = 0

            print(f'{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.')

        self.victory = True
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились')