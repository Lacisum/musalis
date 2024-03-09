import unittest

from musalis.markov.graph.graph import Graph


class GraphTest(unittest.TestCase):
    '''
    A test case for the Graph class.
    '''


    def setUp(self):
        self.graph = Graph()


    def test_nodes_are_set_correctly(self):
        self.assertEqual(dict(), self.graph.nodes)
