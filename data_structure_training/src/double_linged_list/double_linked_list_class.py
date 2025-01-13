class Node:

    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head  # работа с текущей головой
            self.head.prev_node = new_node  # работа с текущей головой
        self.head = new_node
        return f"Теперь в голове узел с данными {self.head.data}"

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        return f"Теперь в хвосте узел с данными {self.tail.data}"

    """Метод переписан: причина описано ниже."""
    def remove_from_head(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            removed_node = self.head
            self.head = self.tail = None
            return f"Были удалены данные {removed_node.data} из головы списка.\nТеперь список пустой."
        else:
            removed_node = self.head
            self.head = self.head.next_node
            self.head.prev_node = None
            return f"Были удалены данные {removed_node.data} из головы списка.\nТеперь голова списка {self.head.data}"

    """Логика вашего кода некорректно обрабатывает краевые случаи"""
    # def remove_from_head(self):
    #     removed_node = self.head
    #     self.head = self.head.next_node
    #     self.head.prev_node = None
    #     return f"Были удалены данные {removed_node.data} из головы списка.\nТеперь голова списка {self.head.data}"

    """Метод переписан: причина описано ниже."""
    def remove_from_tail(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            removed_node = self.head
            self.head = self.tail = None
            return f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь список пустой."
        else:
            removed_node = self.tail
            self.tail = self.tail.prev_node
            removed_node.prev_node = None
            self.tail.next_node = None
            return f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь хвост списка {self.tail.data}"

    """Логика вашего кода некорректно обрабатывает краевые случаи"""
    # def remove_from_tail(self):
    #     removed_node = self.tail
    #     self.tail = self.tail.prev_node
    #     self.tail.next_node = None
    #     return f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь хвост списка {self.tail.data}"

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        return "Список выведен с начала"


"""Так как методы у вас возвращают подробную информацию, решил реализовать так же."""
class DoubleLinkedList(LinkedList):
    """Класс для реализации двусвязного списка."""

    def __init__(self):
        """
        Инициализация двусвязного списка.
        В данной реализации полностью наследуется от родительского класса.
        """
        super().__init__()

    def print_ll_from_tail(self):
        """Выводит информацию по данным списка начиная с конца."""
        if self.head:
            current_node = self.tail
            while current_node:
                print(current_node.data)
                current_node = current_node.prev_node
            return 'Список выведен с конца.'
        return 'Список пустой.'

    def insert_at_index(self, data, index):
        """Добавляет узел по указанному индексу, заменяя при совпадении индекса."""
        new_node = Node(data)
        if index == 0:
            if self.head == self.tail:
                self.head = self.tail = new_node
            else:
                new_node.next_node = self.head.next_node
                self.head.next_node.prev_node = new_node
                self.head.next_node = None
                self.head = new_node
            return f'Данные "{data}" добавлены по индексу {index}.'
        current = self.head
        counter = 0
        # Реализация логики вне цикла, чтобы избежать лишних проверок
        while current and counter < index - 1:
            counter += 1
            current = current.next_node
        if not current or not current.next_node:
            return 'Индекс вне диапазона.'
        temp = current.next_node
        if current.next_node == self.tail:
            self.tail = new_node
        else:
            new_node.next_node = temp.next_node
            new_node.next_node.prev_node = new_node
        current.next_node = new_node
        new_node.prev_node = current
        temp.next_node = None
        temp.prev_node = None
        return f'Данные "{data}" добавлены по индексу {index}.'

    def remove_node_index(self, index):
        """Удаляет узел по индексу."""
        if not self.head:
            return 'Список пуст.'
        if index == 0:
            removed = self.head
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next_node
                self.head.prev_node = None
                removed.next_node = None
            return f'Данные "{removed.data}" удалены под индексом: {index}.'
        current = self.head
        counter = 0
        while current and counter < index - 1:
            counter += 1
            current = current.next_node
        if not current or not current.next_node:
            return 'Индекс вне диапазона.'
        removed = current.next_node
        if removed == self.tail:
            self.tail = current
            self.tail.next_node = None
        else:
            current.next_node = removed.next_node
            removed.next_node.prev_node = current
        removed.next_node = None
        removed.prev_node = None
        return f'Данные "{removed.data}" удалены под индексом: {index}.'

    def remove_node_data(self, rm_data):
        """Удаляет узел по данным."""
        if not self.head:
            return 'Список пуст.'
        if self.head.data == rm_data:
            removed = self.head
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next_node
                self.head.prev_node = None
                removed.next_node = None
            return f'Данные "{removed.data}" удалены.'
        current = self.head
        # Много вариантов перепробовал, получилось только в цикле реализовать.
        while current.next_node:
            if current.next_node.data == rm_data:
                removed = current.next_node
                if removed.data == self.tail.data:
                    self.tail = current
                    self.tail.next_node = None
                else:
                    current.next_node = removed.next_node
                    removed.next_node.prev_node = current
                removed.next_node = None
                removed.prev_node = None
                return f'Данные "{removed.data}" удалены.'
            current = current.next_node
        return f'Данные "{rm_data}" в списке не найдены.'

    def len_ll(self):
        """Выводит длину списка."""
        if self.head:
            current = self.head
            counter = 0
            while current:
                counter += 1
                current = current.next_node
            return f'Длина списка: {counter}.'
        return 'Список пуст.'

    # Раз нет уточнения по выводу в данной и последующей реализации: код возвращает - True или False
    def contains_from_head(self, data):
        """Проверка на содержание элемента, начиная с головы (head)."""
        if self.head:
            current = self.head
            while current:
                if current.data == data:
                    return f'Данные найдены: "{current.data}".'
                current = current.next_node
        return 'Данные не найдены.'

    def contains_from_tail(self, data):
        """Проверка на содержание элемента, начиная с хвоста (tail)."""
        if self.tail:
            current = self.tail
            while current:
                if current.data == data:
                    return f'Данные найдены: "{current.data}".'
                current = current.prev_node
        return 'Данные не найдены.'

    def contains_from(self, data, choice_direction):
        """Проверка содержания элемента по выбору направления head / tail."""
        if choice_direction == 'head':
            return self.contains_from_head(data)
        elif choice_direction == 'tail':
            return self.contains_from_tail(data)
        else:
            return 'Неправильное направление, выберите "head" или "tail".'

if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insert_at_head('data - index 5')
    dll.insert_at_head('data - index 4')
    dll.insert_at_head('data - index 3')
    dll.insert_at_head('data - index 2')
    dll.insert_at_head('data - index 1')
    dll.insert_at_head('data - index 0')
    print()

    # insert_at_index()
    # print(dll.insert_at_index('test data - index: 0', 0))
    # print(dll.insert_at_index('test data - index: 3', 3))
    # print(dll.insert_at_index('test data - index: 5', 5))
    # print(dll.insert_at_index('test data - index: 5', 6))

    # remove_node_index()
    # print(dll.remove_node_index(0))
    # print(dll.remove_node_index(3))
    # print(dll.remove_node_index(5))

    # remove_node_data()
    # print(dll.remove_node_data('index 5'))

    # len_ll()
    print(dll.len_ll())

    # contains_from_head
    # print(dll.contains_from_head('index 0'))
    # print(dll.contains_from_head('index 3'))
    # print(dll.contains_from_head('index 5'))
    # print(dll.contains_from_head('index 234'))

    # contains_from_tail
    # print(dll.contains_from_tail('index 0'))
    # print(dll.contains_from_tail('index 3'))
    # print(dll.contains_from_tail('index 5'))
    # print(dll.contains_from_head('index 234'))


    # contains_from
    # print(dll.contains_from('data - index 0', 'head'))
    # print(dll.contains_from('data - index 5', 'tail'))
    # print(dll.contains_from('data - index 123', 'tail'))

    print()
    print(dll.print_ll_from_head())
    print()
    print()
    # print_ll_from_tail()
    print(dll.print_ll_from_tail())