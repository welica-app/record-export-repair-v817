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
python3 save_test_results.py evidence/before_tests.txt
```

The first command should print `Exported 8 records to evidence/before.csv`. The test command writes its actual results into `evidence/before_tests.txt` as well as showing them in the terminal. The second should name three tests, mark each `ok`, then end with `Ran 3 tests` and `OK`. The elapsed time can differ. This confirms that the unchanged starter runs. It does not establish that the app meets every requirement.

Open `evidence/before.csv` in a text editor to see what the app wrote. Keep that file. Then run `python3 summary_readings.py measurements.csv`. It should show `Records: 8`, `Lowest reading: -2.250` and `Highest reading: 100.010`. Copy these three lines into `evidence/before_summary.txt` with your text editor. Use a text editor rather than a spreadsheet when you need to see the exact characters in a CSV file.

If you see **can't open file**, list the files in the current folder and follow the wrong folder recovery above. If you see **No such file or directory** or **FileNotFoundError**, check the input filename and confirm that `evidence` exists. If an output file is open elsewhere, close it before retrying. If a command is missing, repeat the Python version check and use the command that works. Rerun the unchanged baseline before editing the app. If the evidence saver says a file already exists, use a new filename so you keep the earlier result. After adding tests and again after the repair, run it with new names such as `evidence/original_checks.txt` and `evidence/after_tests.txt`. It finds every `test*.py` file in this folder. A failed test still produces a saved transcript and a nonzero exit code, which tells the terminal the checks failed.

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

## 6. Keep a local record with Git

Git records which files changed. You do not need an account or a remote repository. First run `git --version`. If the command is missing, install Git from [its official downloads page](https://git-scm.com/downloads). On Linux you can also use your system's software manager. Reopen the terminal in the starter folder and check again.

If you downloaded the ZIP, run these commands before editing code:

```text
git init
git config user.name "Learner"
git config user.email "learner@example.invalid"
git add .
git commit -m "Save unchanged starter and baseline"
```

These name and email settings apply only to this folder. You may replace them with the identity you want to show with your work. If Git says **Author identity unknown**, run the two configuration commands again and retry the commit. If Git says **not a git repository**, list the files and return to the starter folder before running `git init`.

After repairing and checking the app, run `git diff` to inspect changes. Then run `git add .`, followed by `git commit -m "Repair export and add regression checks"`. Run `git log -1 --oneline` and copy that commit reference into your repair note. Include the diff of your repair commit, which you can save by running `git show --format=fuller > evidence/repair.diff`. Keep the local `.git` folder with your working copy. You can hand over a ZIP of the final files plus this diff without sharing the hidden folder.

## Requirements and hand-in

Use the requirements on the project page when choosing expected results. The file `summary_readings.py` is also part of the starter. The reviewer already uses it to see the record count and the lowest and highest readings as numbers, rounded to three decimal places. Keep that behaviour while repairing the export. For an empty file it prints `Records: 0` and `No readings.` instead of a numeric range. In its code, `min` chooses the smallest value and `max` chooses the largest. The format `:.3f` displays a number with three decimal places. The command handling and summary display are already set up, so you can focus on the repair.

Add your own automated tests. An AI assistant may explain code or suggest changes. You choose the repair and check its effect on both programs.

## About this data

The eight measurement records were made for this project. They contain no readings from real equipment or people. The queue example was also made for this project and has no real tickets. These files support code checks but cannot show equipment performance or real waiting times.
