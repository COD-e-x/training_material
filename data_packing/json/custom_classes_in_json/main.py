from dataclasses import dataclass
import json


class InvalidFormatError(Exception):
    """Исключение для ошибок неверного формата."""
    pass


@dataclass
class Product:
    """Представляет продукт с названием и ценой."""
    name: str
    price: float


class ManagerProduct:
    """Управляет коллекцией продуктов."""

    def __init__(self):
        """Инициализирует списком продуктов."""
        self.products = []

    def add_product(self, name: str, price: (int, float)):
        """
        Добавляет новый продукт в коллекцию, проверяя типы данных для
        имени и цены продукта.

        Параметры:
            name (str): Название продукта.
            price (float): Цена продукта.

        Исключения:
            TypeError: Если name не является строкой или price не является числом с плавающей запятой.
        """
        if not isinstance(name, str):
            raise InvalidFormatError('Ошибка: название продукта должно быть строкой.')
        if not isinstance(price, (int, float)):
            raise InvalidFormatError('Ошибка: цена продукта должна быть числом.')
        self.products.append(Product(name, price))

    def remove_product(self, name):
        """Удаляет продукт из списка по названию."""
        for product in self.products:
            if name.lower() == product.name.lower():
                self.products.pop(self.products.index(product))
                return True
        return False

    def calculate_total_price(self):
        """Вычисляет и возвращает общую стоимость всех продуктов."""
        total_price = 0
        for product in self.products:
            total_price += product.price
        return total_price

    def filter_by_price(self, min_price=0, max_price=float('inf')):
        """Фильтрует продукты по заданному диапазону цен и возвращает совпадающие продукты."""
        filtered_products = [product for product in self.products if min_price <= product.price <= max_price]
        return filtered_products

    def sort_product(self, by='price', reverse=False):
        """Сортирует продукты по указанному атрибуту (name или price)."""
        if by == 'price':
            self.products.sort(key=lambda product: product.price, reverse=reverse)
        elif by == 'name':
            self.products.sort(key=lambda product: product.name, reverse=reverse)
        else:
            raise InvalidFormatError('Ошибка: Неверный формат, ведите "price" или "name"')

    def search_by_name(self, name):
        """Ищет продукты по названию."""
        search_result = [product for product in self.products if name.lower() in product.name.lower()]
        return search_result

    def update_product(self, name, new_data, change='price'):
        """Обновляет информацию о продукте (name или price) для указанного продукта."""
        for product in self.products:
            if change == 'price':
                if product.name.lower() == name.lower():
                    product.price = new_data
            elif change == 'name':
                if product.name.lower() == name.lower():
                    product.name = new_data
            return True
        return False

    def save_to_json(self, filename):
        """Сохраняет список продуктов и общую стоимость в JSON файл."""
        product_data = [{'name': product.name, 'price': product.price} for product in self.products]
        product_data.append({'total_price': self.calculate_total_price()})
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(product_data, file, indent=4, ensure_ascii=False)
        except OSError as e:
            return print(f'Указан неверный путь к файлу. {e}')

    def load_to_json(self, filename):
        """Загружает данные продуктов из JSON файла в список продуктов."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                product_data = json.load(file)
                self.products = [Product(item['name'], item['price']) for item in product_data if 'name' in item]
        except FileNotFoundError as e:
            print(f'Файл не найден! {e}')
        except json.JSONDecodeError as e:
            print(f'Ошибка в формате JSON! {e}')

    def __str__(self):
        return (f'Продукты: '
                f'{''.join(f'\nПродукт: {product.name}, стоимость: {product.price}' for product in self.products)}')

    def __repr__(self):
        return repr(self.products)


if __name__ == '__main__':
    manager = ManagerProduct()
    manager.add_product('Tablet', 300)
    manager.add_product('Laptop', 1000)
    manager.add_product('Smartphone', 500)
    manager.remove_product('Smartphone')
    print(repr(manager))
    print(manager)

    # print()
    # # manager.sort_product('price')
    # manager.sort_product('name')
    # manager.save_to_json(r'./products.json')
    # manager.load_to_json(r'./products.json')
    #
    # print()
    # print(manager.products)
    # print(manager.search_by_name('laptop'))
    # manager.update_product('laptop', '800')
    # print(manager.search_by_name('laptop'))
    # manager.remove_product('laptop')
    # print(manager.products)
    # manager.save_to_json(r'./products.json')
    #
    # print()
    # for p in manager.products:
    #     print(f'{p.name}: {p.price}')
    #
    # print('Общая стоимость:', manager.calculate_total_price(), 'руб.')
