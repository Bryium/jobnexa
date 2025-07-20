import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

async def generate_roadmap(goal: str) -> str:
    prompt = f"""
    You're an expert African career mentor. Generate a 3-month learning roadmap for someone who wants to become a(n): {goal}.
    Format:
    Month 1:
    - ...
    Month 2:
    - ...
    Month 3:
    - ...
    Keep it concise and relevant for African youth with limited internet access.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini Error: {str(e)}"
