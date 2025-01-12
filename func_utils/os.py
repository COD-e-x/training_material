import os

def check_file(filename):
    """`Проверка существования `и содержимого файла"""
    if os.path.exists(filename):
        if os.path.getsize(filename) > 0:
            raise ValueError('Ошибка: Файл уже существует и не пустой.')
    return filename

def check_directory(filename):
    """Проверка существования директории"""
    if not os.path.exists(os.path.dirname(filename)) and os.path.dirname(filename) != '':
            raise ValueError('Ошибка: Директория для файла не существует.')
    return filename