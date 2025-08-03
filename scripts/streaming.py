import asyncio
from gpt_helper.http_client import async_stream_ask

async def main():
    prompt = "Me explique resumidamente o que é IA generativa."
    await async_stream_ask(prompt)

if __name__ == "__main__":
    asyncio.run(main())