"""Run all project tests and save their actual terminal output."""

from pathlib import Path
import subprocess
import sys


if len(sys.argv) != 2:
    raise SystemExit("Usage: python3 save_test_results.py evidence/before_tests.txt")
output_path = Path(sys.argv[1])
if output_path.exists():
    raise SystemExit("That evidence file already exists. Choose a new name.")
if not output_path.parent.is_dir():
    raise SystemExit("Create the evidence folder first.")
result = subprocess.run(
    [sys.executable, "-m", "unittest", "discover", "-v"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
)
output_path.write_text(result.stdout, encoding="utf-8")
print(result.stdout, end="")
print("Saved actual test output to {}".format(output_path))
raise SystemExit(result.returncode)
