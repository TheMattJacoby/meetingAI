import sounddevice as sd
import wave

def record_audio(filename, duration=10, samplerate=44100, channels=1):
    """Records audio and saves it to a WAV file."""
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype="int16")
    sd.wait()
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes())