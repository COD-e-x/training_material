from threading import Thread, BoundedSemaphore, currentThread
import time
import random

"""
Semaphore (Семафор): Это механизм синхронизации, который используется для управления 
    доступом к ограниченным ресурсам в многозадачной среде.
Barrier  (Барьер): Это механизм синхронизации, который заставляет потоки ожидать друг друга до тех пор, 
    пока все они не достигнут определенной точки. 
"""

max_connections = 5
pool = BoundedSemaphore(value=max_connections)


def my_test():
    while True:
        """
        Запись with (ниже), эквивалентна:
        
        pool.acquire()  # захват ресурса
        try:
            # КОД
            print(currentThread().name)
            time.sleep(2)
        finally:
            pool.release()  # освобождение ресурса
                
        """
        with pool:  # с помощью with, семафор будет захвачен и освобожден автоматически
            slp = random.randint(1, 5)
            # Печатаем информацию о потоке и времени сна
            print(f'{currentThread().name} - захватил семафор, будет спать ({slp} секунд)')
            time.sleep(slp)
            print(f'{currentThread().name} - освободил семафор после сна ({slp} секунд)')


# Запускаем потоки
for i in range(10):
    Thread(target=my_test, name=f'thr-{i}').start()
