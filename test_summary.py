"""Keep the existing numeric summary working while repairing the export."""

from pathlib import Path
import tempfile
import unittest

from summary_readings import summarise


class SummaryTests(unittest.TestCase):
    def test_numeric_range(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / "measurements.csv"
            source.write_text(
                "record_id,position,reading,label\n"
                "a,1,2.500,A\n"
                "b,2,10.000,B\n"
                "c,3,-1.250,C\n",
                encoding="utf-8",
            )
            self.assertEqual(
                summarise(source),
                "Records: 3\nLowest reading: -1.250\nHighest reading: 10.000\n",
            )


if __name__ == "__main__":
    unittest.main()
