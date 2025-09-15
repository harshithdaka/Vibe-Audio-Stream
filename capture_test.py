# This script tests if the sound device is working correctly by recording a short audio snippet.
# It requires the 'sounddevice' and 'numpy' libraries.

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

# --- Configuration ---
# Set the sample rate and recording duration.
sample_rate = 44100  # Standard audio CD quality
duration_seconds = 5  # Record for 5 seconds
channels = 2  # Stereo audio

# --- Main Logic ---
print("Recording audio...")

# Use the sounddevice library to record a NumPy array.
# The 'dtype' specifies the data type of the audio samples.
recording = sd.rec(int(duration_seconds * sample_rate), samplerate=sample_rate, channels=channels, dtype='float64')

# Wait for the recording to finish.
sd.wait()

print("Recording complete. Saving to file...")

# Save the recorded NumPy array to a WAV file.
write('output.wav', sample_rate, recording)

print("Audio saved successfully as output.wav")