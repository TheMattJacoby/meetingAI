from recorder import start_recording
from transcriber import transcribe_audio
from llm_analysis import generate_summary
from ui import start_ui

def main():
    start_ui()  # Launch system tray UI

if __name__ == "__main__":
    main()