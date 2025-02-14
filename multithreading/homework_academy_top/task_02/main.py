from threading import Thread, Lock, Event, current_thread

min_event = Event()
print_lock = Lock()


# В этом и следующем задании решение противоречит принципу SRP.
# Просто когда код писал они настолько были похожи, что решил реализовать так, для практики.
# Так как прошлое выполнение было в разных функциях, хотел посмотреть на эту.

def find_max_or_min(numbers, find_max=True):
    """
    Ищет и выводит максимальные или минимальные числа из списка, удаляя число из списка после вывода.

    :param numbers: Список чисел.
    :param find_max: Если True ищет максимальные числа, иначе минимальные.
    """
    if len(numbers) < 1:
        return print('Ошибка. Ведите хотя бы одно число.')
    new_numbers = list(numbers)
    range_count = 0
    if 1 <= len(new_numbers) < 5:
        range_count = len(new_numbers)
    elif len(new_numbers) >= 5:
        range_count = 5
    for i in range(range_count):
        if find_max:
            num = max(new_numbers)
            with print_lock:
                print(f'max: {num}')
        else:
            num = min(new_numbers)
            with print_lock:
                print(f'min: {num}')
        new_numbers.remove(num)
    with print_lock:
        print(f'Поток ({current_thread().name}) завершил свою работу.')
    min_event.set()


if __name__ == '__main__':
    text = 'Введите числа через пробел (например: 34 2 234 21 45 ...): '
    values_list = list(map(int, input(text).split())) or [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    max_thr = Thread(target=find_max_or_min, args=(values_list, True), name='max thr')
    min_thr = Thread(target=find_max_or_min, args=(values_list, False), name='min thr')

    max_thr.start()
    min_thr.start()

    max_thr.join()
    min_event.wait()
    min_thr.join()
