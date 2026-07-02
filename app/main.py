from fastapi import FastAPI
from pydantic import BaseModel
from app.core.config import settings
from app.brain.providers.gemini import GeminiProvider

# Inicializamos la aplicación FastAPI
app = FastAPI(
    title="A.T.L.A.S. Core API",
    description="Artificial Thinking, Learning and Action System",
    version="1.0.0"
)

# Instanciamos el cerebro (nuestro adaptador seguro)
brain_provider = GeminiProvider()

# Definimos cómo debe ser la estructura de la pregunta (Pydantic)
class ChatRequest(BaseModel):
    prompt: str

# Endpoint 1: Health-Check
@app.get("/health")
def health_check():
    return {
        "status": "online",
        "ai_provider": settings.ai_provider,
        "message": "A.T.L.A.S. Core is running."
    }

# Endpoint 2: Hablar con A.T.L.A.S. (El nuevo cerebro)
@app.post("/chat")
def chat_with_atlas(request: ChatRequest):
    """
    Envía un mensaje a A.T.L.A.S. y recibe su respuesta inteligente.
    """
    # Usamos la capa de abstracción para pensar la respuesta
    response_text = brain_provider.generate_response(request.prompt)
    
    # Devolvemos la respuesta estructurada
    return {
        "response": response_text
    }