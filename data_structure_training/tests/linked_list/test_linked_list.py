import unittest
from data_structure_training.src.linked_list.linked_list_class import Node, LinkedList

class TestNode(unittest.TestCase):

    def test_Node(self):
        node_1 = Node(5)
        self.assertEqual(node_1.data, 5)
        self.assertEqual(node_1.next_node, None)
        node_2 = Node(3, node_1)
        self.assertEqual(node_2.data, 3)
        self.assertEqual(node_2.next_node.data, 5)

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll_list = LinkedList()

    def test_init(self):
        self.assertEqual(self.ll_list.head, None)

    def test_insert_at_head(self):
        self.ll_list.insert_at_head('test_data_1')
        self.ll_list.insert_at_head('test_data_2')
        self.assertEqual(self.ll_list.head.data, 'test_data_2')
        self.assertEqual(self.ll_list.head.next_node.data, 'test_data_1')

    def test_insert_at_end(self):
        self.ll_list.insert_at_end('test_data_1')
        self.ll_list.insert_at_end('test_data_2')
        self.assertEqual(self.ll_list.head.data, 'test_data_1')
        self.assertEqual(self.ll_list.head.next_node.data, 'test_data_2')

    def test_remove_node_position(self):
        self.ll_list.insert_at_head('test_data_1')
        self.ll_list.insert_at_head('test_data_2')
        self.ll_list.insert_at_end('test_data_3')
        self.assertEqual(self.ll_list.remove_node_position(1), 'Удален узел с данными test_data_2 позиции 1')
        self.assertEqual(self.ll_list.remove_node_position(2), 'Удален узел с данными test_data_3 позиции 2')
        self.assertEqual(self.ll_list.remove_node_position(234), 'Ничего не удалено')

    def test_insert_at_position(self):
        for i in range(5):
            self.ll_list.insert_at_head('test_data')
        self.assertEqual(self.ll_list.insert_at_position('test_insert_at_position_1',1),
                         'Узел с данными test_insert_at_position_1 добавлен на позицию 1')
        self.assertEqual(self.ll_list.insert_at_position('test_insert_at_position_2',2),
                         'Узел с данными test_insert_at_position_2 добавлен на позицию 2')
        self.assertEqual(self.ll_list.insert_at_position('test_insert_at_position_2', 234),None)

    def test_print_ll(self):
        for i in range(2):
            self.ll_list.insert_at_head('test_data')
        self.assertEqual(self.ll_list.print_ll(), 'Данные списка выведены')

    def test_get(self):
        self.ll_list.insert_at_head('test_data_1')
        self.ll_list.insert_at_head('test_data_2')
        self.ll_list.insert_at_head('test_data_3')
        found, test_node_1 = self.ll_list.get('test_data_2')
        not_found, test_node_2 = self.ll_list.get('test_not_data')
        self.assertEqual(self.ll_list.get('test_data_2'), (found, test_node_1))
        self.assertEqual(self.ll_list.get('test_not_data'), (not_found, None))

    def test_change_data(self):
        self.ll_list.insert_at_head('test_data_1')
        self.ll_list.insert_at_head('test_data_2')
        self.assertEqual(self.ll_list.change_data('test_data_1', 'test_change_1'), 'Заменены данные в узле № 2')
        self.assertEqual(self.ll_list.change_data('test_data_2', 'test_change_2'), 'Заменены данные в узле № 1')
        self.assertEqual(self.ll_list.change_data('test_not_data', 'test_change_2'), 'Данные не обнаружены')