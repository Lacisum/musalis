from music21 import scale, note, stream

from choice import pitchChoice




def main():

    # set the possible pitches
    cMajorScale = scale.MajorScale('C')
    lowestPitch, highestPitch = 'C4', 'A5'

    # create a random list of notes
    randPitches = pitchChoice.pitchesUniformDistribution(cMajorScale, lowestPitch, highestPitch)
    randNotes = [note.Note(pitch) for pitch in randPitches]

    # put the list of notes into a stream
    myStream = stream.Stream()
    myStream.append(randNotes)

    # show the stream in a music notation program
    myStream.show()




if __name__ == '__main__':
    main()