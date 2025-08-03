import asyncio
from gpt_helper.chatbot import Chatbot

async def main():
    name = input("Enter a session name (e.g. client_acme): ").strip().replace(" ", "_")
    file = f"chats/{name}.json"
    bot = Chatbot(file)

    while True:
        user_input = input("\n🤔 You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        if user_input.startswith("/export"):
            format = user_input.split(" ", 1)[-1] if " " in user_input else "md"
            path = bot.export(format)
            print(f"📁 History exported to {path.resolve()}")
            continue

        if user_input == "/history":
            for role, content in bot.show_history():
                print(f"{role.capitalize()}: {content}")
            continue

        if user_input == "/reset":
            bot.messages = [{"role": "system", "content": "You are a polite assistant."}]
            bot._save()
            print("⚠️ Conversation history has been reset.")
            continue

        await bot.ask(user_input)
    
if __name__ == "__main__":
    asyncio.run(main())