import os
import datetime
import zipfile

#To create a backup name we'll use the current date and time
def create_backup_name():
    date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"backup_{date}.zip"

#If the origin path do not exist print an error but if the destination folder do not exist, create it
def create_backup(origin_folder, destination_folder):
    if not os.path.exists(origin_folder):
        print (f"Error: The origin folder {origin_folder} do not exist.")
        return None

    if not os.path.exists(destination_folder):
        print (f"Creating destination folder: '{destination_folder}'...")
        os.makedirs(destination_folder)

    #Creating backup file name
    backup_name = create_backup_name()
    path_backup = os.path.join(destination_folder, backup_name)

    #Creating ZIP file
    print (f"Creating backup in '{path_backup}'...")

    with zipfile.ZipFile(path_backup, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for actual_folder, subfolders, files in os.walk(origin_folder):
            for file in files:
                file_path = os.path.join(actual_folder, file)
                #Save route in its respective ZIP
                relative_path = os.path.relpath(file_path, os.path.dirname(origin_folder))
                zip_file.write(file_path, relative_path)
                print (f"Added: {relative_path}")
    
    print (f"Backup Completed: {path_backup}")
    return path_backup


def main():
    print ("=== AUTO BACKUP ===")
    
    origin_folder = input("Insert the origin folder you want to backup: ")
    destination_folder = input("Insert the destination folder where you want to save the backup (leave it empty to use './backups' as default): ")

    if not destination_folder:
        destination_folder = "./backups"
    
    #Creating backup
    path_backup = create_backup(origin_folder, destination_folder)

    #If the path of the backup exists then we will obtain the size of the backup by bytes and convert it to MB using the following code:
    if path_backup:
        print (f"\nBackup size: {os.path.getsize(path_backup) / (1024*1024):.2f} MB")
        print ("\nBackup completed succesfully!")

if __name__ == "__main__":
    main()

    








