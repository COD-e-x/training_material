class Node:
    """Класс для узла стека."""

    def __init__(self, data, next_node=None):
        """Инициализация стека."""
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для реализации стека."""

    def __init__(self, stack_size=5, top=None):
        """Инициализация стека."""
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        """Добавление элемента в стек."""
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            print("Стек переполнен")
            return "Стек переполнен"

    def pop(self):
        """Удаление элемента из стека."""
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стек пуст"

    def is_empty(self):
        """Проверяет, пуст ли стек."""
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        """Проверяет, заполнен ли стек."""
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        """Очищает стек"""
        while self.top:
            self.pop()

    def get_data(self, index):
        """Возвращает данные по индексу."""
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        """Возвращает размер стека."""
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        """Подсчитывает количество целых чисел в стеке."""
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


# stack = Stack()
# stack.push(1)
# stack.push("sta")
# stack.push(2)
# stack.push(2.5)
# stack.push("sta")
# print(stack.counter_int())