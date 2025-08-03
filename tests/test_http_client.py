# test/test_http_client.py
import pytest
import asyncio
from gpt_helper.http_client import async_ask

@pytest.mark.asyncio
async def test_async_ask_returns_text():
    """Test if async_ask returns a non-empty string."""
    response = await async_ask("Qual linguagem estamos aprendendo?")
    assert len(response) > 0