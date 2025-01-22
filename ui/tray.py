import pystray
from pystray import MenuItem as item, Icon
import threading
import time
from ui.icons import create_icon
from ui.handlers import (
    record_action,
    stop_record_action,
    transcribe_action,
    assign_speakers_action,
    summarize_action,
    retry_summarization_action,
    export_action
)

is_recording = False  # UI flag for recording state
tray_icon = None  # Store tray icon reference

def build_menu():
    """Dynamically builds the menu based on recording status."""
    if is_recording:
        return pystray.Menu(
            item('⏹ Stop Recording', stop_record_action)
        )
    else:
        return pystray.Menu(
            item('🔴 Start Recording', record_action),
            item('📝 Transcribe Meeting', transcribe_action),
            item('👤 Assign Speaker Names', assign_speakers_action),
            item('🤖 Generate Summary', summarize_action),
            item('🔄 Retry Failed Summaries', retry_summarization_action),
            item('📤 Export Summary', export_action),
            item('❌ Exit', exit_action)
        )

def exit_action(icon, item):
    """Stops the tray application."""
    icon.stop()

def update_tray_icon(state):
    """Updates the tray icon and menu dynamically."""
    global tray_icon, is_recording
    is_recording = (state == "recording")

    # Change icon color based on state
    tray_icon.icon = create_icon("recording" if is_recording else "idle")

    # Update menu options
    tray_icon.menu = build_menu()

    # Refresh the tray UI
    tray_icon.visible = False
    tray_icon.visible = True
    print(f"✅ Tray UI updated: {'Recording' if is_recording else 'Idle'}.")

def start_ui():
    """Launches the system tray UI immediately and allows dynamic updates."""
    global tray_icon
    tray_icon = Icon("MeetingRecorder", create_icon("idle"), menu=build_menu())

    # Start the tray UI in a separate thread
    tray_thread = threading.Thread(target=tray_icon.run, daemon=True)
    tray_thread.start()

    # Keep the main thread alive
    tray_thread.join()
