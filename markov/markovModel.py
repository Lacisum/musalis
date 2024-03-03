import itertools
import random

class MarkovModel():

    def __init__(self, states: set, order: int):
        '''
        Builds a MarkovModel.

        Parameters:
            - states: the set of states
            - order: the order of the Markov model
        '''
        if len(states) != len(set(states)):
            raise Exception('States must be unique')
        if order <= 0:
            raise Exception('Order of a Markov model must be greater than 0')
        self.states = tuple(states)
        self.order = order
        self.transition_matrix = dict()
        permutations_with_repetitions = itertools.product(self.states, repeat=order+1)
        for perm in permutations_with_repetitions:
            tmp = self.transition_matrix
            for i in range( len(perm) - 1):
                state = perm[i]
                if not state in tmp:
                    tmp[state] = dict()
                tmp = tmp[state]
            last_state = perm[-1]
            tmp[last_state] = 0.


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
