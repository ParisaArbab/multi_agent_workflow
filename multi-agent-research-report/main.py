"""
Main entry point for the multi-agent research report generator.
"""

from dotenv import load_dotenv

from multi_agent_report.config import config
from multi_agent_report.utils import save_report
from multi_agent_report.workflow import build_workflow


def main() -> None:
    """
    Runs the full workflow.
    """

    load_dotenv()

    topic = input("Enter a research topic: ").strip()

    if not topic:
        print("Please enter a valid topic.")
        return

    app = build_workflow()

    result = app.invoke({"topic": topic})
    final_report = result["final_report"]

    saved_path = save_report(final_report, config.output_file)

    print("\n================ FINAL REPORT ================\n")
    print(final_report)
    print(f"\nReport saved to: {saved_path}")


if __name__ == "__main__":
    main()
