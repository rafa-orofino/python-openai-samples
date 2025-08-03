"""Retrieval-augmented generation (RAG) helper: query indexed docs and ask LLM with context."""
from gpt_helper.ingestor import query_by_similarity
from gpt_helper.http_client import async_stream_ask

async def ask_with_context(prompt: str):
    """Query indexed documents for context and ask the LLM with streaming response.

    Args:
        prompt (str): Text question to ask the model.

    Returns:
        str: Complete assistant response."""
    chuncks = query_by_similarity(prompt, n_results=3)
    context = "\n\n".join(chuncks)
    # Build the system prompt to instruct the model
    prompt = f"""You should answer the question below based on the provided context. If the context is insufficient, respond with 'I don't know.'

### Conteúdo:
{context}

### Pergunta:
{prompt}
"""
    return await async_stream_ask(
        prompt,
        system_msg="You are a document-based assistant."
    )