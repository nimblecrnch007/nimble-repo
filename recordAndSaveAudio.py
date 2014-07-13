import pyaudio  # for python audio processing methods
import wave # to handle .wav files
import sys
import os.path 

FORMAT = pyaudio.paInt16	
CHUNK = 1024	# frames_per_buffer
CHANNELS = 2	# stereo
RATE = 44100	# 44.1kHz sampling rate
RECORD_SECONDS = int(raw_input("Enter the number of seconds to record: ")) 	
#OUTPUT_WAVEFILE = 'sampleaudio.wav'
TRACK_NO = 0	# Track number. As the name says. 
OUTPUT_WAVEFILE = 'SampleAudio'+str(TRACK_NO)+'.wav'
SAVE_FOLDER = 'Saved Recordings'

if sys.platform == 'darwin':	# for Mac users
  CHANNELS = 1
  
if os.path.exists(SAVE_FOLDER):
	pass
else:
	os.makedirs(SAVE_FOLDER)

p = pyaudio.PyAudio()

# opening an input stream:
inputStream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print '* REC'

frames = []

for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
  data = inputStream.read(CHUNK)
  frames.append(data)

print '* DONE RECORDING'

inputStream.stop_stream()
inputStream.close()

p.terminate()

save =  raw_input("Do you want to save the recording?(Press N to Discard): ")
if save == ('N' or 'n'):
	print "Discarding the record!"
else:
	# Checks if the file already exists in the folder.
	SAVE_LOC = SAVE_FOLDER+'/'+OUTPUT_WAVEFILE
	
	while os.path.isfile(SAVE_LOC):
		# generates a new file name for saving after confirming to save
		TRACK_NO += 1
		OUTPUT_WAVEFILE = 'SampleAudio'+str(TRACK_NO)+'.wav'
		SAVE_LOC = SAVE_FOLDER+'/'+OUTPUT_WAVEFILE
	
	# now saving recorded audio onto a .wav file:
	wavfile = wave.open(SAVE_LOC, 'wb')
	wavfile.setnchannels(CHANNELS)
	wavfile.setsampwidth(p.get_sample_size(FORMAT))
	wavfile.setframerate(RATE)
	wavfile.writeframes(b''.join(frames))
	wavfile.close()
