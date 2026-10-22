from fastapi import FastAPI
from app.core.config import Setting
app = FastAPI()

@app.get("/")
async def landing_page():
    return {"Hello": "World"}


@app.get("/health")
async def health_check():
    return {"status": "health"}

@app.get("/api_key")
async def get_api_key():
    return {"api_key": [Setting.GROQ_API_KEY,Setting.GEMINI_API_KEY]}   