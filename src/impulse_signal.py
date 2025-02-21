import numpy as np
import soundfile as sf  #pip install soundfile  <- install this package
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

sampling_rate = 48000  #48Khz
total_duration = 10  # 10 second
interval = 0.005 #50ms

# generate impulse signals
# 1 second for a 48kHz sampling rate
impulse = np.zeros(sampling_rate * total_duration)


calculated_interval = int(sampling_rate * interval)  #50ms

for i in range(0, len(impulse), calculated_interval):
    impulse[i] = 1.0  #set a single signal every interval(50ms)

file_path = os.path.join(current_directory, "impulse_signal.wav")
sf.write(file_path, impulse, 48000)
print(f"saved complete: {file_path}")

