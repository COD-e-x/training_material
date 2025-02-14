import time
import threading


def get_data(data):
    while True:
        print(f'[{threading.current_thread().name}] = {data}')
        time.sleep(1)


print('Запуск основного патока (поток запуска самого файла)')

thr = threading.Thread(target=get_data, args=(str(time.time()),))
thr.setDaemon(True)  # Делаем дополнительный поток демоном.
thr.start()  # Запускаем дополнительный поток.

time.sleep(1)  # Основной поток спит секунду.

print('Завершение основного потока.')
# После того как основной поток завершится, демон-поток тоже завершится автоматически,
# поскольку он не может существовать без основного потока.
