import os
import shutil

folder_path = "test_files"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        extension = file.split(".")[-1].lower()

        destination_folder = os.path.join(folder_path, extension)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        shutil.move(file_path, os.path.join(destination_folder, file))

print("Files organized successfully!")