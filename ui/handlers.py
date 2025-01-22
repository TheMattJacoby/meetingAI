# ui/handlers.py

def get_menu_actions(tray_app):
    """Returns a list of menu actions, dynamically linked to `tray_app`."""
    return [
        ("🔴 Start Recording", lambda icon, item: tray_app.start_recording(icon, item)),
        ("⏹ Stop Recording", lambda icon, item: tray_app.stop_recording(icon, item)) if tray_app.is_recording else None,
        ("📝 Transcribe Meeting", transcribe_action),
        ("👤 Assign Speaker Names", assign_speakers_action),
        ("🤖 Generate Summary", summarize_action),
        ("🔄 Retry Failed Summaries", retry_summarization_action),
        ("📤 Export Summary", export_action),
        ("❌ Exit", lambda icon, item: tray_app.exit_app(icon, item))
    ]

def transcribe_action(icon, item):
    """Handles the action to transcribe the meeting."""
    print("📝 Transcribing meeting...")

def assign_speakers_action(icon, item):
    """Handles the action to assign speaker names."""
    print("👤 Assigning speaker names...")

def summarize_action(icon, item):
    """Handles the action to generate summary."""
    print("🤖 Generating summary...")

def retry_summarization_action(icon, item):
    """Handles the action to retry failed summaries."""
    print("🔄 Retrying failed summaries...")

def export_action(icon, item):
    """Handles the action to export the meeting summary."""
    print("📤 Exporting summary...")
