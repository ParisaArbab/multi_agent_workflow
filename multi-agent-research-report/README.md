# Multi-Agent Research Report Generator

A simple Python project that uses a multi-agent workflow to research a topic, summarize it, and generate a final report.

This project is built with:

- LangChain
- LangGraph
- OpenAI API
- Python

## Project Goal

The goal of this project is to show how different AI agents can work together in one workflow.

Instead of using one AI prompt for everything, this project separates the work into different agents. Each agent has one clear job.

## Agents

### 1. Research Agent

The Research Agent collects useful information about the topic.

It focuses on:

- Background
- Key ideas
- Current importance
- Benefits
- Challenges
- Real-world examples

### 2. Summary Agent

The Summary Agent takes the research and turns it into short, simple bullet points.

### 3. Report Writer Agent

The Report Writer Agent uses the research and summary to create a structured report.

The report includes:

- Title
- Introduction
- Main Discussion
- Benefits
- Challenges
- Real-World Applications
- Conclusion

### 4. Review Agent

The Review Agent improves the final report.

It checks:

- Grammar
- Clarity
- Structure
- Professional tone

## Workflow

The agents work in this order:

```text
Research Agent -> Summary Agent -> Report Writer Agent -> Review Agent
```

## Folder Structure

```text
multi-agent-research-report/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
│
└── src/
    └── multi_agent_report/
        ├── __init__.py
        ├── agents.py
        ├── config.py
        ├── workflow.py
        └── utils.py
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/multi-agent-research-report.git
cd multi-agent-research-report
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

For macOS or Linux:

```bash
source .venv/bin/activate
```

For Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Copy the example file:

```bash
cp .env.example .env
```

Then add your OpenAI API key inside `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the project

Because the source code is inside the `src` folder, run this command:

For macOS or Linux:

```bash
PYTHONPATH=src python main.py
```

For Windows PowerShell:

```powershell
$env:PYTHONPATH="src"; python main.py
```

### 6. Enter a topic

Example:

```text
Enter a research topic: Agentic AI in cybersecurity
```

The program will print the final report and save it here:

```text
outputs/final_report.md
```

## Example Output

```text
================ FINAL REPORT ================

# Agentic AI in Cybersecurity

## Introduction
Agentic AI is an advanced type of artificial intelligence that can plan tasks, use tools, and make decisions with less human input...
```

## Why This Project Is Useful

This project is useful because it shows practical agentic AI concepts:

- Multi-step reasoning
- Agent collaboration
- Task separation
- Report generation
- LangGraph workflow design

## Possible Improvements

You can improve this project by adding:

- Web search tools for real online research
- PDF export
- FastAPI backend
- Streamlit user interface
- Source citations
- Human approval before final report

## Technologies Used

- Python
- LangChain
- LangGraph
- OpenAI API
- dotenv


