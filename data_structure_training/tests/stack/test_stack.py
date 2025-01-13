import unittest
from data_structure_training.src.stack.main import Node, Stack

class TestNode(unittest.TestCase):
    """Тесты для класса Node."""

    def test_Node(self):
        """Проверка создания узлов и их связей."""
        node_1 = Node(5)
        self.assertEqual(node_1.data, 5)
        self.assertEqual(node_1.next_node, None)
        node_2 = Node(2, node_1)
        self.assertEqual(node_2.next_node, node_1)
        self.assertEqual(node_2.next_node.data, 5)

class TestStack(unittest.TestCase):
    """Тесты для класса Stack."""

    def setUp(self):
        """Инициализация стека перед каждым тестом."""
        self.stack = Stack()

    def test_init(self):
        """Проверка инициализации стека."""
        self.assertEqual(self.stack.top, None)
        self.assertEqual(self.stack.stack_size, 5)

    def test_push(self):
        """Проверка добавления элементов в стек."""
        self.stack.push('test_data')
        self.assertEqual(self.stack.top.data, 'test_data')
        for i in range(4):
            self.stack.push('test_data_in_range')
        self.assertEqual(self.stack.push('test_overflow'), 'Стек переполнен')

    def test_pop(self):
        """Проверка удаления элементов из стека."""
        self.stack.push('test_data')
        self.assertEqual(self.stack.pop(), 'test_data')
        self.assertEqual(self.stack.pop(), 'Стек пуст')

    def test_is_empty(self):
        """Проверка, пуст ли стек."""
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push('test_data')
        self.assertEqual(self.stack.is_empty(), False)

    def test_is_full(self):
        """Проверка, заполнен ли стек."""
        self.assertEqual(self.stack.is_full(), False)
        for i in range(5):
            self.stack.push('test_data_range')
        self.assertEqual(self.stack.is_full(), True)

    def test_clear_stack(self):
        """Проверка очистки стека."""
        self.stack.push('test_data')
        self.stack.clear_stack()
        self.assertEqual(self.stack.top, None)

    def test_get_data(self):
        """Проверка получения данных из стека по индексу."""
        self.stack.push('test_data_1')
        self.stack.push('test_data_2')
        self.assertEqual(self.stack.get_data(1), 'test_data_1')
        self.assertEqual(self.stack.get_data(0), 'test_data_2')
        self.assertEqual(self.stack.get_data(2), 'Out of range')

    def test_size_stack(self):
        """Проверка подсчета элементов в стеке (размер стека)."""
        self.stack.push('test_data')
        self.assertEqual(self.stack.size_stack(), 1)


    def test_counter_int(self):
        """Проверка подсчета целых чисел в стеке."""
        for i in range(2):
            self.stack.push('test_data')
            self.stack.push(1)
        self.assertEqual(self.stack.counter_int(), 2)