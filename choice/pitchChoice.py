from music21 import pitch

import random


def generateRandomPitches(possiblePitches, amount=50):
    return random.choices(possiblePitches, k=amount)
