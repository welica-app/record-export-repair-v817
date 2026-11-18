"""Export recorded measurements as a CSV file."""

import argparse
import csv


FIELDS = ("record_id", "position", "reading", "label")


def load_records(path):
    records = []
    with open(path, encoding="utf-8", newline="") as source:
        for row in csv.DictReader(source):
            records.append({
                "record_id": row["record_id"],
                "position": int(row["position"]),
                "reading": float(row["reading"]),
                "label": row.get("label") or "",
            })
    return records


def export_records(source_path, output_path):
    records = load_records(source_path)
    records.sort(key=lambda record: record["position"])
    with open(output_path, "w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(records)
    return len(records)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Input CSV file")
    parser.add_argument("output", help="New output CSV file")
    args = parser.parse_args()
    count = export_records(args.source, args.output)
    print("Exported {} records to {}".format(count, args.output))


if __name__ == "__main__":
    main()
