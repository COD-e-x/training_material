from threading import Thread, Lock, Event, current_thread
import threading
import time

print_lock = Lock()
print_enumerate = Event()


def find_max_or_min(numbers, find_max=True):
    """
    Ищет и выводит поочередно максимальное или минимальное числа из списка,
    удаляя само число из списка после вывода.

    :param numbers: Список чисел.
    :param find_max: Если True ищет максимальные числа, иначе минимальные.
    # """
    if len(numbers) < 1:
        return print('Ошибка. Ведите хотя бы одно число.')
    new_numbers = list(numbers)
    range_count = min(len(new_numbers), 5)
    print_enumerate.wait()
    for i in range(range_count):
        num = max(new_numbers) if find_max else min(new_numbers)
        with print_lock:
            print(f'max: {num}') if find_max else print(f'min: {num}')
            time.sleep(1)
        new_numbers.remove(num)
    with print_lock:
        print(f'Поток ({current_thread().name}) завершил свою работу.')


if __name__ == '__main__':
    text = 'Введите числа через пробел (например: 34 2 234 21 45 ...): '

    values_list = list(map(int, input(text).split())) or [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    max_thr = Thread(target=find_max_or_min, args=(values_list, True), name='max thr')
    min_thr = Thread(target=find_max_or_min, args=(values_list, False), name='min thr')

    max_thr.start()
    min_thr.start()

    # Изначально выводит количество и список активных потоков
    print_enumerate.set()
    with print_lock:
        print(f'active thread: {threading.active_count()},  enumerate: {threading.enumerate()}')

    max_thr.join()
    min_thr.join()
