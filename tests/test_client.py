# tests/test_client.py
import types
import pytest
from gpt_helper import ask_llm
import gpt_helper.client as client_mod

class DummyResp:
    def __init__(self, text):
        self.choices = [types.SimpleNamespace(message=types.SimpleNamespace(content=text))]
        self.usage = types.SimpleNamespace(total_tokens=5)

@pytest.fixture(autouse=True)
def patch_openai(monkeypatch):
    """Mock OpenAI client to avoid actual API calls."""
    # intercepta OpenAI.chat.completions.create
    def fake_create(*_, **__):
        return DummyResp("Pong")
    
    fake_chat = types.SimpleNamespace(completions=types.SimpleNamespace(create=fake_create))
    monkeypatch.setattr(client_mod, "OpenAI", lambda *_, **__: types.SimpleNamespace(chat=fake_chat))

def test_ask_llm_returns_pong():
    """Test if ask_llm returns 'Pong'."""
    assert ask_llm("Ping", system_msg=None) == "Pong"