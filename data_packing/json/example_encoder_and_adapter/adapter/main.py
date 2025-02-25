from json import JSONDecodeError
import json


class Stadium:
    def __init__(self, name, location, seats):
        self.name = name
        self.location = location
        self.seats = seats

    def update_capacity(self, new_seats):
        """Обновляет вместимость стадиона."""
        self.seats = new_seats

    def display_info(self):
        """Возвращает информацию о стадионе."""
        return f'Стадион "{self.name}", локация {self.location}, вместимость: {self.seats} зрителей'


class StadiumAdapter:

    @staticmethod
    def to_dict(obj):
        if isinstance(obj, Stadium):
            return {
                'reg_numbers': obj.name,
                'sunroof': obj.location,
                'radio': obj.seats,
                'methods': [method for method in dir(obj) if
                            callable(getattr(obj, method)) and not method.startswith('__')]
            }


if __name__ == '__main__':
    stadium = Stadium('ЦСК', 'Москва', 15000)

    try:
        with open(r'stadium_data.json', 'w', encoding='utf-8') as fh:
            json.dump(StadiumAdapter.to_dict(stadium), fh, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f'Указан неверный путь к файлу. {e}')

    try:
        with open(r'stadium_data.json', 'r', encoding='utf-8') as fh:
            data_json = json.load(fh)
    except FileNotFoundError:
        print(f'Файл {r'stadium_data.json'} не найден!')
    except JSONDecodeError as e:
        print(f'Ошибка в формате JSON! {e}')

    print(data_json)
