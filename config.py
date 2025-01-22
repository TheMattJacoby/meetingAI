import os

# 🚀 LLM Configuration (Choose Local or External API)
USE_EXTERNAL_LLM = False  # Toggle between local and cloud-based LLMs
EXTERNAL_LLM_PROVIDER = "openai"  # Options: "openai", "claude", "gemini", "mistral"

# 🔍 API Keys (Set these in environment variables for security)
OPENAI_API_KEY = "your-openai-api-key"
CLAUDE_API_KEY = "your-claude-api-key"
GEMINI_API_KEY = "your-gemini-api-key"
MISTRAL_API_KEY = "your-mistral-api-key"

# 📝 Export Formats
EXPORT_FORMAT = "docx"  # Options: "docx", "pdf", "txt"
EXPORT_FILENAME_FORMAT = "{event_name}_{date}.docx"

# 🔒 Security
ENABLE_TRANSCRIPTION_ENCRYPTION = False
AUTO_DELETE_RAW_AUDIO = False

# 📊 LLM Cost Tracking
COST_PER_1000_TOKENS = {
    "openai": 0.01,
    "claude": 0.008,
    "gemini": 0.007,
    "mistral": 0.006
}