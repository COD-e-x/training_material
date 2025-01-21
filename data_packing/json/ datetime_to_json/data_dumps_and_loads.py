import json
from datetime import datetime


# Кастомный сериализатор
def datetime_converter(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError('Тип, не подлежащий сериализации')


# Создаем объект datetime
current_time = datetime.now()

# Создаем словарь с datetime
data = {
    'name': 'Событие',
    'time': current_time
}

# Сериализация с использованием кастомного сериализатора
json_data = json.dumps(data, indent=4, default=datetime_converter)
print(json_data)

# Пример строки из JSON
json_data = '{"name": "Событие", "time": "2025-01-16 15:30:00"}'

# Десериализация
data = json.loads(json_data)

# Преобразование строки обратно в datetime
event_time = datetime.strptime(data['time'], '%Y-%m-%d %H:%M:%S')

print()
print(f'name - {data['name']}\ntime - {event_time}')
