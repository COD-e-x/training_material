class Node:
    """Класс для узла стека."""

    def __init__(self, data, next_node=True):
        """Инициализация узла."""
        self.data = data
        self.next_node = next_node


class Steck:
    """Класс для реализации стека."""

    def __init__(self, stack_size=5, top=None):
        """Инициализация стека."""
        self.stack_size = stack_size
        self.top = top

    def push(self, data):
        """Добавление элемента в стек."""
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top
            self.top = new_node
        else:
            return 'Стек переполнен.'

    def pop(self):
        """Удаляет последний добавленный элемент стека."""
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            remove_last.next_node = None
            return remove_last.data
        else:
            return 'Стек пуст.'

    def is_empty(self):
        """Проверяет, пуст ли стек."""
        if self.top:
            return False
        return True

    def is_full(self):
        """Проверяет, заполнен ли стек."""
        return self.size_stack() == self.stack_size

    def clear_stack(self):
        """Очищает стек."""
        while self.top:
            self.pop()

    def get_data(self, index):
        """Возвращает данные по индексу."""
        counter = self.size_stack() - 1
        current_node = self.top
        while current_node:
            if counter == index:
                return current_node.data
            current_node = current_node.next_node
            counter -= 1
        return f"Out of range"

    def size_stack(self):
        """Возвращает размер стека."""
        counter = 0
        current_node = self.top
        while current_node:
            counter += 1
            current_node = current_node.next_node
        return counter


if __name__ == '__main__':
    size = 20
    s = Steck(size)

    # Заполняем стек.
    for i in range(1, size + 1):
        s.push(f'some data {i}')

    # Получаем данные по индексу.
    print(s.get_data(5))

    # Очищаем стек.
    s.clear_stack()

    print(s.is_full())

    # Снова заполняем стек.
    for i in range(1, size + 1):
        s.push(f'some data {i}')

    print(s.is_full())
    assert s.push('6') == 'Стек переполнен.'

    # Удаляем по одному все элементы стека.
    for i in range(1, size + 1):
        s.pop()

    assert s.pop() == 'Стек пуст.'
    assert s.is_empty() == True

    print(s.size_stack())
