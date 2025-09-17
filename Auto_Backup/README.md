# 🗂️ Auto Backup

A simple Python script to automatically create ZIP backups of a specified folder. The script generates timestamped backup files, stores them in a chosen destination, and prints the size of the backup in MB.  

---

## 🚀 Features

- Creates ZIP backups of any folder.
- Automatically generates a timestamped backup filename.
- Creates the destination folder if it does not exist.
- Displays the size of the backup file.
- Easy-to-use interactive command line interface.

__________________________________________________________________________________________________________________________________________________________________________________
## 🛠️ Requirements
•Python 3.8+
_____________________________________________________________________________________________________________________________________________________________________________________
## ▶️ Usage
Run the script:
  python app.py

Follow the prompts:
  1. Enter the origin folder you want to backup.
  2. Enter the destination folder to save the backup (leave empty to use ./backups).
  3. The script will create a timestamped ZIP backup and display its size.
_____________________________________________________________________________________________________________________________________________________________________________________
## 📈 Example output:

=== AUTO BACKUP ===
Insert the origin folder you want to backup: ./my_project
Insert the destination folder where you want to save the backup (leave it empty to use './backups' as default): 
Creating backup in './backups/backup_20250917_143022.zip'...
Added: my_project/file1.txt
Added: my_project/file2.py
Backup Completed: ./backups/backup_20250917_143022.zip

Backup size: 1.45 MB
Backup completed successfully!
_____________________________________________________________________________________________________________________________________________________________________________________
## 🧩 Functions Overview

•create_backup_name(): Generates a timestamped backup filename.
•create_backup(origin_folder, destination_folder): Creates the ZIP backup of the given folder.
•main(): Interactive script interface.
_____________________________________________________________________________________________________________________________________________________________________________________
## 📜 License

This project is licensed under the MIT License.
