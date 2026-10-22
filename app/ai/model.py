from google import genai
from app.core.config import Setting

client = genai.Client(api_key=Setting.GENAI_API_KEY)

def gemini_llm(prompt:str):
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return interaction.output_text



 

