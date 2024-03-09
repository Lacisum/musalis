import unittest

from musalis.markov.graph.graph import Graph
from musalis.markov.graph.node import Node


class GraphTest(unittest.TestCase):
    '''
    A test case for the Graph class.
    '''


    def setUp(self):
        self.graph1 = Graph()
        self.graph2 = Graph()
        self.graph2.add_node('A')


    def test_nodes_are_set_correctly(self):
        self.assertEqual(dict(), self.graph1.nodes)

    def test_non_hashable_nodes_are_forbidden(self):
        with self.assertRaises(Exception):
            self.graph2.add_node(['not', 'hashable'])
    
    def test_adding_nodes_does_update_nodes(self):
        self.assertEqual({'A': Node('A')}, self.graph2.nodes)
        self.graph2.add_node('B')
        self.assertEqual({'A': Node('A'), 'B': Node('B')}, self.graph2.nodes)

    def test_trying_to_add_existing_node_does_nothing(self):
        pass # TODO
