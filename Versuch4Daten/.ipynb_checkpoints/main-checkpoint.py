
import pyaudio
import numpy
import matplotlib.pyplot as plt
FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220
p = pyaudio.PyAudio()
print('running')
stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,
input=True,frames_per_buffer=FRAMESIZE)
data = stream.read(NOFFRAMES*FRAMESIZE)
decoded = numpy.frombuffer(data, 'int16')
stream.stop_stream()
stream.close()
p.terminate()
#numpy.save("aufnahme42", decoded)
a = decoded.tolist()

first20 = 20000
for x in a[20000:]:
    if x >= 50 or x <= -50:
        break
    first20 += 1

oneSecond = a[first20: first20 + 44100]

print(a)
numpy.save("testDatenJanis/rechts5", numpy.array(oneSecond))

print(numpy.shape(decoded))
print('done')
plt.plot(decoded)
plt.show()
plt.plot(numpy.array(oneSecond))
plt.show()
