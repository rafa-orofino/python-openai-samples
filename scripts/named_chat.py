import asyncio
from gpt_helper.chatbot import Chatbot

async def main():
    name = input("Digite um nome para a asessão (ex: cliente_acme): ").strip().replace(" ", "_")
    file = f"chats/{name}.json"
    bot = Chatbot(file)

    while True:
        user_input = input("\n🤔 Você: ").strip()

        if user_input.lower() in ["sair", "exit", "quit"]:
            print("👋 Até logo!")
            break

        if user_input.startswith("/export"):
            format = user_input.split(" ", 1)[-1] if " " in user_input else "md"
            path = bot.export(format)
            print(f"📁 Histórico exportado para {path.resolve()}")
            continue

        if user_input == "/history":
            for role, content in bot.show_history():
                print(f"{role.capitalize()}: {content}")
            continue

        if user_input == "/reset":
            bot.messages = [{"role": "system", "content": "Você é um assistente educado."}]
            bot._save()
            print("⚠️ Histórico da conversa foi reiniciado.")
            continue

        await bot.ask(user_input)
    
if __name__ == "__main__":
    asyncio.run(main())