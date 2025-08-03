import asyncio
from gpt_helper.rag_bot import ask_with_context
from gpt_helper.ingestor import load_document

async def main():
    text_content = """
Python é uma linguagem de programação de alto nível, interpretada e de tipagem dinâmica.
Ela suporta múltiplos paradigmas de programação, incluindo programação orientada a objetos, imperativa e funcional.
Python é amplamente utilizada em ciência de dados, automação, desenvolvimento web e IA.
"""

    load_document("python_intro", text_content)

    prompt = input("Faça sua pergunta sobre os documentos: ")
    response = await ask_with_context(prompt)
    print(f"\n🧠 GPT com dados próprios:\n{response}")

if __name__ == "__main__":
    asyncio.run(main())