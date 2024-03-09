import unittest

from musalis.markov.markovModel import MarkovModel


class MarkovModelTest(unittest.TestCase):
    '''
    A test case for the MarkovModel class.
    '''


    @classmethod
    def setUpClass(cls):
        cls.mm = MarkovModel(1)
        data = ['A', 'B', 'A', 'A', 'C']
        cls.STATES = list(set(data))
        cls.mm.train(data)    


    def test_order_is_set_correctly(self):
        emptyMm = MarkovModel(3)
        self.assertEqual(3, emptyMm.order)
    

    def test_graph_is_initially_empty(self):
        emptyMm = MarkovModel(3)
        self.assertEqual(Graph(), emptyMm.graph)


    def test_exception_raised_when_order_is_zero(self):
        with self.assertRaises(Exception):
            MarkovModel(0)


    def test_exception_raised_when_order_is_negative(self):
        with self.assertRaises(Exception):
            MarkovModel(-1)


    def test_method_train_creates_the_states(self):
        '''Test wether the Markov model contains all the states and only the states present in the training data.'''
        self.assertEqual(len(self.STATES), len(self.mm.getStates()))
        self.assertEqual(set(self.STATES), set(self.mm.getStates()))


    def test_method_getSequenceProbability_works_if_existing_states_are_passed_in_argument_as_the_previous_states(self):
        self.assertAlmostEqual(1/3, self.mm.getSequenceProbability(('A'), 'A'))
        self.assertAlmostEqual(1/3, self.mm.getSequenceProbability(('A'), 'B'))
        self.assertAlmostEqual(1/3, self.mm.getSequenceProbability(('A'), 'C'))
        self.assertEqual(1, self.mm.getSequenceProbability(('B'), 'A'))
        self.assertEqual(0, self.mm.getSequenceProbability(('B'), 'B'))
        self.assertEqual(0, self.mm.getSequenceProbability(('B'), 'C'))
        # test for the state that ends the training data list
        self.assertEqual(0, self.mm.getSequenceProbability(('C'), 'A'))
        self.assertEqual(0, self.mm.getSequenceProbability(('C'), 'B'))
        self.assertEqual(0, self.mm.getSequenceProbability(('C'), 'C'))
        # test for a non existing state
        self.assertNotIn('Z', self.mm.getStates())
        self.assertEqual(0, self.mm.getSequenceProbability(('A'), 'Z'))


    def test_method_getSequenceProbability_raises_exception_if_non_existing_states_are_passed_in_argument_as_the_previous_states(self):
        self.assertNotIn('Z', self.mm.getStates())
        with self.assertRaise(Exception):
            self.mm.getSequenceProbability(('Z'), 'A')
                        


    def test_method_next_raises_exception_if_too_many_previous_states_are_passed_in_argument(self):
        self.assertEqual(1, self.mm.order)
        with self.assertRaises(Exception):
            self.mm.next(('B', 'A'))
    

    def test_method_next_raises_exception_if_too_few_previous_states_are_passed_in_argument(self):
        self.assertEqual(1, self.mm.order)
        with self.assertRaises(Exception):
            self.mm.next(())


    def test_method_next_raises_exception_if_a_previous_state_has_no_next_state(self):
        self.assertIn('C', self.mm.getStates())
        with self.assertRaises(Exception):
            self.mm.next(('C'))


    def test_method_next_raises_exception_if_a_previous_state_is_actually_not_a_state(self):
        self.assertNotIn('Z', self.mm.getStates())
        with self.assertRaises(Exception):
            self.mm.next(('Z'))


    def test_next_works_with_the_right_probabilites(self):
        for i in range(1000):
            self.assertEqual('A', self.mm.next(('B')))
