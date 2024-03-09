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
    
    def test_can_add_successors(self):
        successor1 = Node('BAA')
        successor2 = Node('AAA')
        self.assertEqual([], self.node.successors)
        self.node.add_successor(successor1)
        self.assertEqual([successor1], self.node.successors)
        self.node.add_successor(successor2)
        self.assertEqual([successor1, successor2], self.node.successors)

    def test_successors_must_be_nodes(self):
        with self.assertRaises(Exception):
            self.node.add_successor(4)
