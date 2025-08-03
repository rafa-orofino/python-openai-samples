# gpt_helper/__main__.py
import typer
import asyncio
from gpt_helper.chatbot import Chatbot

app = typer.Typer(help="Chatbot com histórico e memória locais.")

@app.command()
def ask(
    name: str = typer.Argument(..., help="Nome da sessão de chat (ex: cliente_acme) que será usado para salvar o histórico."),
    prompt: str = typer.Argument(..., help="Pergunta ou comando para o chatbot.")
):
    """Faz uma pergunta ao chatbot e salva o histórico localmente."""
    file = f"chats/{name}.json"
    bot = Chatbot(file)

    async def run():
        response = await bot.ask(prompt)

    asyncio.run(run())

@app.command()
def export(
    name: str = typer.Argument(...),
    format: str = typer.Option("md", help="Formato de exportação (ex: md ou txt).")
):
    """Exporta o histórico de chat para um arquivo."""
    file = f"chats/{name}.json"
    bot = Chatbot(file)

    path = bot.export(format)
    typer.echo(f"📁 Histórico exportado para {path.resolve()}")

if __name__ == "__main__":
    app()    