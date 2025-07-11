import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
  Project_Name: str = "Jobnexa"
  POSTGRES_URL: str = os.getenv("DATABASE_URL")
  GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
  FRONTEND_ORIGIN: str = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")


settings = Settings()