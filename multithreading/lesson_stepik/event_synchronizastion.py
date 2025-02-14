import threading
import time

# Функция для потока, который ожидает события
def worker(event):
    print('Поток ожидает события...')
    event.wait()  # Ожидает, пока событие не будет установлено
    print('Поток продолжает выполнение после получения события!')

# Создаем объект Event
event = threading.Event()

# Создаем несколько потоков, которые будут ожидать события
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(event,))
    t.start()
    threads.append(t)

# Пауза перед установкой события
time.sleep(2)

# Устанавливаем событие, чтобы потоки продолжили выполнение
print('Устанавливаю событие...')
event.set()

# Ждем завершения всех потоков
for t in threads:
    t.join()

print('Все потоки завершили работу.')
