from typing import Hashable



class Node():
    '''A class for nodes.'''


    def __init__(self, label):
        '''
        Creates a node with the given label.

        The label must be hashable. If it is not, an exception
        is raised.
        '''
        if not isinstance(label, Hashable):
            raise Exception('The label must be hashable')
        self.label = label
        self.successors = []    # List of nodes. Represent outgoing edges
        self.weights = []       # List of numbers (floats or ints). Represent outgoing edges' weights


    def add_successor(self, successor: 'Node', weight=1):
        '''
        Creates an edge between this node and the given node.
        The edge gets the given weight (default weight is 1).
        '''
        if not isinstance(successor, Node):
            raise Exception('Successor must be a Node')
        self.successors.append(successor)
        self.weights.append(weight)
