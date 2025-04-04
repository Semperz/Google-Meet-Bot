import sounddevice as sd
from scipy.io.wavfile import write
import os
from dotenv import load_dotenv

load_dotenv()

class AudioRecorder:
    def __init__(self):
        self.sample_rate = int(os.getenv('SAMPLE_RATE', 48000)) # Sample rate in Hz, CHANGE THIS TO 44100 IF NEEDED

    def get_audio(self, filename, duration):
        device_info = sd.query_devices(kind='output')
        device_index = 12
        device_info = sd.query_devices(device_index)
        print(f"Device info for index {device_index}: {device_info}")
        print("Recording...")
        print(f"Using device: {device_info['name']}")
        print(f"Devices available: {sd.query_devices()}")
        recording = sd.rec(int(duration * self.sample_rate), samplerate=self.sample_rate, channels=2, dtype='int16', device=12)
        sd.wait()  # Wait until the recording is finished
        write(filename, self.sample_rate, recording)
        print(f"Recording finished. Saved as {filename}.")
