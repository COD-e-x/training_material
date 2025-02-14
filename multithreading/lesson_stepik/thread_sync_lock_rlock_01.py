import time
import threading

value = 0
locker = threading.Lock()  # Объект синхронизации потоков.


def inc_value():
    global value
    while True:
        with locker:  # Блокирует доступ к переменной value для других потоков.
            # locker.acquire() # Захватывает блокировку, чтобы гарантировать, что только один поток получит доступ к коду ниже.
            value += 1
            print(value)
            time.sleep(1)


#         locker.release() # Освобождает блокировку, позволяя другим потокам получить доступ к коду.

for _ in range(5):
    threading.Thread(target=inc_value).start()  # Создает 5 потоков, каждый из которых выполняет функцию inc_value.
