import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

ROADMAP_PROMPT = """
You are an expert career coach. Given a user's goal, generate a learning roadmap that spans 3 to 6 months.

Respond in this format:
Month 1:
- ...
Month 2:
- ...
...
Use bullet points, keep it concise but actionable.
"""

async def generate_roadmap(goal: str) -> str:
    try:
        full_prompt = f"{ROADMAP_PROMPT}\n\nGoal: {goal}"
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Roadmap Generation Error: {str(e)}"
