from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import auth, profile, roadmap, recommender, ai_assistant
from app.database import create_db_and_tables

app = FastAPI(title="JobNexa API", version="1.0")

# Cors for frontend access
origins = ["http://localhost:3000", "https://your-frontend-domain.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(profile.router, prefix="/api/profile", tags=["Profile"])
app.include_router(roadmap.router, prefix="/api/roadmap", tags=["Roadmap"])
app.include_router(recommender.router, prefix="/api/recommender", tags=["Recommender"])
app.include_router(ai_assistant.router, prefix="/api/ai", tags=["AI Mentor"])

@app.on_event("startup")
async def startup_event():
    # Create database tables if they do not exist
    await create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "JobNexa Backend is running"}