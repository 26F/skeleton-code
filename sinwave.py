
# write a wave file in Python (stereo) 
# we'll create a Sine wave to illustrate
import wave, struct, numpy, random

sampleRate = 44100.0 # hertz
# open (create) wave file
waveout = wave.open("sinewave.wav", "w")
# how many channels, 2 for stereo
waveout.setnchannels(2)
# 2 bytes per sample, e.g 2^^16
# -32767, 32767 e.g this is a 16-bit wave
waveout.setsampwidth(2)
waveout.setframerate(sampleRate)

# 2 seconds of audio
for i in range(int(sampleRate * 2)):
	vl = 32767 * numpy.sin(i / 25)
	vr = 32767 * numpy.cos(i / 25)

	data = struct.pack('<h', int(vl))
	waveout.writeframesraw(data)

	data = struct.pack('<h', int(vr))
	waveout.writeframesraw(data)

waveout.close()