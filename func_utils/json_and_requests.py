import json
import requests

def get_operations_url(url):
    """Получает данные с указанного URL. Обрабатывает ошибки"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), 'INFO: Данные получены успешно!\n'
        return None, f'INFO: Ошибка status_code {response.status_code}\n'
    except requests.exceptions.ConnectionError:
        return None, 'INFO: Ошибка status_code requests.exceptions.ConnectionError'
    except json.JSONDecodeError:
        return None, 'INFO: Ошибка status_code json.JSONDecodeError'

import json


def read_json(filename):
    """Чтение данных из JSON файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not data:
                return []
            return data
    except FileNotFoundError as e:
        return f'Файл {filename} не найден. Ошибка {e}'
    except json.JSONDecodeError as e:
        return f'Ошибка декодирования JSON в файле {filename}'


def write_json(filename, data):
    """Запись данных в JSON файл по указанному адресу"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except OSError:
        return f'Ошибка при открытии или записи в файл {filename}.'
    except Exception as e:
        return f'Произошла ошибка: {e}'

