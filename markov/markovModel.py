class MarkovModel():

	def __init__(self, states: tuple):
		self.states = states
		self.transition_matrix = dict()
		for row in states:
			self.transition_matrix[row] = dict()
			for column in states:
				self.transition_matrix[row][column] = 0.
