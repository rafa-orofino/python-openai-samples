import asyncio
from gpt_helper.http_client import async_ask

questions = [
    "What is the capital of England?",
    "What is the largest ocean in the world?",
    "Who wrote 'Dom Casmurro'?",
    "What is supervised learning?",
    "Explain what OpenAI is."
]

async def main():
    tasks = [async_ask(q) for q in questions]
    responses = await asyncio.gather(*tasks)

    for i, reponse in enumerate(responses, 1):
        print(f"\n[{i}] {reponse[:120]}...")

if __name__ == "__main__":
    asyncio.run(main())