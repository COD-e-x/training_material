import json

employee = {
    'name': 'Larry',
    'age': 25,
    'position': 'programmer',
    'list_skills': ['Python', 'Django'],
}

try:
    with open(r'./data_employee.json', 'w', encoding='utf-8') as file:
        json.dump([employee], file, indent=4, ensure_ascii=False)
except OSError as e:
    print(f'Указан неверный путь к файлу. {e}')

try:
    with open(r'./data_employee.json', 'r', encoding='utf-8') as file:
        data_employee = json.load(file)
except FileNotFoundError as e:
    print(f'Файл не найден! {e}')
except json.JSONDecodeError as e:
    print(f'Ошибка в формате JSON! {e}')

print('Данные до добавления нового сотрудника:')
print(data_employee)

new_employee = {
    'name': 'Anna',
    'age': 28,
    'position': 'designer',
    'list_skills': ['Photoshop', 'Illustrator'],
}

data_employee.append(new_employee)

try:
    with open(r'./data_employee.json', 'w', encoding='utf-8') as file:
        json.dump(data_employee, file, indent=4, ensure_ascii=False)
except OSError as e:
    print(f'Указан неверный путь к файлу. {e}')

print('Данные после добавления нового сотрудника:')
print(data_employee)
