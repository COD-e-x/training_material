from threading import Event, current_thread
import threading
import random
import time
from multithreading.homework_academy_top.task_01.utils.json_utils import write_json, read_json
from multithreading.homework_academy_top.task_01.utils.time_utils import get_formatted_current_time

print_lock = threading.Lock()
file_lock = threading.Lock()
primes_done = Event()

PATH_NUMBERS = 'data/numbers.json'
PATH_PRIMES = 'data/primes.json'
PATH_FACTORIAL = 'data/factorial.json'


def generate_numbers(filename):
    """Генерирует случайные числа от 1 до 10 и записывает их в файл."""
    start_time = time.time()
    # Случайные числа выбрал от 1 до 10, что бы облегчить проверку. Задача основана на теме - многопоточность.
    numbers = [random.randint(1, 10) for _ in range(11)]
    # Понятно что файлы разные и порядок записи,
    # но мне кажется я пока не все понял, поэтому использовал Lock() во всех случаях записи в файл.
    with file_lock:
        write_json(filename, {'numbers': numbers})
    end_time = time.time()
    with print_lock:
        print(f'[{get_formatted_current_time()}] Поток ({current_thread().name}). '
              f'Генерация чисел завершена за {end_time - start_time:.5f} секунд.')
    return f'Рандомные числа записаны в файл - {filename}.'


def find_primes(r_filename, w_filename):
    """Ищет простые числа из списка, считанного из файла, и записывает их в другой файл."""
    start_time = time.time()
    data = read_json(r_filename)
    numbers_list = data['numbers']
    prime_list = []
    for i in numbers_list:
        if i <= 1:
            continue
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    with file_lock:
        write_json(w_filename, {'primes': prime_list})
    end_time = time.time()
    with print_lock:
        print(
            f'[{get_formatted_current_time()}] Поток ({current_thread().name}). Поиск простых чисел завершен за '
            f'{end_time - start_time:.5f} секунд. Найдено простых чисел: {len(prime_list)}. ')
    primes_done.set()
    return f'Простые числа записаны в файл - {w_filename}.'


def calculate_factorial(r_filename, w_filename):
    """
    Вычисляет факториалы чисел, считанных из файла, и записывает результат в другой файл.
    Ожидает завершения поиска простых чисел перед выполнением.
    """
    start_time = time.time()
    primes_done.wait()
    data = read_json(r_filename)
    numbers_list = data['numbers']
    factorial_list = []
    for i in numbers_list:
        if i <= 0:
            factorial_list.append(1)
        else:
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            factorial_list.append(factorial)
    with file_lock:
        write_json(w_filename, {'factorial': factorial_list})
    end_time = time.time()
    with print_lock:
        print(
            f'[{get_formatted_current_time()}] Поток ({current_thread().name}). Расчет факториалов завершен за '
            f'{end_time - start_time:.5f} секунд. Факториалов посчитано: {len(factorial_list)}. ')
    return f'Факториал каждого числа из списка, записаны в файл - {w_filename}.'


if __name__ == '__main__':
    random_thr = threading.Thread(target=generate_numbers, args=(PATH_NUMBERS,), name='random thr')
    random_thr.start()
    random_thr.join()

    primes_thr = threading.Thread(target=find_primes, args=(PATH_NUMBERS, PATH_PRIMES), name='primes thr')
    factorial_thr = threading.Thread(target=calculate_factorial, args=(PATH_NUMBERS, PATH_FACTORIAL),
                                     name='factorial thr')

    primes_thr.start()
    factorial_thr.start()

    primes_thr.join()
    factorial_thr.join()
