from dotenv import load_dotenv
import os
load_dotenv()

class Setting:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
    
    
    
