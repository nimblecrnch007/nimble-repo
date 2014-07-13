import pyaudio  # for python audio processing methods
import wave # to handle .wav files
import sys

wavfile = wave.open(sys.argv[1], 'rb') # pass the .wav filename to be played as a command line argument
p = pyaudio.PyAudio()

CHUNK = 1024
WIDTH = wavfile.getsampwidth()
FORMAT = p.get_format_from_width(WIDTH)
CHANNELS = wavfile.getnchannels()
RATE = wavfile.getframerate()

# open output stream
outputStream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)

# read data
data = wavfile.readframes(CHUNK)

# play output stream
while data != '':
    outputStream.write(data)
    data = wavfile.readframes(CHUNK)

# stop and then close output stream
outputStream.stop_stream()
outputStream.close()

# close file
wavfile.close()

# terminate PyAudio
p.terminate()
