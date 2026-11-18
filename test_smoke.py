"""Basic checks that the starter can run and write a CSV file."""

import csv
from pathlib import Path
import tempfile
import unittest

from export_records import FIELDS, export_records


class ExportSmokeTests(unittest.TestCase):
    def test_writes_rows_in_position_order(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "source.csv"
            output = Path(folder) / "output.csv"
            source.write_text(
                "record_id,position,reading,label\n"
                "rec-b,2,2.5,Room B\n"
                "rec-a,1,1.5,Room A\n",
                encoding="utf-8",
            )
            self.assertEqual(export_records(source, output), 2)
            with output.open(encoding="utf-8", newline="") as result:
                reader = csv.DictReader(result)
                self.assertEqual(reader.fieldnames, list(FIELDS))
                rows = list(reader)
            self.assertEqual([row["record_id"] for row in rows], ["rec-a", "rec-b"])
            self.assertEqual([row["label"] for row in rows], ["Room A", "Room B"])

    def test_empty_file_keeps_header(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "source.csv"
            output = Path(folder) / "output.csv"
            source.write_text("record_id,position,reading,label\n", encoding="utf-8")
            self.assertEqual(export_records(source, output), 0)
            with output.open(encoding="utf-8", newline="") as result:
                self.assertEqual(list(csv.reader(result)), [list(FIELDS)])


if __name__ == "__main__":
    unittest.main()
