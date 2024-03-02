from music21 import interval

import random


def pitchesUniformDistribution(theScale, minPitch, maxPitch, maxLeap=None, amount=50):
	'''
	Generates a random list of pitches using a uniform distribution of probability.
	'''
	possiblePitches = theScale.getPitches(minPitch, maxPitch)
	# if maxLeap is None, allow all melodic motions
	if maxLeap is None:
		pitches = random.choices(possiblePitches, k=amount)
	# else, leaps must be equal or less than maxLeap
	else:
		# transform potentially descending maxLeap into an ascending interval
		maxLeap = interval.Interval(maxLeap.name)
		# randomly choose the first pitch
		pitches = [random.choice(possiblePitches)]
		# choose the remaining pitches
		for i in range(0,amount-1):
			currentPitch = pitches[i]
			nextMinPitch = max( currentPitch.transpose(maxLeap.reverse()), minPitch )
			nextMaxPitch = min( currentPitch.transpose(maxLeap), maxPitch )
			possiblePitches = theScale.getPitches(nextMinPitch, nextMaxPitch)
			nextPitch = random.choice(possiblePitches)
			pitches.append(nextPitch)
	return pitches
