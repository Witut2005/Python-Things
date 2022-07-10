
import numpy as np

class linked_list:

    next_node = None
    value = None
    nodes = np.zeros([10])
    size = 0

    def __init__(self, value = 0):
        self.value = value

    def link(self, next_node):
        self.next_node = next_node

    def add_node(self, next_node):
        counter = 0
        while self.nodes[counter] != 0:
            counter += 1
        self.nodes[counter] = next_node
        self.size += 1

    def print(self):
        counter = 0
        while counter < self.size:
            print(self.nodes[counter])
            counter += 1
    pass

def find_value(x, y):
    for i in range(0, x.size):
        if x.nodes[i] == y.nodes[i]:
            return x.nodes[i]
    return None


a1 = linked_list(0)
a1.add_node(2)
a1.add_node(2)
a1.add_node(3)
a1.add_node(4)

b1 = linked_list(0)
b1.add_node(1)
b1.add_node(2)
b1.add_node(3)
b1.add_node(4)

print(find_value(a1, b1))