# 📂 Auto File Mover

A simple Python script to automatically move files from a source folder into a newly created, timestamped folder. This is useful for organizing files by date, cleaning up directories, or automating file management tasks.

## 🚀 Features

- Moves all files from a source folder into a new folder named with today’s date.
- Automatically creates the destination folder if it doesn’t exist.
- Prints how many files were moved and where they were stored.
- Supports filtering by file type (e.g., move only .txt files).
- Lightweight and easy to run with Python.
__________________________________________________________________________________________________________________________________________________________________________________
### 🛠️ Requirements

Python 3.8+
__________________________________________________________________________________________________________________________________________________________________________________
### ▶️ Usage

Run the script:

    python app.py

Steps performed by the script:

1. Creates a new folder named with today’s date (e.g., 2025-09-17_Files).

2. Reads all files from your source folder.

3. Moves the files into the newly created folder.

4. Displays how many files were successfully moved.

👉 To move only a specific file type (e.g., .txt), you can uncomment the provided filter logic in the script.
__________________________________________________________________________________________________________________________________________________________________________________
### 📈 Example output
    Folder '2025-09-17_Files' has been created
    5 files have been moved into the folder 2025-09-17_Files
__________________________________________________________________________________________________________________________________________________________________________________
### 🧩 Functions Overview

This script doesn’t use custom functions, but the logic is divided into these steps:

•datetime.now().strftime("%Y-%m-%d") → Generates today’s date for the new folder name.

•os.makedirs() → Creates the folder if it doesn’t already exist.

•os.listdir() → Reads files from the source folder.

•shutil.move() → Moves each file into the new folder.

### 📜 License

This project is licensed under the MIT License.
