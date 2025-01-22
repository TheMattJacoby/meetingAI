import os
import subprocess
import sys

VENV_DIR = "venv"
REQUIREMENTS_FILE = "requirements.txt"

# 🚀 Step 1: Ensure Virtual Environment Exists
def ensure_venv():
    """Checks if venv exists, creates it if not."""
    if not os.path.exists(VENV_DIR):
        print("🔧 Virtual environment not found. Creating one...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
        print("✅ Virtual environment created.")

# 🚀 Step 2: Activate Virtual Environment
def activate_venv():
    """Ensures the correct virtual environment is activated."""
    venv_python = os.path.join(VENV_DIR, "Scripts", "python.exe") if os.name == "nt" else os.path.join(VENV_DIR, "bin", "python3")

    if sys.executable != venv_python:
        print(f"🔄 Switching to virtual environment ({venv_python})...")
        os.environ["VIRTUAL_ENV"] = os.path.abspath(VENV_DIR)
        os.environ["PATH"] = os.path.abspath(os.path.join(VENV_DIR, "Scripts" if os.name == "nt" else "bin")) + os.pathsep + os.environ["PATH"]
        sys.executable = venv_python
        print("✅ Virtual environment activated.")

# 🚀 Step 3: Detect & Fix Encoding Issues in `requirements.txt`
def fix_requirements_encoding():
    """Detects and converts requirements.txt to UTF-8 if needed, and removes BOM."""
    try:
        with open(REQUIREMENTS_FILE, "rb") as f:
            raw_data = f.read()

        # Strip BOM if present
        if raw_data.startswith(b'\xef\xbb\xbf'):  # UTF-8 BOM
            print("⚠️ Detected UTF-8 BOM in `requirements.txt`. Removing it...")
            raw_data = raw_data[3:]

        decoded_data = raw_data.decode("utf-8")

        # Rewrite file without BOM
        with open(REQUIREMENTS_FILE, "w", encoding="utf-8") as f:
            f.write(decoded_data)

        print("✅ `requirements.txt` successfully converted to UTF-8 and BOM removed.")
    except UnicodeDecodeError as e:
        print(f"❌ Encoding error in `requirements.txt`: {e}. Try recreating the file.")

# 🚀 Step 4: Check & Install Missing Packages Dynamically
def install_missing_requirements():
    """Reads requirements.txt safely and installs missing dependencies."""
    try:
        required_packages = set()

        # Read the cleaned requirements file
        with open(REQUIREMENTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                clean_line = line.strip()
                if clean_line and not clean_line.startswith("#"):  # Ignore empty lines & comments
                    required_packages.add(clean_line)

        installed_packages = set(subprocess.check_output([sys.executable, "-m", "pip", "list", "--format=freeze"], text=True).splitlines())

        missing_packages = required_packages - installed_packages

        # Special handling for git-based packages like `openai-whisper`
        git_packages = {pkg for pkg in missing_packages if "git+" in pkg}
        normal_packages = missing_packages - git_packages

        if normal_packages:
            print(f"🔍 Installing missing dependencies: {normal_packages}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", *normal_packages])
            print("✅ All normal dependencies installed.")

        for git_pkg in git_packages:
            print(f"🔍 Installing git-based package: {git_pkg}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", git_pkg])
            print(f"✅ Installed {git_pkg}.")

    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")

# 🚀 Run the setup process
ensure_venv()
activate_venv()
fix_requirements_encoding()  # Fix encoding before reading the file
install_missing_requirements()
