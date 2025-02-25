import json
from json import JSONEncoder, JSONDecodeError


class Car:
    data_car = {}

    def __init__(self, reg_numbers, sunroof=False, radio=False):
        self.reg_numbers = reg_numbers
        self.sunroof = sunroof
        self.radio = radio
        Car.data_car = {}

    def change_reg_number(self, new_reg_numbers):
        self.reg_numbers = new_reg_numbers

    def radio_on(self):
        if not self.radio:
            self.radio = True


class CarEncoder(JSONEncoder):
    @classmethod
    def default(cls, obj):
        if isinstance(obj, Car):
            return {
                'reg_number': obj.reg_numbers,
                'sunroof': obj.sunroof,
                'radio': obj.radio,
                'methods': [method for method in dir(obj) if
                            callable(getattr(obj, method)) and not method.startswith('__')]
            }
        return super().default(obj)


if __name__ == '__main__':
    car = Car('oo100o rus', True, True)

    try:
        with open(r'data_car.json', 'w', encoding='utf-8') as fh:
            json.dump(car, fh, cls=CarEncoder, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f'Указан неверный путь к файлу. {e}')

    try:
        with open(r'data_car.json', 'r', encoding='utf-8') as fh:
            data_json = json.load(fh)
    except FileNotFoundError:
        print(f'Файл {r'data_car.json'} не найден!')
    except JSONDecodeError as e:
        print(f'Ошибка в формате JSON! {e}')

    print(data_json)
