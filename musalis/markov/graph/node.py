from typing import Hashable

class Node():

    def __init__(self, label):
        if not isinstance(label, Hashable):
            raise Exception('The label must be hashable')
        self.label = label
        self.successors = []    # represent outgoing edges
        self.weights = []       # represent outgoing edges' weights

    def add_successor(self, successor: 'Node', weight=1):
        pass

    def set_weight(self, index: int):
        pass
