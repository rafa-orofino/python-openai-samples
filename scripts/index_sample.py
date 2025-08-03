from gpt_helper.ingestor import load_document

text_content = """
Python is a high-level, interpreted programming language with dynamic typing.
It supports multiple programming paradigms, including object-oriented, imperative, and functional.
Python is widely used in data science, automation, web development, and AI.
"""

load_document("python_intro", text_content)