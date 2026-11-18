"""Show the numeric range in a measurement file."""

import argparse
from export_records import load_records


def summarise(source_path):
    records = load_records(source_path)
    readings = []
    for record in records:
        readings.append(record["reading"])
    if not readings:
        return "Records: 0\nNo readings.\n"
    return "Records: {}\nLowest reading: {:.3f}\nHighest reading: {:.3f}\n".format(
        len(records), min(readings), max(readings)
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Input CSV file")
    args = parser.parse_args()
    print(summarise(args.source), end="")


if __name__ == "__main__":
    main()
