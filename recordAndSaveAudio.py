import pyaudio  # for python audio processing methods
import wave # to handle .wav files
import sys

FORMAT = pyaudio.paInt16	
CHUNK = 1024	# frames_per_buffer
CHANNELS = 2	# stereo
RATE = 44100	# 44.1kHz sampling rate
RECORD_SECONDS = 5	# 5 seconds of recording time
OUTPUT_WAVEFILE = 'sampleaudio.wav'

if sys.platform == 'darwin':	# for Mac users
	CHANNELS = 1

p = pyaudio.PyAudio()

# 
inputStream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print '* REC'

frames = []

for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
	data = stream.read(CHUNK)
	frames.append(data)

print '* DONE RECORDING'

stream.stop_stream()
stream.close()

p.terminate()

wavfile = wave.open(OUTPUT_WAVEFILE, 'wb')
wavfilef.setnchannels(CHANNELS)
wavfile.setsampwidth(p.get_sample_size(FORMAT))
wavfile.setframerate(RATE)
wavfile.writeframes(b''.join(frames))
wavfile.close()
