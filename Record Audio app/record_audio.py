import pyaudio
import wave
from threading import Timer

record = True

def stop_record():
    global record
    record = False
    print("Stopped")
    return record

chunk = 1024
sample_format = pyaudio.paInt16
channels = 1
fs = 44100
seconds = 3
filename = "output.wav"

p = pyaudio.PyAudio()

print("Record")

stream = p.open(format = sample_format,
channels = channels,
rate = fs,
frames_per_buffer = chunk,
input = True)

frames = []

Timer(seconds, stop_record).start()

while record:
    data = stream.read(chunk)
    frames.append(data)



stream.stop_stream()
stream.close()
p.terminate()

print("Finished recording")

wf = wave.open(filename, "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b"".join(frames))
wf.close()