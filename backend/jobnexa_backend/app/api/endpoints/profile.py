from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserOut
from app.services.utils import get_current_user
from app.database import get_db
router = APIRouter(prefix="/profile", tags=["profile"])

@router.get("/", response_model=UserOut)
def get_profile(current_user: UserOut = Depends(get_current_user)):
    return current_user
