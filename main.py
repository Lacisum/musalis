from music21 import scale, note, stream
import random




def main():

    # set the possible pitches
    cMajorScale = scale.MajorScale('C')
    possiblePitches = cMajorScale.getPitches('C4','A5')

    # create a random list of notes
    randPitches = random.choices(possiblePitches, k=50)
    randNotes = [note.Note(pitch) for pitch in randPitches]

    # put the list of notes into a stream
    myStream = stream.Stream()
    myStream.append(randNotes)

    # show the stream in a music notation program
    myStream.show()




if __name__ == '__main__':
    main()