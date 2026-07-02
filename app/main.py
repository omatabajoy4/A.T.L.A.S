from fastapi import FastAPI
from app.core.config import settings

# Inicializamos la aplicación FastAPI
app = FastAPI(
    title="A.T.L.A.S. Core API",
    description="Artificial Thinking, Learning and Action System",
    version="1.0.0"
)

# Endpoint de Health-Check (Fase 1 del Roadmap)
@app.get("/health")
def health_check():
    """
    Ruta básica para comprobar que A.T.L.A.S. está encendido y leyendo variables.
    NUNCA devolvemos la API KEY aquí por seguridad.
    """
    return {
        "status": "online",
        "ai_provider": settings.ai_provider,
        "message": "A.T.L.A.S. Core is running."
    }