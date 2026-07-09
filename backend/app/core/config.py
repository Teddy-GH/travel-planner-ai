from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application setting with environment variables"""

    # API Keys
    gemini_api_key: str

    # Model Configuration

    model_name: str = "gemini-2.0-flash-exp"
    temperature: float = 0.7
    max_tokens: int = 2048

    # Application
    app_name: str = "Travel Planner AI"
    debug: bool = True


    # CORS
    allowed_origins: list = ["https://localhost:3000"]

    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()        
