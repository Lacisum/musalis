from typing import Hashable

from musalis.markov.graph.node import Node



class Graph():
    '''A class for graphs.'''


    def __init__(self):
        '''Creates a graph.'''
        self.nodes = dict()     # {node_label: node}


    def add_node(self, node_label):
        '''
        If the given node label is not worn by any of the graph's
        nodes, then adds a new node with that label to the graph.

        Otherwise, does nothing (i.e. does not replace or modify
        the already existing node).
        '''
        if not isinstance(node_label, Hashable):
            raise Exception("The node's label must be hashable")
        if node_label in self.nodes.keys():
            return
        self.nodes[node_label] = Node(node_label)
