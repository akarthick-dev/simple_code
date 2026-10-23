from typing import Annotated

from fastapi import FastAPI, File, UploadFile

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
    """Confirm whether the configured API keys are available without exposing them."""
    return {
        "groq_configured": bool(Setting.GROQ_API_KEY),
        "gemini_configured": bool(Setting.GEMINI_API_KEY),
    }

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@app.post("/uploadfile2/")
async def create_upload_file2(file: UploadFile):
    content = await file.read()
    return {"filename": file.filename, "file_size": len(content)}
