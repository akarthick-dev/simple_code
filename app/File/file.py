from fastapi import UploadFile,File
from fastapi import APIRouter
import pymupdf
import easyocr
from app.ai.rag.emddeding import em_model

route = APIRouter()



pdf = "/home/karthick/Documents/Karthick - Python _ Backend Developer Resume.pdf"


@route.post('/file')
async def read(file: UploadFile = File(...)):
    pdf = await file.read()
    doc = pymupdf.open(stream=pdf,filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    chunks = chuck(text)
    vector = em_model(chunks)
    return {"data":chunks,"total":len(chunks),"vector":vector}



def chuck(text: str, chunk_size: int = 300, overlap: int = 50) -> list:
    words = text.split()
    if not words:
        return []

    chunks = []
    step = max(1, chunk_size - overlap)
    for start in range(0, len(words), step):
        chunk_words = words[start:start + chunk_size]
        chunks.append(" ".join(chunk_words))

        if start + chunk_size >= len(words):
            break

    return chunks




# Global EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)


@route.post('/image')
async def image(image: UploadFile = File(...)):
    image_bytes = await image.read()
    text = reader.readtext(image_bytes, detail=0)
    return {"text": " ".join(text),"lines": text}


