from pathlib import Path

from multi_agent_report.utils import save_report


def test_save_report_creates_markdown_file(tmp_path):
    output_file = tmp_path / "final_report.md"
    saved_path = save_report("# Test Report", str(output_file))

    assert saved_path == output_file
    assert output_file.exists()
    assert output_file.read_text(encoding="utf-8") == "# Test Report"
