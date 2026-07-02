# brain/providers/gemini.py

import google.generativeai as genai
from app.core.config import settings
from brain.interfaces import BrainProvider
from brain.prompts import ATLAS_SYSTEM_PROMPT  # Importamos su personalidad

class GeminiProvider(BrainProvider):
    def __init__(self):
        # Configurar la API Key global
        genai.configure(api_key=settings.gemini_api_key)
        
        # Inicializar el modelo inyectando la instrucción de sistema de A.T.L.A.S.
        self.model = genai.GenerativeModel(
            model_name='models/gemini-3.5-flash',
            system_instruction=ATLAS_SYSTEM_PROMPT  # ¡Aquí ocurre la magia!
        )

    def generate_response(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text