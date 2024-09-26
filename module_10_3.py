import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount_deposit = random.randint(50, 500)  # Генерация суммы пополнения баланса
            self.lock.acquire()  # Начальная блокировка баланса

            try:    # Для проверки и исключения "гонки" потоков
                self.balance += amount_deposit
                print(f'Пополнение на сумму: {amount_deposit}. Баланс: {self.balance} у.е.\n')
                if self.balance >= 500:  # Проверка баланса (необязательно)
                    pass
            finally:
                self.lock.release()  # Снятие блокировки баланса

            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            withdrawal_deposit = random.randint(50, 500)  # Генерация суммы снятия средств
            print(f'Запрос снятия средств на сумму {withdrawal_deposit}\n')
            self.lock.acquire()  # Начальная блокировка баланса

            try:    # Для проверки и исключения "гонки" потоков
                if withdrawal_deposit <= self.balance:
                    self.balance -= withdrawal_deposit
                    print(f'Снятие средств на сумму: {withdrawal_deposit}. Баланс: {self.balance} у.е.')
                else:
                    print('Запрос отклонён, недостаточно средств')
            finally:
                self.lock.release()  # Снятие блокировки баланса

            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают только self, никаких атрибутов нет,
# то в потоки следует передавать сам объект (экземпляр) класса Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance} у.е.')

