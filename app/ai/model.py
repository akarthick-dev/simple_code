from functools import lru_cache

from google import genai
from app.core.config import Setting


@lru_cache
def get_client() -> genai.Client:
    """Create the Gemini client only when it is needed."""
    if not Setting.GEMINI_API_KEY:
        raise RuntimeError("GOOGLE_API_KEY is not configured")
    return genai.Client(api_key=Setting.GEMINI_API_KEY)


def gemini_llm(prompt: str) -> str:
    """Generate text using the configured Gemini model."""
    response = get_client().models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
    )
    return response.text or ""

