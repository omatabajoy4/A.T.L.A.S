from abc import ABC, abstractmethod

class AIProvider(ABC):
    """
    Capa de abstracción obligatoria (ADR-002).
    Cualquier IA que A.T.L.A.S. use en el futuro debe cumplir con este molde.
    """
    
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """Toma un texto (prompt) y devuelve la respuesta generada por la IA."""
        pass