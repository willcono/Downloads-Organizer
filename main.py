import os
import shutil

# Function that goes through each file in downloads and organizes them into folders named after file types
def organize_files(downloads_path):
    for file in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, file)

        if os.path.isfile(file_path):
            file_type = file.split('.')[-1].lower()
            destination_folder = os.path.join(downloads_path, file_type)

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            destination_path = os.path.join(destination_folder, file)

            # Check if the file is already in the correct folder
            if file_path != destination_path:
                shutil.move(file_path, destination_path)
                print(f"Moved {file} to {file_type} folder.")



downloads_path = r'path/to/downloads/folder'


organize_files(downloads_path)