# 📝 Meeting Recorder & AI Summarizer  

🚀 **Capture, transcribe, summarize, and analyze your meetings with AI!**  
This application **records** Microsoft Teams (or any audio source), **transcribes speech** using Whisper, and **generates structured meeting summaries** using AI (Phi-2, OpenAI, Claude, Gemini, or Mistral).  

---

## 🔹 Features  
👉 **System Tray App** – Start/stop recording with ease.  
👉 **AI-Powered Summaries** – Choose from multiple LLMs (OpenAI, Claude, Gemini, Mistral, or local).  
👉 **Multiple Summaries Per Meeting** – Generate different summaries using different models or settings.  
👉 **Retry Failed Summarizations** – If an API call fails, the system supports rerunning summarization.  
👉 **Export to Word, PDF, or TXT** – Generate professional meeting reports.  
👉 **Configurable Settings** – Customize AI models, export formats, security, and more.  
👉 **Security & Privacy** – Encryption, auto-delete, and restricted access.  

---

## 📂 Project Structure  
```
/meeting_recorder
    ├─ main.py                  # System tray & UI integration
    ├─ config.py                # Configurable settings (prefixes, paths)
    ├─ database.py              # SQLite database management
    ├─ recorder.py              # Audio recording & merging
    ├─ transcriber.py           # Speech-to-text (Whisper)
    ├─ process_transcription.py # Stores structured insights
    ├─ llm_analysis.py          # AI summarization (Phi-2, OpenAI, Claude, Gemini, Mistral)
    ├─ export.py                # Export to Word/PDF/TXT
    ├─ logger.py                # Logs API calls, failures, and costs
    ├─ requirements.txt         # Dependencies
    ├─ README.md                # Documentation (You are here!)
```

---

## 🛠 Installation  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/meeting-recorder-ai.git
cd meeting-recorder-ai
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application  
```bash
python main.py
```

---

## 🎤 How It Works  
1. **Record the meeting** → Audio is captured from the microphone and system audio.  
2. **Transcription & Summarization** → Converts speech to text and generates structured insights.  
3. **AI-Powered Summarization** → The system selects an AI model (local or external) to process and generate summaries.  
4. **Support for Multiple Summaries** → Users can generate different summaries with different models or settings.  
5. **Retry on API Failures** → If an API call fails, users can trigger a retry.  
6. **Export Meeting Notes** → Save transcriptions and summaries in DOCX, PDF, or TXT formats.  

---

## 🎨 Key Features  
| Feature                      | Description |
|------------------------------|-------------|
| 🎤 **Record Meetings**       | Captures both microphone & speaker audio |
| 📝 **AI Summarization**      | Supports OpenAI, Claude, Gemini, Mistral, and local models |
| 🔄 **Multiple Summaries**    | Meetings can have multiple summaries (different models/settings) |
| ❌ **Retry Summarization**   | If an API call fails, the system supports a retry |
| 📚 **Full Transcriptions**   | Automatically generates text transcripts |
| 📂 **Export to Word/PDF/TXT**| Save meeting notes in a professional format |
| 📊 **LLM Cost Tracking**     | Logs token usage and cost per API call |
| 🛠 **Dynamic Configurations**| Customize LLMs, export settings, security, and more |

---

## 🔧 Configuration (`config.py`)  
```python
# 🚀 LLM Configuration (Choose Local or External API)
USE_EXTERNAL_LLM = True  # Toggle between local and cloud-based LLMs
EXTERNAL_LLM_PROVIDER = "openai"  # Options: "openai", "claude", "gemini", "mistral"

# 🔍 API Keys (Set these in environment variables for security)
OPENAI_API_KEY = "your-openai-api-key"
CLAUDE_API_KEY = "your-claude-api-key"
GEMINI_API_KEY = "your-gemini-api-key"
MISTRAL_API_KEY = "your-mistral-api-key"
```

---

## 📊 LLM Cost Tracking & Logging  
- Logs **token usage, estimated cost, and response time**.  
- **Failed API calls are logged** for debugging.  
- Users can **review cost logs & API failures** via the UI.  

---

## 📝 Exporting Meeting Notes  
- Save meeting summaries & transcripts in **DOCX, PDF, or TXT**.  
- The document includes:  
  ✅ Summary  
  ✅ Commitments  
  ✅ Coaching Opportunities  
  ✅ Full Transcript  

---

## 🖥 System Tray UI  
- **Right-click the tray icon** to access features:  
  ✅ Start Recording  
  ✅ View Analysis  
  ✅ Assign Speaker Names  
  ✅ Trigger Summarization  
  ✅ Retry Failed Summarizations  
  ✅ Export Meeting to Word/PDF/TXT  
  ✅ Exit  

---

## 🛠 Next Features (Contribute!)  
Want to contribute? Check out our roadmap!  
💡 **Ideas:** Auto-scheduled summarization, cloud storage integration, meeting insights dashboard.  

---

## 👥 Contributing  
1. **Fork the repository**  
2. **Create a feature branch** (`git checkout -b feature-xyz`)  
3. **Commit changes** (`git commit -m "Added feature xyz"`)  
4. **Push to branch** (`git push origin feature-xyz`)  
5. **Create a pull request** 🚀  

---

## 🛠 Dependencies  
- `python-docx` → Word document generation  
- `sounddevice` → Capturing system & mic audio  
- `pydub` → Audio processing  
- `whisper` → Speech-to-text AI  
- `transformers` → AI-based summarization  

---

## 📝 License  
This project is licensed under **MIT License**. Feel free to use, modify, and distribute!  

---

## 📱 Support  
If you have questions or feedback, open an **issue** on GitHub! 🚀

