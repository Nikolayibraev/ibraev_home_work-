import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):              # ПОПОЛНЕНИЕ СЧЁТА
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:                                # Блок доступ
                self.balance += amount
                print(f'Пополнение: {amount}. Баланс: {self.balance}')
                if self.balance >= 500 and not self.lock.locked(): #Если бланс < 500 => разблок
                    self.lock.release()
            time.sleep(0.001)

    def take(self):              # СНЯТИЕ
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Снятие: {amount}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
                    self.lock.acquire()  # Блокируем поток если недостаточно средств
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')