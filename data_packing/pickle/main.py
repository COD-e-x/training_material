import pickle


class Node:
    """Класс для представления узла двусвязного списка"""

    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DoublyLinkedList:
    """Класс для двусвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        """Вставка узла в начало списка."""
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        """Вставка узла в конец списка."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node

    def print_ll_from_head(self):
        """Вывод элементов списка в терминал, начиная от головы"""
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next_node

    def print_ll_from_tail(self):
        """Вывод элементов списка в терминал начиная от хвоста"""
        node = self.tail
        while node is not None:
            print(node.data)
            node = node.prev_node

    def __iter__(self):
        """Итератор для обхода элементов от головы"""
        self.current_node = self.head
        return self

    # def __next__(self):
    #     """Получение следующего элемента в списке"""
    #     if self.current_node:
    #         data = self.current_node.data
    #         self.current_node = self.current_node.next_node
    #         return data
    #     raise StopIteration


if __name__ == '__main__':
    # Создаем объект двусвязного списка
    box_list = DoublyLinkedList()

    # Добавляем элементы в начало и конец списка
    box_list.insert_at_head('Барсик_1')
    box_list.insert_at_head('Снежок_0')
    box_list.insert_at_tail('Персик_2')

    # # Преобразуем список в обычный список и выводим первый элемент, проверка работы __iter__
    # x = list(box_list)
    # print(x[0])

    # # Сериализация списка с помощью pickle
    # box_list = pickle.dumps(box_list)
    # print(box_list)
    # box_list = pickle.loads(box_list)
    # box_list.print_ll_from_head()
    # print()

    # # Сохранение сериализованного списка в файл
    # try:
    #     with open(r'./box_pickled.cats', 'wb') as fp:
    #         pickle.dump(box_list, fp)
    # except OSError as e:
    #     print(f'Указан неверный путь к файлу: {e}')

    # # Чтение сериализованного списка из файла
    # try:
    #     with open(r'./box_pickled.cats', 'rb') as fp:
    #         box_list_from_file = pickle.load(fp)
    # except FileNotFoundError as e:
    #     print(f'Файл не найден: {e}')

    # # Печать объекта после десериализации
    # print(box_list_from_file)

    # # Печать списка с хвоста
    # box_list.print_ll_from_tail()
