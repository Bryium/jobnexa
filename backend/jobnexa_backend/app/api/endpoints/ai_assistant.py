from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_gemini import ask_gemini

router = APIRouter()

class QueryInput(BaseModel):
    query: str

@router.post("/mentor")
async def mentor(query_input: QueryInput):
    if not query.message.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    response = await ask_gemini(query.message)
    return {"reply": response}