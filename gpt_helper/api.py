# gpt_helper/api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gpt_helper.chatbot import Chatbot
import asyncio

app = FastAPI()

class Ask(BaseModel):
    session: str
    prompt: str

@app.post("/ask")
async def ask_chatbot(ask: Ask):
    """Faz uma pergunta ao chatbot e salva o histórico localmente."""
    try:
        bot = Chatbot(f"chats/{ask.session}.json")
        response = await bot.ask(ask.prompt)
        return {"response": response, "session": ask.session}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))