import pickle


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
            new_node.next_node = self.head
            self.head.prev_node = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node

    def print_ll_from_head(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next_node

    def print_ll_from_tail(self):
        node = self.tail
        while node is not None:
            print(node.data)
            node = node.prev_node

    def __iter__(self):
        self.current_node = self.head
        return self

    def __next__(self):
        if self.current_node:
            data = self.current_node.data
            self.current_node = self.current_node.next_node
            return data
        raise StopIteration


if __name__ == '__main__':
    box_list = LinkedList()
    box_list.insert_at_head('Барсик_1')
    box_list.insert_at_head('Снежок_0')
    box_list.insert_at_tail('Персик_2')
    x = list(box_list)
    print(x[0])

    # box_list = pickle.dumps(box_list)
    # print(box_list)
    # box_list = pickle.loads(box_list)
    # box_list.print_ll_from_head()
    # print()
    #
    # with open(r'./box_pickled.cats', 'wb') as fp:
    #     pickle.dump(box_list, fp)
    #
    # try:
    #     with open(r'./box_pickled.cats', 'rb') as fp:
    #         box_list_from_file = pickle.load(fp)
    # except FileNotFoundError:
    #     print('Файл не найден!')
    #
    # print(box_list_from_file)
    # box_list.print_ll_from_tail()
