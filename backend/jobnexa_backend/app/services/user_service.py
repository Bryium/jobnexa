from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash, verify_password

async def get_user_by_email(session: AsyncSession, email: str):
    result = await session.execute(select(User).where(User.email == email))
    return result.scalars().first()

async def create_user(session: AsyncSession, user_in: UserCreate):
    hashed_pw = get_password_hash(user_in.password)
    user = User(full_name=user_in.full_name, email=user_in.email, hashed_password=hashed_pw)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user