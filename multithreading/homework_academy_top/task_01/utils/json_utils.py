import json


def write_json(filename, data):
    """Запись данных в JSON файл по указанному адресу"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        return f'Данные успешно записаны в файл {filename}.'
    except OSError:
        return f'Ошибка при открытии или записи в файл {filename}.'
    except Exception as e:
        return f'Произошла ошибка: {e}'


def read_json(filename):
    """Чтение данных из JSON файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not data:
                return 'Файл пустой.'
            return data
    except FileNotFoundError as e:
        return f'Файл {filename} не найден. Ошибка {e}'
    except json.JSONDecodeError as e:
        return f'Ошибка декодирования JSON в файле {filename}'
