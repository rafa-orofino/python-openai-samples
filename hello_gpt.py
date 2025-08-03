import os
import json
from openai import OpenAI
from pathlib import Path

# recupera a chave exportada no shell
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(question: str) -> str:
    """Envia 'question' para a API e devolve a resposta do modelo."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente educado."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    log = []
    countPrompts = 0

    print("Digite sua pergunta (ou 'sair'):")

    while True:
        countPrompts += 1
        prompt = input(f"Pergunta #{countPrompts} 🤔 > ").strip()

        if prompt.lower() in {"sair", "exit", "quit", ""}:
            break

        answer = ask_llm(prompt)
        print(f"🤖 : {answer}")

        log.append({"#": countPrompts, "pergunta": prompt, "resposta": answer})

    from pprint import pprint

    perguntas_only = [e["pergunta"] for e in log] # list comprehension
    respostas_longas = {e["#"]: e["resposta"] for e in log if len(e["resposta"]) > 100} # dict comprehension + filter

    print("\nPerguntas feitas:")
    pprint(perguntas_only)

    print("\nRespostas com >100 caracteres:")
    pprint(respostas_longas)

    outfile = Path("log.json")
    outfile.write_text(json.dumps(log, indent=2, ensure_ascii=False))

    print(f"\n📁 Log salvo em {outfile.resolve()}")