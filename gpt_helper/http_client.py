# gpt_helper/http_client.py

import os
import httpx
import asyncio
from.logger import logger

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
URL = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

async def async_ask(prompt: str, system_msg: str = "Você é um assistente educado.", model="gpt-4o-mini") -> str:
    """Envia uma pergunta para o modelo e retorna a resposta."""
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        logger.debug(f"Enviando: {prompt}")

        response = await client.post(URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]
        logger.info(f"Recebido: {len(content)} caracteres.")
        return content.strip()
    
async def async_stream_ask(prompt: str, system_msg: str = "Você é um assistente educado.", model="gpt-4o-mini") -> str:
    """Envia uma pergunta para o modelo e retorna a resposta em streaming."""
    payload = {
        "model": model,
        "stream": True,
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    }

    response = ""

    async with httpx.AsyncClient(timeout=60.0) as client:
        async with client.stream("POST", URL, headers=HEADERS, json=payload) as resp:
            async for row in resp.aiter_lines():
                if not row or not row.startswith("data: "):
                    continue

                row = row.removeprefix("data: ").strip()

                if row == "[DONE]":
                    break

                try:
                    token = httpx.Response(200, content=row).json()["choices"][0]["delta"].get("content", "")
                    print(token, end="", flush=True)
                    response += token
                except Exception as e:
                    logger.warning(f"Erro ao processar linha: {row} ({e})")

    print("\n\n[✓] Streaming concluído.")

    return response
