"""
Configuration file for the multi-agent research report project.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    """Application settings."""

    model_name: str = "gpt-4o-mini"
    temperature: float = 0.3
    output_file: str = "outputs/final_report.md"


config = AppConfig()
