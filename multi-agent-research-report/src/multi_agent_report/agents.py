"""
Agent definitions for the multi-agent research report workflow.

Each agent has one clear responsibility:
1. Research Agent
2. Summary Agent
3. Report Writer Agent
4. Review Agent
"""

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from multi_agent_report.config import config


llm = ChatOpenAI(
    model=config.model_name,
    temperature=config.temperature,
)


def research_agent(state: dict) -> dict:
    """
    Researches the topic and returns useful information.
    """

    topic = state["topic"]

    prompt = f"""
You are a research agent.

Research this topic:
{topic}

Give clear and useful information.
Include:
- Background
- Key ideas
- Current importance
- Benefits
- Challenges
- Real-world examples

Write in simple English.
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {"research": response.content}


def summary_agent(state: dict) -> dict:
    """
    Summarizes the research into short and simple points.
    """

    research = state["research"]

    prompt = f"""
You are a summary agent.

Summarize this research in simple English:

{research}

Use short bullet points.
Keep only the most important ideas.
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {"summary": response.content}


def report_writer_agent(state: dict) -> dict:
    """
    Writes a structured report using the research and summary.
    """

    topic = state["topic"]
    research = state["research"]
    summary = state["summary"]

    prompt = f"""
You are a report writing agent.

Write a professional report about this topic:
{topic}

Use this research:
{research}

Use this summary:
{summary}

Report format:
1. Title
2. Introduction
3. Main Discussion
4. Benefits
5. Challenges
6. Real-World Applications
7. Conclusion

Write in clear and simple English.
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {"report": response.content}


def review_agent(state: dict) -> dict:
    """
    Reviews and improves the final report.
    """

    report = state["report"]

    prompt = f"""
You are a review agent.

Improve this report:

{report}

Improve:
- Grammar
- Clarity
- Structure
- Professional tone

Keep the language simple.
Return only the final report.
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {"final_report": response.content}
