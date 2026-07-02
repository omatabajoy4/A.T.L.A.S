import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.gemini_api_key)

print("Modelos disponibles:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Nombre: {m.name}")