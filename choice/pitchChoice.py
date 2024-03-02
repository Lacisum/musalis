from music21 import pitch

import random


def pitchesUniformDistribution(theScale, lowestPitch, highestPitch, amount=50):
	'''
	Generates a random list of pitches using a uniform distribution of probability.
	'''
	possiblePitches = theScale.getPitches(lowestPitch, highestPitch)
	return random.choices(possiblePitches, k=amount)
