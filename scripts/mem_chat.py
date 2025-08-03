import asyncio
from gpt_helper.chatbot import Chatbot

async def main():
    bot = Chatbot("historico.json")

    while True:
        user_input = input("\n🤔 You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        await bot.ask(user_input)

if __name__ == "__main__":
    asyncio.run(main())