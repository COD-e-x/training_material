from threading import Thread, Barrier, currentThread
import random
import time

start_time = time.time()


def my_test(barrier):
    slp = random.randint(10, 15)
    print(f'Поток [{currentThread().name}] запущен в {time.ctime()}. Будет спать {slp} секунд.')
    time.sleep(slp)
    barrier.wait()
    elapsed_time = time.time() - start_time
    print(f'Поток [{currentThread().name}] преодолел барьер. Время от старта: {elapsed_time:.2f} секунд.')


bar = Barrier(5)  # Устанавливаем барьер на 5 потоков
for i in range(5):
    Thread(target=my_test, args=(bar,), name=f'thr-{i}').start()
