from gpt_helper.ingestor import query_by_similarity
from gpt_helper.http_client import async_stream_ask

async def ask_with_context(prompt: str):
    """
    Ask the LLM with context from the indexed documents.
    
    Args:
        prompt (str): The question to ask.
    
    Returns:
        str: The response from the LLM.
    """
    chuncks = query_by_similarity(prompt, n_results=3)
    context = "\n\n".join(chuncks)
    prompt = f"""Você deve responder à pergunta abaixo com base no conteúdo fornecido. Se o conteúdo não for suficiente, diga que não sabe.

### Conteúdo:
{context}

### Pergunta:
{prompt}
"""
    return await async_stream_ask(prompt, system_msg="Você é um assistente baseado em documentos internos.")