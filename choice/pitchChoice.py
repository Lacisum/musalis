from music21 import pitch

import random


def pitchesUniformDistribution(theScale, lowestPitch, highestPitch, amount=50):
	'''
	Generates a random list of pitches using a uniform distribution of probability.
	'''
	possiblePitches = theScale.getPitches(lowestPitch, highestPitch)
	return random.choices(possiblePitches, k=amount)


def pitchesMaxLeapIsPerfectFourth(theScale, minPitch, maxPitch, amount=50):
	'''
	Generates a random list of pitches using a uniform distribution of probability, 
	except that leaps bigger than a perfect 4th are forbidden.
	'''
	possiblePitches = theScale.getPitches(minPitch, maxPitch)
	pitches = [random.choice(possiblePitches)]
	for i in range(0,amount-1):
		currentPitch = pitches[i]
		nextMinPitch = max( currentPitch.transpose('P-4'), minPitch )
		nextMaxPitch = min( currentPitch.transpose('P4'), maxPitch )
		possiblePitches = theScale.getPitches(nextMinPitch, nextMaxPitch)
		nextPitch = random.choice(possiblePitches)
		pitches.append(nextPitch)
	return pitches
