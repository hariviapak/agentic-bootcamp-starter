from dataclasses import dataclass
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@dataclass
class Settings:
    model_name: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    temperature: float = float(os.getenv("TEMPERATURE", "0.3"))
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")

settings = Settings()
