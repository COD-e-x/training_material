import json
from datetime import datetime


# Кастомный сериализатор для datetime
def datetime_converter(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError('Тип, не подлежащий сериализации')


# Данные с объектом datetime
data = {
    'name': 'Событие',
    'time': datetime.now()
}

# Запись данных в файл с использованием кастомного сериализатора
try:
    with open('data.json', 'w', encoding='utf-8') as file:
        # как только json.dumps дойдет, учитывая что формат даты не сериализуется автоматически,
        # программа зайдет в default для преобразования (с помощью пользовательской функции) формата даты в строку.
        json.dump(data, file, default=datetime_converter, indent=4, ensure_ascii=False)
    print("Данные успешно записаны в файл!")
except OSError as e:
    print(f'Путь к фалу указан неверно: {e}.')
except TypeError as e:
    print(f'Ошибка сериализации: {e}')


# Кастомный десериализатор для datetime
def datetime_parser(dct):
    if 'time' in dct:
        dct['time'] = datetime.strptime(dct['time'], '%Y-%m-%d %H:%M:%S')
    return dct


# Чтение данных из файла и десериализация
try:
    with open('data.json', 'r', encoding='utf-8') as file:
        # object_hook=datetime_parser - тут обратный процесс, когда необходим не строковый формат, а даты самой.
        loaded_data = json.load(file, object_hook=datetime_parser)
    print('Данные успешно загружены из файла!')
    print(loaded_data)
except FileNotFoundError as e:
    print(f'Файл не найден! {e}')
except json.JSONDecodeError as e:
    print(f'Ошибка в формате JSON! {e}')
