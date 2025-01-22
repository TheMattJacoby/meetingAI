import subprocess
import sys

# 🚀 Ensure the environment is set up (including activation)
subprocess.check_call([sys.executable, "setup_environment.py"])

# 🚀 Start the application
from ui.tray import start_ui

def main():
    """Starts the system tray UI."""
    start_ui()

if __name__ == "__main__":
    main()
