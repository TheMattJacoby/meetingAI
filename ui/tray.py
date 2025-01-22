# ui/tray.py

import pystray
from pystray import MenuItem as item, Icon
import threading
import time
from ui.icons import create_icon
from ui.updater import update_tray_icon  # Updater handles tray updates

class TrayApp:
    def __init__(self):
        self.is_recording = False
        self.tray_icon = Icon("MeetingRecorder", create_icon("idle"), menu=self.build_menu())

    def build_menu(self):
        """Dynamically builds the menu based on recording status."""
        from ui.handlers import get_menu_actions  # Import only inside function to prevent circular import
        menu_actions = get_menu_actions(self)  # Pass `TrayApp` instance to handlers

        return pystray.Menu(
            *[item(label, action) for label, action in menu_actions if action is not None]
        )

    def start_recording(self, icon, item):
        """Handles the action to start recording."""
        print("🎤 Recording started...")
        self.is_recording = True
        update_tray_icon(self, "recording")

    def stop_recording(self, icon, item):
        """Handles the action to stop recording."""
        print("⏹ Recording stopped.")
        self.is_recording = False
        update_tray_icon(self, "idle")

    def exit_app(self, icon, item):
        """Stops the tray application."""
        icon.stop()

    def run(self):
        """Starts the tray icon."""
        self.tray_icon.run()

def start_ui():
    """Launches the system tray UI."""
    app = TrayApp()
    tray_thread = threading.Thread(target=app.run, daemon=True)
    tray_thread.start()
    tray_thread.join()
