from typing import Hashable

from musalis.markov.graph.node import Node



class Graph():


    def __init__(self):
        self.nodes = dict()


    def add_node(self, node_label):
        if not isinstance(node_label, Hashable):
            raise Exception("The node's label must be hashable")
        if node_label in self.nodes.keys():
            return
        self.nodes[node_label] = Node(node_label)
