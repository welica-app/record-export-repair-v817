# Repair a record export app

An equipment reviewer needs an export to compare with the original measurement records. You will investigate this small app, choose a repair and check it against the written requirements.

## 1. Get the files

On this repository page, choose **Code**, then **Download ZIP**. You do not need an account. Extract the ZIP into a folder you can write to, such as Documents. On Windows, right click the ZIP and choose **Extract All**. On macOS, open the ZIP. On Linux, use your file manager's extract action.

Open the extracted folder. It may contain another folder. Continue until you see `export_records.py`, `measurements.csv` and `test_smoke.py` together. This is the starter folder. Keep these original files so you can compare your work later.

## 2. Open a terminal in the starter folder

A terminal is a window where you type commands. Run each command below on its own line and press Enter. Leave the terminal open as you work.

- **Windows:** Open the starter folder in File Explorer. Click the address bar, type `powershell` and press Enter. A terminal opens in that folder. Run `Get-Location`, then `Get-ChildItem` to see the folder and its files.
- **macOS:** Open Terminal using your app search. Type `cd `, including the space. Drag the starter folder from Finder into the terminal, then press Enter. Run `pwd`, then `ls`.
- **Linux:** Open the starter folder in your file manager. If it has **Open in Terminal**, choose that action. Otherwise open Terminal from your app list and run `cd "/full/path/to/your/starter/folder"`, replacing the path with the folder's actual path. Run `pwd`, then `ls`.

If the file list does not include `export_records.py`, you are in the wrong folder. In your file manager, find the folder containing that file and copy its full path. In the terminal run `cd "PASTE THE FULL FOLDER PATH HERE"`, replacing the words inside the quotes. Keep the quotes because folder names can contain spaces. List the files again before continuing.

## 3. Find Python

You need Python 3.9 or later. Try these commands one at a time until one prints a supported version, such as `Python 3.12.0`:

| System | Commands to try |
| --- | --- |
| Windows | `py -3 --version`, then `python --version`, then `python3 --version`. |
| macOS or Linux | `python3 --version`, then `python --version`. |

A version beginning with 2, or 3 followed by a number below 9, is too old for this starter. A missing command means the terminal cannot find Python under that name. Try the next command. If Windows opens an app store instead of printing a version, close it and try the next command.

If none works, install Python first. On Windows or macOS, use the installer for your system from [the official Python downloads page](https://www.python.org/downloads/). On Windows, enable the installer's option to add Python to PATH if it offers one. PATH is the list of folders the terminal searches for commands. On Linux, open your system's software manager, search for Python 3 and install it. You may need the computer owner's help if you cannot install software.

After installing, close the terminal and open it in the starter folder again. Repeat the version check. Continue only when a command prints Python 3.9 or later.

The commands below use `python3`. Replace **only** `python3` with the command that worked for you. For example, on Windows the first command might be `py -3 export_records.py measurements.csv evidence/before.csv`. Keep `-3` each time if you use `py -3`.

## 4. Run the unchanged app first

Create a folder for evidence by running `mkdir evidence`. If it already exists, keep its contents and choose unused output filenames. The output must be different from the input. The app replaces an existing output file, so do not reuse an evidence filename you want to keep.

Run:

```text
python3 export_records.py measurements.csv evidence/before.csv
python3 -m unittest -v test_smoke.py
```

The first command should print `Exported 8 records to evidence/before.csv`. The second should name two tests, mark both `ok`, then end with `Ran 2 tests` and `OK`. The elapsed time can differ. This confirms that the unchanged starter runs. It does not establish that the app meets every requirement.

Open `evidence/before.csv` in a text editor to see what the app wrote. Keep that file. Copy the terminal's test results into `evidence/before_tests.txt` with your text editor. Use a text editor rather than a spreadsheet when you need to see the exact characters in a CSV file.

If you see **can't open file**, list the files in the current folder and follow the wrong folder recovery above. If you see **No such file or directory** or **FileNotFoundError**, check the input filename and confirm that `evidence` exists. If an output file is open elsewhere, close it before retrying. If a command is missing, repeat the Python version check and use the command that works. Rerun the unchanged baseline before editing the app.

## 5. Try the small CSV example

CSV means comma separated values. It is a text format with named columns and one record per row. Python's `csv` library handles commas and quotation marks inside cells.

Before changing the app, run:

```text
python3 example_csv.py
```

It should print:

```text
ticket,queue,note
Q2,2,
Q3,2,
Q1,11,
The temporary example output has been removed.
```

Read `example_csv.py` beside `example_queue.csv`. This separate example gives you file handling code to use while you work:

- `Path(__file__).with_name(...)` finds the input beside the script, even if the terminal is elsewhere.
- `with ... open(...)` closes the file when that part finishes, including when an error occurs. `encoding="utf-8"` supports text in many languages. `newline=""` lets the CSV library handle line endings.
- `csv.DictReader` makes each row a dictionary. A column name is its key. `list(...)` collects the rows so they can be sorted.
- `queue_number` converts the queue text to a whole number. `sort(key=queue_number)` compares those numbers. Equal numbers keep their original order, so Q2 stays before Q3.
- `row.get("note", "")` returns an empty string when the `note` key is absent. If the key exists, it returns the value already there.
- `csv.DictWriter` writes named columns. `writeheader()` writes the names and `writerows(...)` writes the records.
- `TemporaryDirectory` creates a separate folder for the example output. The code reads the output before leaving the `with` section. Then Python removes that folder and its contents. Your evidence files use a normal folder so they remain available.

The example uses only Python's standard library, which comes with Python. You do not need to install packages.

## 6. Check the export requirements

Valid input has a header with `record_id`, `position` and `reading`. The `label` column is optional. Identifiers are unique text. Positions are positive whole numbers. Readings are decimal text with an optional sign, up to six digits before the decimal point and up to four after it. Labels may contain spaces, commas or quotation marks. All measurements use the same unit. Handling invalid input and converting units are outside this project.

- Keep every record exactly once.
- Keep each identifier, reading and supplied label exactly as written in the input.
- Sort by position as a whole number, from smallest to largest. Keep input order for equal positions.
- Write `record_id,position,reading,label` in that order. Write positions as whole numbers.
- Write an empty label when its cell is empty or the label column is absent.
- Write a header even when there are no records.

Add your own automated tests. Use the requirements to choose expected results. The supplied tests check basic operation only. You can ask an AI assistant to explain code or suggest changes, but check its suggestions yourself.

## About this data

The eight measurement records were made for this project. They contain no readings from real equipment or people. The queue example was also made for this project and has no real tickets. These files support code checks but cannot show equipment performance or real waiting times.

## Share your work

Keep the licence with your corrected source. Share your tests, actual before and after exports, test results and repair note on a public page or repository. Check that each file opens without signing in. Explain what you changed, one alternative and what your evidence supports. Start with the task and result so a reader can understand the work in two minutes.
