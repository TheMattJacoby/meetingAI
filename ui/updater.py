# ui/updater.py

from ui.icons import create_icon

def update_tray_icon(tray_app, state):
    """
    Updates the tray icon and menu dynamically.

    Parameters:
    - tray_app (TrayApp): The TrayApp instance.
    - state (str): The current state ('recording' or 'idle').
    """
    tray_app.is_recording = (state == "recording")

    # Change icon based on state
    tray_app.tray_icon.icon = create_icon("recording" if tray_app.is_recording else "idle")

    # Update menu dynamically
    tray_app.tray_icon.menu = tray_app.build_menu()

    # Refresh the UI
    tray_app.tray_icon.visible = False
    tray_app.tray_icon.visible = True
    print(f"✅ Tray UI updated: {'Recording' if tray_app.is_recording else 'Idle'}.")
