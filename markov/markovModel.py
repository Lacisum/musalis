import random

class MarkovModel():

    def __init__(self, states: set):
        self.states = tuple(states)
        self.transition_matrix = dict()
        for row in states:
            self.transition_matrix[row] = dict()
            for column in states:
                self.transition_matrix[row][column] = 0.

    def next(self, prev_states: list):
        '''
        Returns a next state considering the previous states and the transition matrix.

        Parameters:
            - pre_states: the previous states
        
        Return:
            the next state
        '''
        if len(prev_states) != 1:
            raise Exception('There must be exactly 1 previous state')
        if not all(prev in self.states for prev in prev_states):
            raise Exception('At least one previous state is actually not a state')
        tmp = self.transition_matrix
        for prev in prev_states:
            tmp = tmp[prev]
        probabilities = (tmp[state] for state in self.states)
        return random.choices(self.states, weights=probabilities)[0]
