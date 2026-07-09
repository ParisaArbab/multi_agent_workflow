# MCP AI Assistant

An MCP-based AI assistant project that connects an AI model to external tools.

This project shows how to build a small tool server using the **Model Context Protocol (MCP)**. The server exposes tools that an AI assistant can call when it needs to do real work, such as calculating, checking weather, reading a file, or fetching a web page.

## Features

- MCP server built with `FastMCP`
- External tool examples:
  - Calculator
  - Weather lookup
  - Local text file reader
  - URL text fetcher
- Clean Python package structure
- Simple demo script
- Unit tests
- GitHub Actions CI workflow
- `.env.example` file for configuration

## Project Structure

```text
mcp-ai-assistant/
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── examples/
│   ├── claude_desktop_config.json
│   └── sample_notes.txt
├── src/
│   └── mcp_ai_assistant/
│       ├── __init__.py
│       ├── config.py
│       ├── demo.py
│       ├── server.py
│       └── tool_logic.py
├── tests/
│   └── test_tool_logic.py
├── .env.example
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## What Each File Does

### `src/mcp_ai_assistant/server.py`

This is the MCP server. It exposes tools that an AI assistant can use.

Available tools:

- `calculate(expression)`: solves simple math expressions.
- `weather(city)`: gets weather from a public web service.
- `read_file(path, max_chars)`: reads a local text file.
- `fetch_url(url, max_chars)`: fetches a web page and returns a short text preview.

### `src/mcp_ai_assistant/tool_logic.py`

This file contains the real logic behind the tools.

The MCP server imports functions from this file. This makes the code easier to test because the tool logic is separate from the MCP server code.

### `src/mcp_ai_assistant/demo.py`

This is a simple demo script. It does not need an LLM. It directly calls the same functions used by the MCP tools.

Use it to quickly check that the project works.

### `src/mcp_ai_assistant/config.py`

This file loads environment variables from `.env`.

### `examples/claude_desktop_config.json`

This is an example MCP configuration for Claude Desktop or any MCP-compatible client. You may need to adjust the Python path depending on your system.

### `examples/sample_notes.txt`

A small sample file for testing the `read_file` tool.

### `tests/test_tool_logic.py`

Unit tests for calculator and file-reading logic.

### `.github/workflows/python-ci.yml`

A GitHub Actions workflow that installs the project, runs tests, and checks code style.

## Requirements

- Python 3.10 or higher
- pip

## Setup

Clone the repository:

```bash
git clone https://github.com/your-username/mcp-ai-assistant.git
cd mcp-ai-assistant
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the project:

```bash
pip install -e ".[dev]"
```

Create your environment file:

```bash
cp .env.example .env
```

## Run the Demo

```bash
python -m mcp_ai_assistant.demo
```

This runs a simple calculator test and a weather lookup.

## Run the MCP Server

```bash
python -m mcp_ai_assistant.server
```

The server runs over stdio, which is the common setup for local MCP clients.

## Connect to an MCP Client

You can connect this server to an MCP-compatible client.

Example configuration:

```json
{
  "mcpServers": {
    "mcp-ai-assistant-tools": {
      "command": "python",
      "args": ["-m", "mcp_ai_assistant.server"],
      "env": {}
    }
  }
}
```

If your client cannot find the package, run the client from the project folder or install the project first:

```bash
pip install -e .
```

## Example Tool Requests

After connecting the server to an MCP client, try questions like:

```text
Calculate 25 * (7 + 3).
```

```text
What is the weather in New York?
```

```text
Read examples/sample_notes.txt and summarize it.
```

```text
Fetch https://example.com and tell me what it says.
```

## Run Tests

```bash
pytest
```

Run code style check:

```bash
ruff check .
```

## How This Project Works

The project has three main parts:

1. **MCP server**: exposes tools to the assistant.
2. **Tool logic**: contains normal Python functions for each tool.
3. **MCP client**: an external app, such as Claude Desktop or another MCP-compatible assistant, can call the server tools.

The AI assistant does not need to know how each tool is built. It only sees the tool names, descriptions, and inputs. When the assistant needs help, it asks the MCP server to run the correct tool.

## Possible Improvements

You can extend this project by adding:

- Database search tool
- Google Drive tool
- GitHub issue reader
- Email draft tool
- RAG tool with ChromaDB
- Authentication and permission checks
- More detailed logging
- Docker support

## Safety Notes

Be careful with tools that read files or call external services.

For production use, add:

- File access limits
- URL allowlists or blocklists
- Rate limits
- Better error handling
- User permission checks
- Logging and monitoring

## License

This project is licensed under the MIT License.
