"""
Utility functions for saving the generated report.
"""

from pathlib import Path


def save_report(report: str, output_path: str) -> Path:
    """
    Saves the final report as a Markdown file.
    """

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")
    return path
