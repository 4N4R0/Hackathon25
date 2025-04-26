# Handle recording user voice input
# Capture microphone input and save as WAV
import sounddevice as sd
import scipy.io.wavfile as wav

def record_audio(save_path, duration=5, fs=16000):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write(save_path, fs, audio)
    print(f"Audio saved to {save_path}")
    return save_path