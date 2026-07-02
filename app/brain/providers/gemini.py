import google.generativeai as genai
from app.core.config import settings
from app.brain.interfaces import AIProvider
from app.brain.prompts import ATLAS_SYSTEM_PROMPT # Importamos la personalidad

class GeminiProvider(AIProvider):
    """
    Implementación específica para Gemini Pro con inyección de contexto.
    """
    def __init__(self):
        genai.configure(api_key=settings.gemini_api_key)
        self.model = genai.GenerativeModel('models/gemini-3.5-flash')

    def generate_response(self, prompt: str) -> str:
        # Combinamos la personalidad de A.T.L.A.S. con la pregunta del usuario
        full_prompt = f"{ATLAS_SYSTEM_PROMPT}\n\nSolicitud del usuario: {prompt}\n\nRespuesta de A.T.L.A.S.:"
        
        response = self.model.generate_content(full_prompt)
        return response.text