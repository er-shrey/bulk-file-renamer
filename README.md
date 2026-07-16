# Bulk File Renamer

A small Python script that renames every file in a folder to a sequential numeric name (`.jpg`), useful for quickly normalizing a folder of images/wallpapers.

## Tech Stack

- Python (script uses Python 2-style `print` syntax — see note below)

## Prerequisites

- Python 2.7, or Python 3 after updating the `print` statement (see Notes)

## Usage

1. Open `renammer.py` and set `path` to the folder you want to rename files in:

   ```python
   path = '/path/to/your/folder'
   ```

2. Run the script:

   ```bash
   python renammer.py
   ```

Each file in `path` is renamed to `<index + 128>.jpg` (the offset of 128 and the `.jpg` extension are hardcoded).

## Notes

- The script currently hardcodes a Windows-style path (`D:\books\Wallpapers`) and uses the Python 2 `print index, file` statement inside the `except` block — update both before running on Python 3 or a non-Windows machine.
- The extension is hardcoded to `.jpg`; adjust the script if renaming other file types.
