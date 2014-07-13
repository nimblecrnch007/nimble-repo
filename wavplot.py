# Required modules:
# 1. scipy
# 2. matplotlib

from scipy.io import wavfile
from matplotlib import pyplot
import sys

# read audio samples:
[sampleRate, data] = wavfile.read(sys.argv[1])  # pass a .wav file as a command line arg.

# input the number of samples to plot:
print 'Enter number of samples. (say 1024)'
SAMPLES = input()

# plot:
pyplot.plot(data[:SAMPLES])

# label the axes:
pyplot.ylabel('Amplitude')
pyplot.xlabel('Time samples')

# set title:
pyplot.title('TITLE')

# display plot:
pyplot.show()
