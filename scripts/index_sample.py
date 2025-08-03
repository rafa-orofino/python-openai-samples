from gpt_helper.ingestor import load_document

text_content = """
Python é uma linguagem de programação de alto nível, interpretada e de tipagem dinâmica.
Ela suporta múltiplos paradigmas de programação, incluindo programação orientada a objetos, imperativa e funcional.
Python é amplamente utilizada em ciência de dados, automação, desenvolvimento web e IA.
"""

load_document("python_intro", text_content)