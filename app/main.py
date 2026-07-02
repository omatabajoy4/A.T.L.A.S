from fastapi import FastAPI
from pydantic import BaseModel
from brain.providers.gemini import GeminiProvider

app = FastAPI(
    title="A.T.L.A.S. Core API",
    description="Artificial Thinking, Learning and Action System",
    version="1.0.0"
)

brain_provider = GeminiProvider()

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_with_atlas(request: ChatRequest):
    response = brain_provider.generate_response(request.prompt)
    return {"response": response}