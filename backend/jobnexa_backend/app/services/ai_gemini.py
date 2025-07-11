import google.generativeai as genai
from app.core.config import settings

genai.configure(
    api_key=settings.GEMINI_API_KEY,)

model = genai.GenerativeModel("gemini-pro")

async def ask_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini Error: {str(e)}"