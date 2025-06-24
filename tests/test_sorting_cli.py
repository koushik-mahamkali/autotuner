import subprocess
import sys

def test_sort_cli_output():
    result = subprocess.run(
        [sys.executable, "-m", "autotuner_core.cli.sort_cli", "10", "3", "2", "1"],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )

    print("\nSTDOUT:\n", result.stdout)
    print("\nSTDERR:\n", result.stderr)

    assert result.returncode == 0, f"Process failed with return code {result.returncode}"
    assert "Sorted" in result.stdout or "✅ Sorted" in result.stdout, "Expected output not found"
