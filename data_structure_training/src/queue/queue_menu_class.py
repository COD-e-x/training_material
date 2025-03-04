"""
В реализации вместо метода show() класса QueueСlass,
реализовал для ознакомления магические методы __iter__(), __next__().
"""


class QueueMenu:
    """Класс для реализации меню очереди."""

    def __init__(self, queue_obj):
        """Инициализирует меню класса очереди."""
        self.__queue = queue_obj

    def display_menu(self):
        """Отображает меню для пользователя."""
        print('\n--- Меню ---')
        print('0. Для повторного вывода меню')
        print('1. Добавить элемент в очередь')
        print('2. Удалить элемент из очереди')
        print('3. Показать очередь')
        print('4. Проверить, пуста ли очередь')
        print('5. Проверить, полна ли очередь')
        print('6. Выйти')

    def process_choice(self, choice):
        """Обрабатывает выбор пользователя."""
        if choice == 0:
            self.display_menu()
        elif choice == 1:
            self.add_item_queue()
        elif choice == 2:
            self.remove_item_queue()
        elif choice == 3:
            self.show_queue()
        elif choice == 4:
            self.is_empty_queue()
        elif choice == 5:
            self.is_full_queue()
        elif choice == 6:
            self.exit_program()
        else:
            print('Неверный выбор, попробуйте снова.')

    def add_item_queue(self):
        """Добавление элемента в очередь."""
        if not self.__queue.is_full():
            add_data = input('Введите данные для добавления в очередь: ')
            if add_data:
                self.__queue.enqueue(add_data)
                print('Данные добавлены.')
            else:
                print('Данные не переданы (пустая строка)!')
        else:
            print('Очередь заполнена.')

    def remove_item_queue(self):
        """Удаление элемента из очереди."""
        remove_data = self.__queue.dequeue()
        if remove_data:
            print(f'Удалены данные: {remove_data}.')
        else:
            print('Очередь пуста.')

    def show_queue(self):
        """Выводит все элементы очереди в списке."""
        if self.__queue.is_empty():
            print('Список данных в очереди:')
            print(list(self.__queue))
        else:
            print('Очередь пуста.')

    def is_empty_queue(self):
        """Проверка, пуста ли очередь."""
        print('Очередь не пуста.' if self.__queue.is_empty() else 'Очередь пуста.')

    def is_full_queue(self):
        """Проверка, полная ли очередь."""
        print('Очередь заполнена.' if self.__queue.is_full() else 'Очередь не заполнена.')

    @staticmethod
    def exit_program():
        """Завершает работу программы"""
        print('Программа завершена!')
        exit(0)
