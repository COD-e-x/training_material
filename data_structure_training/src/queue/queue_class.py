class Node:
    """Клас для реализации Узла."""

    def __init__(self, data):
        """Инициализация узла."""
        self.data = data
        self.next_node = None


class Queue:
    """Класс для реализации очереди."""

    def __init__(self, size=5):
        """Инициализация очереди."""
        self.__size = size
        self.__head = None
        self.__tail = None
        self.__current_size = 0

    def enqueue(self, data):
        """Добавляет элемент в очередь."""
        if self.__current_size < self.__size:
            new_node = Node(data)
            if not self.__tail:
                self.__head = new_node
            else:
                self.__tail.next_node = new_node
            self.__tail = new_node
            self.__current_size += 1
            return f'Данные ({data}) занесены в очередь.'
        else:
            return 'Очередь заполнена.'

    def dequeue(self):
        """Удаляет элемент из очереди."""
        if self.__head:
            if not self.__head.next_node:
                self.__tail = None
            remove_node = self.__head
            self.__head = self.__head.next_node
            remove_node.next_node = None
            self.__current_size -= 1
            return remove_node.data
        return 'Очередь пустая.'

    def is_empty(self):
        """Проверка, пуста ли очередь."""
        return self.__head

    def is_full(self):
        """Проверка, заполнена ли очередь."""
        return self.__current_size == self.__size

    def show(self):
        """Выводит все элементы очереди."""
        current_node = self.__head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def __iter__(self):
        """Делаем очередь итерируемой."""
        self.current_node = self.__head
        return self

    def __next__(self):
        """Возвращает следующий элемент очереди."""
        if self.current_node:
            data = self.current_node.data
            self.current_node = self.current_node.next_node
            return data
        raise StopIteration
