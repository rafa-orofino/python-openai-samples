# Hello GPT
Hello GPT is a sample Python project demonstrating how to interact with the OpenAI API using both synchronous and asynchronous calls. It includes examples of chat completions, streaming, concurrent requests, and document indexing, leveraging the official OpenAI Python library and direct API consumption.

# Prerequisites
Before running this project, ensure you have:
- Python 3.8 or higher
- [Poetry](https://python-poetry.org/) (dependency and virtual environment manager)

# Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/rafa-orofino/python-openai-samples.git
   cd python-openai-samples
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

# Configuration
Set your OpenAI API key in the environment:
```bash
export OPENAI_API_KEY="your_api_key_here"
```

# Usage
### Running example scripts
Use Poetry to run any script in the `scripts/` folder:
```bash
poetry run python scripts/<script_name>.py
```
Available examples:
- `streaming.py`: Demonstrates OpenAI streaming responses
- `test_concurrency.py`: Tests concurrent requests
- `mem_chat.py`: Chat with memory storage
- `named_chat.py`: Persistent chats with session names
- `index_sample.py`: Indexing documents for later queries
- `ask_docs.py`: Asking questions against indexed documents

### Command-line Interface (CLI)
The `gpt_helper` package provides a CLI powered by Typer. Run:
```bash
poetry run python -m gpt_helper <command> [options]
```
Commands:
- `ask`: Send a prompt to the model
  - `--session TEXT`  Name for chat session
  - `--question TEXT`  Question to ask
- `export`: Export chat history to a file
  - `--session TEXT`  Name of chat session
  - `--format [md|txt]`  Output format (default: md)

### Web API
This project includes a FastAPI server exposing the same endpoints. Start it with:
```bash
poetry run uvicorn gpt_helper.api:app --reload
```
Access docs at `http://localhost:8000/docs`.

---
## Testing
Run the test suite with pytest:
```bash
poetry run pytest
```

## Project Structure
```
.
├── scripts/           Example scripts demonstrating SDK features
├── gpt_helper/        Core library: client, logger, API, CLI
├── tests/             Unit tests with pytest
├── hello_gpt.py       Simple CLI application example
├── pyproject.toml     Poetry config and dependencies
├── README.md          Project documentation
└── LICENSE            MIT License
```

## License
This project is licensed under the MIT License. See `LICENSE` for details.