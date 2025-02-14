import threading

locker = threading.Lock()


def inc_value():
    print('Блокирует поток.')
    locker.acquire()
    print('Поток разблокирован.')


thr_01 = threading.Thread(target=inc_value)
thr_01.start()
thr_02 = threading.Thread(target=inc_value)
thr_02.start()
thr_03 = threading.Thread(target=inc_value)
thr_03.start()
