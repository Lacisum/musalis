import unittest

from markov import *


class MarkovModelTest(unittest.TestCase):
    '''
    A test case for the MarkovModel class.
    '''


    def setUp(self):
        self.mm = MarkovModel({'A', 'B'})
        self.mm.transition_matrix['A']['A'] = 0.
        self.mm.transition_matrix['A']['B'] = 1.
        self.mm.transition_matrix['B']['A'] = 1.
        self.mm.transition_matrix['B']['B'] = 0.


    def test_constructor_works_when_passing_a_set(self):
        self.assertEqual(2, len(self.mm.states))
        self.assertEqual({'A', 'B'}, set(self.mm.states))


    def test_constructor_raises_exception_if_iterable_with_duplicates_is_passed_as_the_states(self):
        with self.assertRaises(Exception):
            MarkovModel(('A', 'B', 'B'))


    def test_next_works_with_the_right_probabilites(self):
        for i in range(1000):
            self.assertEqual('B', self.mm.next(('A')))
            self.assertEqual('A', self.mm.next(('B')))


    def test_next_raises_exception_if_there_is_the_wrong_number_of_previous_states_passed_in_argument(self):
        with self.assertRaises(Exception):
            self.mm.next(('B', 'A'))
    

    def test_next_raises_exception_if_a_previous_state_is_actually_not_a_state(self):
        with self.assertRaises(Exception):
            self.mm.next(('C'))



if __name__ == '__main__':
    unittest.main(verbosity=2)
