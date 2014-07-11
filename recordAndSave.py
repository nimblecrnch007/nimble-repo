import pyaudio  # for python audio processing methods
import wave # to handle .wav files
import sys

CHUNK = 1024	# frames_per_buffer
FORMAT = pyaudio.paInt16	
CHANNELS = 2
RATE = 44100
RECORD_SECONDS
OUTPUT_WAVEFILE = 'sampleaudio.wav'

if sys.platform == 'darwin':	# for MAC users
	CHANNELS = 1

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

print '* REC'

frames = []

for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
	data = stream.read(CHUNK)
	frames.append(data)

print '* DONE RECORDING'

stream.stop_stream()
stream.close()
p.terminate()

wavfile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wavfilef.setnchannels(CHANNELS)
wavfile.setsampwidth(p.get_sample_size(FORMAT))
wavfile.setframerate(RATE)
wavfile.writeframes(b''.join(frames))
wavfile.close()
