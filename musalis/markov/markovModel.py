import random

class MarkovModel():

    def __init__(self, order: int):
        '''
        Builds a MarkovModel.

        Parameters:
            - order: the order of the Markov model
        '''
        if order <= 0:
            raise Exception('Order of a Markov model must be greater than 0')
        self.order = order
        self.graph = dict()


    def next(self, prev_states: list):
        '''
        Returns a next state considering the previous states and the transition matrix.

        Parameters:
            - prev_states: the previous states
        
        Return:
            the next state
        '''
        if len(prev_states) != self.order:
            raise Exception(f'There must be exactly {self.order} previous states in a Markov model of order {self.order}')
        if not all(prev in self.states for prev in prev_states):
            raise Exception('At least one previous state is actually not a state')
        tmp = self.transition_matrix
        for prev in prev_states:
            tmp = tmp[prev]
        probabilities = (tmp[state] for state in self.states)
        return random.choices(self.states, weights=probabilities)[0]
