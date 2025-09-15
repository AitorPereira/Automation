# We want to move files from one folder to another automatically using the os, shutil, and datetime libraries.
# First, we create a new folder if it does not already exist.
# Second, we define the source folder (the one containing the files we want to copy) and store its path in a variable.
# Then, we read the files from the source path and copy them into the destination path (stored in our variable).
# Finally, by using the shutil library, we can move files from one folder to another.

import os
import shutil
from datetime import datetime

#Format strftime (year/month/day)
date = datetime.now().strftime("%Y-%m-%d")

new_folder = f"{date}_Files"

if not os.path.exists(new_folder):
    os.makedirs(new_folder)
    print (f"Folder '{new_folder}' has been created")

main_folder = "/Users/aitor/Documents/Python/Automation_Python/Files"

cont = 0

for file_name in os.listdir(main_folder):
    origin = os.path.join(main_folder, file_name)
    destination = os.path.join(new_folder, file_name)
    shutil.move(origin, destination)
    cont = cont + 1

print (f"{cont} files has been moved into the folder {new_folder}")


#If we want to move only ONE type of file, we can use the following code:
## for file_name in os.listdir(main_folder):
##     if file_name.endswith(".txt"):
##         origin = os.path.join(main_folder, file_name)
##         destination = os.path.join(new_folder, file_name)
##         shutil.move(origin, destination)
##         cont = cont + 1