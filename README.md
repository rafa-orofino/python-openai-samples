# Hello GPT
Este é um projeto de exemplo criado para aprendizado de python, que demonstra como interagir com a API da OpenAI usando Python, utilizando tanto chamadas síncronas quanto assíncronas. O projeto inclui exemplos de uso da API de chat, streaming e concorrência, utilizando biblioteca da OpenAI e consumo direto da API.

# Pré-requisitos
Antes de executar o projeto, certifique-se de ter os seguintes pré-requisitos instalados:

- Python 3.8 ou superior
- Poetry (gerenciador de dependências e ambientes virtuais)

# Instalação
1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. Instale as dependências:
   ```bash
   poetry install
   ```

3. Ative o ambiente virtual:
   ```bash
   poetry shell
   ```

# Configuração
Certifique-se de definir a variável de ambiente `OPENAI_API_KEY` com sua chave de API da OpenAI. Você pode fazer isso no terminal antes de executar o projeto:
```bash
export OPENAI_API_KEY="sua_chave_aqui"
```

# Execução
Para executar o projeto, você pode usar o seguinte comando:
```bash
poetry run python scripts/<script_desejado>.py
```

## Scripts Disponíveis
- `streaming.py`: Demonstra como usar a API de streaming da OpenAI.
- `test_concorrencia.py`: Testes de concorrência para a API.
- `mem_chat.py`: Demonstra como usar o modelo de chat com memória.
- `named_chat.py`: Demonstra como usar o modelo de chat com nomes personalizados para sessões.
- `index_sample.py`: Exemplo de como indexar documentos para consulta posterior.
- `ask_docs.py`: Demonstra como fazer perguntas sobre documentos indexados.

# CLI
Você também pode interagir com a API usando a interface de linha de comando (CLI) fornecida pelo Typer. Para usar a CLI, execute o seguinte comando:
```bash
poetry run python -m gpt_helper <comando> <argumentos>
```

## Comandos Disponíveis
- `ask`: Faz uma pergunta ao modelo de linguagem.
    - nome_sessão: Nome da sessão de chat.
    - pergunta: Pergunta a ser feita ao modelo.
- `export`: Exporta o histórico de chat para um arquivo.
    - nome_sessão: Nome da sessão de chat.
    - formato (opcional, default: md): Formato de exportação (ex: md ou txt).

# API
A API do projeto é baseada no FastAPI e pode ser executada localmente. Para iniciar o servidor, execute:
```bash
poetry run uvicorn gpt_helper.api:app --reload
```