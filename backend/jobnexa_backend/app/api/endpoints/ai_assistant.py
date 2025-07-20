from fastapi import APIRouter
from pydantic import BaseModel
from app.services.roadmap import generate_roadmap

router = APIRouter()

class GoalRequest(BaseModel):
    goal: str

@router.post("/generate-roadmap")
async def generate_ai_roadmap(data: GoalRequest):
    roadmap = await generate_roadmap(data.goal)
    return {"roadmap": roadmap}
