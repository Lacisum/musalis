from music21 import note, pitch, scale, stream

from choice import pitchChoice




def main():

    # set the possible pitches
    cMajorScale = scale.MajorScale('C')
    minPitch, maxPitch = pitch.Pitch('C4'), pitch.Pitch('A5')

    # generate a melody
    randPitches = pitchChoice.pitchesMaxLeapIsPerfectFourth(cMajorScale, minPitch, maxPitch)
    randNotes = [note.Note(pitch) for pitch in randPitches]

    # put the melody into a stream
    myStream = stream.Stream()
    myStream.append(randNotes)

    # show the stream in a music notation program
    myStream.show()




if __name__ == '__main__':
    main()