"""Try CSV files, numeric sorting and an optional column on a separate example."""

import csv
from pathlib import Path
import tempfile


source_path = Path(__file__).with_name("example_queue.csv")
with source_path.open(encoding="utf-8", newline="") as source:
    rows = list(csv.DictReader(source))


def queue_number(row):
    return int(row["queue"])


rows.sort(key=queue_number)
for row in rows:
    row["note"] = row.get("note", "")

with tempfile.TemporaryDirectory() as folder:
    output_path = Path(folder) / "queue_output.csv"
    with output_path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=("ticket", "queue", "note"))
        writer.writeheader()
        writer.writerows(rows)
    print(output_path.read_text(encoding="utf-8"), end="")

print("The temporary example output has been removed.")
