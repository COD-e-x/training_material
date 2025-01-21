import json

information_book_dict = {
    'name': 'book_name',
    'autor': 'autor_name',
    'publication': 1975,
    'genre': 'movie',
}

with open(r'./data_book.json', 'w', encoding='utf-8') as file:
    json.dump(information_book_dict, file, indent=4, ensure_ascii=False)

try:
    with open(r'./data_book.json', 'r', encoding='utf-8') as file:
        data_book = json.load(file)
except FileNotFoundError as e:
    print(f'Файл не найден! {e}')
except json.JSONDecodeError as e:
    print(f'Ошибка в формате JSON! {e}')

print(data_book)

data_book['rating'] = [1, 2, 3, 4, 5]

with open(r'./data_book.json', 'w', encoding='utf-8') as file:
    json.dump(data_book, file, indent=4, ensure_ascii=False)

try:
    with open(r'./data_book.json', 'r', encoding='utf-8') as file:
        updated_data_book = json.load(file)
except FileNotFoundError as e:
    print(f'Файл не найден! {e}')
except json.JSONDecodeError as e:
    print(f'Ошибка в формате JSON! {e}')

print(updated_data_book)
