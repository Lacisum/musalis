import unittest

from musalis.markov.graph.node import Node


class NodeTest(unittest.TestCase):
    '''
    A test case for the Node class.
    '''


    @classmethod
    def setUpClass(cls):
        cls.node = Node("ABC")


    def test_label_is_set_correctly(self):
        self.assertEqual("ABC", self.node.label)
    
    def test_successors_are_set_correctly(self):
        self.assertEqual([], self.node.successors)
    
    def test_weights_are_set_correctly(self):
        self.assertEqual([], self.node.weights)
    
    def test_non_hashable_labels_are_forbidden(self):
        with self.assertRaises(Exception):
            Node(['A', 'B', 'C'])
    