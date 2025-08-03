# gpt_helper/api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Ask(BaseModel):
    """Request body schema for the /ask endpoint."""
    session: str  # Name of the chat session (used for file storage)
    prompt: str   # Text prompt to send to the chatbot

@app.post("/ask")
async def ask_chatbot(ask: Ask):
    """Handle POST /ask: send prompt to Chatbot, save conversation history, and return response."""
    try:
        from gpt_helper.chatbot import Chatbot
        bot = Chatbot(f"chats/{ask.session}.json")
        response = await bot.ask(ask.prompt)
        return {"response": response, "session": ask.session}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))