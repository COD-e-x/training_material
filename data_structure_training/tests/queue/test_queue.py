import unittest
from data_structure_training.src.queue.queue_class import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_is_empty(self):
        self.queue.enqueue('test_data_1')
        self.assertEqual(self.queue.is_empty(), False)
        self.queue.dequeue()
        self.assertEqual(self.queue.is_empty(), True)

    def test_is_full(self):
        self.assertEqual(self.queue.is_full(), False)
        for i in range(5):
            self.queue.enqueue('test_data')
        self.assertEqual(self.queue.is_full(), True)