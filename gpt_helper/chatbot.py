import json
import tiktoken
from pathlib import Path
from typing import Literal

Role = Literal["user", "assistant", "system"]

class Chatbot:
    def __init__(self, file_path: str, system_msg: str = "Você é um assistente educado."):
        self.path = Path(file_path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

        self.messages: list[dict] = []
        self.max_tokens = 4096  # Limite de tokens para o modelo
        self.model = "gpt-4o-mini"
        self.encoding = tiktoken.encoding_for_model(self.model)

        if self.path.exists():
            self.messages = json.loads(self.path.read_text(encoding="utf-8"))
        else:
            self.messages = [{"role": "system", "content": system_msg}]
            self._save()
    
    async def ask(self, prompt: str) -> str:
        self.messages.append({"role": "user", "content": prompt})
        context = self._context_truncate()
        response = await async_stream_ask_with_context(context, self.model)
        self.messages = context + [{"role": "assistant", "content": response}]
        print(f"\nTotal tokens: {self._count_tokens(self.messages)}")
        self._save()

        return response
    
    def _save(self):
        """Salva as mensagens no arquivo JSON."""
        self.path.write_text(json.dumps(self.messages, ensure_ascii=False, indent=2), encoding="utf-8")
    
    def show_history(self):
        """Exibe o histórico de mensagens."""
        return [(msg["role"], msg["content"]) for msg in self.messages if msg["role"] != "system"]
    
    def _context_truncate(self) -> list[dict]:
        """Trunca o contexto para não exceder o limite de tokens do modelo."""
        msgs = self.messages[:]
        system = [msg for msg in msgs if msg["role"] == "system"]
        others = [msg for msg in msgs if msg["role"] != "system"]
        
        while self._count_tokens(system + others) > self.max_tokens and len(others) > 1:
            others.pop(0) # Remove the oldest message (user or assistant)
        
        return system + others
    
    def _count_tokens(self, messages: list[dict]) -> int:
        """Conta os tokens de uma lista de mensagens."""
        return sum(len(self.encoding.encode(msg["content"])) for msg in messages)
    
    def export(self, format: str = "md") -> Path:
        """Exporta o histórico de mensagens para um arquivo no formato especificado."""
        destination = self.path.with_suffix(f".{format}")
        lines = []

        for msg in self.messages:
            if msg["role"] == "system":
                continue
            prefix = f"**{msg['role'].capitalize()}:**" if format == "md" else f"{msg['role'].capitalize()}:"
            lines.append(f"{prefix} {msg['content']}\n")

        destination.write_text("\n".join(lines), encoding="utf-8")
        return destination

async def async_stream_ask_with_context(messages: list[dict], model: str = "gpt-4o-mini") -> str:
    """Envia uma pergunta para o modelo com o contexto das mensagens anteriores."""
    from .http_client import URL, HEADERS
    import httpx

    response = ""
    payload = {
        "model": model,
        "stream": True,
        "messages": messages
    }

    print("🤖 GPT: ", end="")

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
                    response += token
                    print(token, end="", flush=True)
                except Exception as e:
                    print(f"Erro ao processar a resposta: {e}")
                    continue

    print()  # Nova linha após o streaming
    return response.strip()