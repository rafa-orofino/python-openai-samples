import asyncio
from gpt_helper.http_client import async_ask

questions = [
    "Qual a capital da Inglaterra?",
    "Qual o maior oceano d mundo?",
    "Quem escreveu Dom Casmurro?",
    "O que é aprendizado supervisionado?",
    "Me explique o que é OpenAI."
]

async def main():
    tasks = [async_ask(q) for q in questions]
    responses = await asyncio.gather(*tasks)

    for i, reponse in enumerate(responses, 1):
        print(f"\n[{i}] {reponse[:120]}...")

if __name__ == "__main__":
    asyncio.run(main())