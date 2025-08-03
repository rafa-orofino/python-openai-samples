import os
import json
from openai import OpenAI
from pathlib import Path

# retrieve API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(question: str) -> str:
    """Send the 'question' to the API and return the model's response."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a polite assistant."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    log = []
    countPrompts = 0

    print("Enter your question (or 'exit'): ")

    while True:
        countPrompts += 1
        prompt = input(f"Question #{countPrompts} 🤔 > ").strip()

        if prompt.lower() in {"sair", "exit", "quit", ""}:
            break

        answer = ask_llm(prompt)
        print(f"🤖 : {answer}")

        log.append({"#": countPrompts, "question": prompt, "answer": answer})

    from pprint import pprint

    questions_only = [e["question"] for e in log] # list comprehension
    long_responses = {e["#"]: e["answer"] for e in log if len(e["answer"]) > 100} # dict comprehension + filter

    print("\nQuestions asked:")
    pprint(questions_only)

    print("\nResponses longer than 100 characters:")
    pprint(long_responses)

    outfile = Path("log.json")
    outfile.write_text(json.dumps(log, indent=2, ensure_ascii=False))

    print(f"\n📁 Log saved at {outfile.resolve()}")