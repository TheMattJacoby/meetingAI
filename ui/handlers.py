import threading
import sqlite3
from recorder import start_recording, stop_recording
from transcriber import transcribe_audio
from llm_analysis import generate_summary
from export import export_meeting_summary
from ui.icons import create_icon
from ui.tray import update_tray_icon

DB_FILE = "recordings.db"
is_recording = False  # Global flag to track recording state
tray_icon = None  # Global variable for system tray icon

# Start recording
def record_action(icon, item):
    """Starts the recording process and updates UI state."""
    global is_recording, tray_icon
    if not is_recording:
        print("Recording started...")
        is_recording = True
        tray_icon.icon = create_icon(recording=True)  # Change to red icon
        threading.Thread(target=start_recording, args=("meeting_audio.wav", 60)).start()
        update_tray_icon("recording")  # Change tray icon to recording mode

# Stop recording
def stop_record_action(icon, item):
    """Stops recording and updates UI state."""
    global is_recording, tray_icon
    if is_recording:
        print("Stopping recording...")
        stop_recording()
        is_recording = False
        tray_icon.icon = create_icon(recording=False)  # Back to idle icon
        print("Recording stopped.")
        update_tray_icon("idle")  # Change tray icon back to idle mode

# Transcribe meeting
def transcribe_action(icon, item):
    """Transcribes the latest recording."""
    print("Transcribing audio...")
    transcript = transcribe_audio("meeting_audio.wav")
    save_transcript_to_db(transcript)
    print("Transcription complete.")

# Assign speaker names
def assign_speakers_action(icon, item):
    """Assigns speaker names to transcript."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, transcript FROM meetings ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    
    if row:
        print(f"Assigning speakers for Meeting {row[0]}...")
        # Placeholder: Implement speaker naming logic
    else:
        print("No meeting found.")

    conn.close()

# Generate AI summary
def summarize_action(icon, item):
    """Runs AI summarization."""
    print("Generating AI summary...")
    summary = generate_summary("meeting_audio.wav")
    save_summary_to_db(summary)
    print("Summary complete.")

# Retry failed summaries
def retry_summarization_action(icon, item):
    """Retries failed LLM summarizations."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM meeting_summaries WHERE status='failed' ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    
    if row:
        print(f"Retrying summarization for Summary {row[0]}...")
        summary = generate_summary("meeting_audio.wav")
        update_summary_status(row[0], summary)
    else:
        print("No failed summaries to retry.")

    conn.close()

# Export summary
def export_action(icon, item):
    """Exports the meeting summary to a document."""
    print("Exporting summary...")
    export_meeting_summary("meeting_summary.docx")
    print("Export complete.")

# Save transcript
def save_transcript_to_db(transcript):
    """Stores the transcript in the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO meetings (transcript) VALUES (?)", (transcript,))
    conn.commit()
    conn.close()

# Save summary
def save_summary_to_db(summary):
    """Stores the summary in the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO meeting_summaries (summary, status) VALUES (?, 'success')", (summary,))
    conn.commit()
    conn.close()

# Update summary status
def update_summary_status(summary_id, summary):
    """Updates the status of a failed summary."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE meeting_summaries SET summary=?, status='success' WHERE id=?", (summary, summary_id))
    conn.commit()
    conn.close()
