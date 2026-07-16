"""
LangGraph workflow for the multi-agent research report system.
"""

from typing import TypedDict

from langgraph.graph import END, StateGraph

from multi_agent_report.agents import (
    research_agent,
    report_writer_agent,
    review_agent,
    summary_agent,
)


class ResearchState(TypedDict, total=False):
    """Shared state passed between agents."""

    topic: str
    research: str
    summary: str
    report: str
    final_report: str


def build_workflow():
    """
    Builds and compiles the multi-agent workflow.
    """

    workflow = StateGraph(ResearchState)

    workflow.add_node("research_agent", research_agent)
    workflow.add_node("summary_agent", summary_agent)
    workflow.add_node("report_writer_agent", report_writer_agent)
    workflow.add_node("review_agent", review_agent)

    workflow.set_entry_point("research_agent")

    workflow.add_edge("research_agent", "summary_agent")
    workflow.add_edge("summary_agent", "report_writer_agent")
    workflow.add_edge("report_writer_agent", "review_agent")
    workflow.add_edge("review_agent", END)

    return workflow.compile()
