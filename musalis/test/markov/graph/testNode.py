import unittest

from musalis.markov.graph.node import Node


class NodeTest(unittest.TestCase):
    '''
    A test case for the Node class.
    '''


    def setUp(self):
        self.node1 = Node("ABC")
        self.node2 = Node(('A', 2))
        self.node1.add_successor(self.node2)

    def test_label_is_set_correctly(self):
        self.assertEqual(('A', 2), self.node2.label)
    
    def test_successors_are_set_correctly(self):
        self.assertEqual([], self.node2.successors)
    
    def test_weights_are_set_correctly(self):
        self.assertEqual([], self.node2.weights)
    
    def test_non_hashable_labels_are_forbidden(self):
        with self.assertRaises(Exception):
            Node(['A', 'B'])
    
    def test_successors_must_be_nodes(self):
        with self.assertRaises(Exception):
            self.node1.add_successor(4)
    
    def test_adding_successors_does_update_successors(self):
        self.assertEqual([self.node2], self.node1.successors)
        another_node = Node(3)
        self.node1.add_successor(another_node)
        self.assertEqual([self.node2, another_node], self.node1.successors)
    
    def test_adding_successors_does_update_weights(self):
        self.assertEqual([1], self.node1.weights)
        another_node = Node(3)
        self.node1.add_successor(another_node, 2.7)
        self.assertEqual([1, 2.7], self.node1.weights)
