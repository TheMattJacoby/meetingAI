# ui/__init__.py
"""UI package for system tray management."""

# Import key components for easier access
from .tray import start_ui
from .handlers import (
    record_action,
    stop_record_action,
    transcribe_action,
    assign_speakers_action,
    summarize_action,
    retry_summarization_action,
    export_action
)
from .icons import create_icon
