class Node:
    """Класс, представляющий узел очереди."""

    def __init__(self, data):
        """Инициализирует узел с заданными данными и ссылкой на следующий узел."""
        self.data = data
        self.next_node = None

class Queue:
    """Класс для реализации очереди."""

    def __init__(self, size=5):
        """Инициализирует очередь с заданным максимальным размером.

        Атрибуты:
            head = для работы с первым узлом
            tail = для работы с последним узлом
            current_size = для подсчета количества корректных узлов
        """
        self.size = size
        self.head = None
        self.tail = None
        self.current_size = 0

    def enqueue(self, data):
        """Добавление элемента в очередь."""
        if self.current_size < self.size:
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next_node = new_node
                self.tail = new_node
            self.current_size += 1
        else:
            return None

    def dequeue(self):
        """Удаление элемента из очереди."""
        if self.head:
            remove_node = self.head
            self.head = self.head.next_node
            self.current_size -= 1
            return remove_node.data
        return None

    def is_empty(self):
        """Проверка, пуста ли очередь."""
        return False if self.head else True

    def is_full(self):
        """Проверка, полная ли очередь."""
        return True if self.current_size == self.size else False

    def show(self):
        """Выводит все элементы очереди."""
        current_node = self.head
        if not current_node:
            return print('Очередь пуста.')
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def __iter__(self):
        """Делаем очередь итерируемой."""
        self.current_node = self.head
        return self

    def __next__(self):
        """Возвращает следующий элемент очереди."""
        if self.current_node:
            data = self.current_node.data
            self.current_node = self.current_node.next_node
            return data
        raise StopIteration