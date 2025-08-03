import asyncio
from gpt_helper.chatbot import Chatbot

async def main():
    bot = Chatbot("historico.json")

    while True:
        user_input = input("\n🤔 Você: ").strip()

        if user_input.lower() in ["sair", "exit", "quit"]:
            print("👋 Até logo!")
            break

        await bot.ask(user_input)

if __name__ == "__main__":
    asyncio.run(main())