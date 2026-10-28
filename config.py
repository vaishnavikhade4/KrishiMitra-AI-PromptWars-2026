import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Safely load .env with or without python-dotenv
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(BASE_DIR, ".env"))
except ImportError:
    env_file = os.path.join(BASE_DIR, ".env")
    if os.path.exists(env_file):
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = val.strip().strip("'\"")
                    if key not in os.environ:
                        os.environ[key] = val

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "krishimitra_secure_session_key_2026_hackathon")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///" + os.path.join(BASE_DIR, "database.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Model configuration
    MODEL_PATH = os.path.join(BASE_DIR, "models", "plant_disease_model.keras")
    
    # Weather & External APIs
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
    DATA_GOV_IN_API_KEY = os.getenv("DATA_GOV_IN_API_KEY", "")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    
    # Upload settings
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
