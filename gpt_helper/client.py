# gpt_helper/client.py
from __future__ import annotations

import tiktoken
from openai import OpenAI
from openai.types.chat import ChatCompletion
from .logger import logger

_COST_PER_1K_TOKENS = 0.002 # USD, gpt-4o-mini - ajuste quando mudar modelo

class GPTClient:
    """Client to interact with the OpenAI API."""
    def __init__(self, model: str = "gpt-4o-mini"):
        """Initialize the client with the specified model."""
        self.model = model
        self.client = OpenAI()
        self.encoding = tiktoken.encoding_for_model(model)

    def ask(self, prompt: str, system_msg: str | None = None) -> str:
        """Send a prompt to the model and return the response content."""
        messages = []
        
        if system_msg:
            messages.append({"role": "system", "content": system_msg})

        messages.append({"role": "user", "content": prompt})

        logger.debug("Enviando para %s: %s", self.model, messages)

        resp: ChatCompletion = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )

        content = resp.choices[0].message.content.strip()
        usage = resp.usage.total_tokens if resp.usage else self._count_tokens(messages + [{"role": "assistant", "content": content}])
        cost = usage / 1000 * _COST_PER_1K_TOKENS
        logger.info("Tokens: %d | Custo aprox: $%.4f", usage, cost)

        return content
    
    # fallback se API não trouxer usage
    def _count_tokens(self, messages: list[dict]) -> int:
        """Count tokens in a list of messages using model encoding."""
        return sum(len(self._encoding.encode(m["content"])) for m in messages)
    
# Função utilitária - padrão similar ao que usávamos
_client_singleton: GPTClient | None = None

def ask_llm(prompt: str, system_msg: str | None = "Você é um assistente educado.") -> str:
    """Send a question to the model and return its answer."""
    global _client_singleton

    if _client_singleton is None:
        _client_singleton = GPTClient()
    
    return _client_singleton.ask(prompt, system_msg=system_msg)