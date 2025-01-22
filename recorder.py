import sounddevice as sd
import wave
import threading

recording = False  # Global flag to track recording state

def start_recording(filename="output.wav", duration=10, samplerate=44100, channels=1):
    """Records audio and saves it to a WAV file."""
    global recording
    recording = True
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype="int16")
    sd.wait()
    
    if recording:  # Only save if it was not stopped
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(2)
            wf.setframerate(samplerate)
            wf.writeframes(audio.tobytes())
        print(f"Recording saved as {filename}")

def stop_recording():
    """Stops an active recording."""
    global recording
    if recording:
        recording = False
        print("Recording manually stopped.")
    else:
        print("No active recording.")
