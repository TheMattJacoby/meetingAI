# main.py

import subprocess
import sys

# Run the environment setup script
subprocess.check_call([sys.executable, "setup_environment.py"])

# Import and start the tray UI
from ui.tray import start_ui

def main():
    """Starts the system tray UI."""
    start_ui()

if __name__ == "__main__":
    main()
