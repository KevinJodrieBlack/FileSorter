import os
import shutil
import windowdisplay

# Dictionary to map folder names to their corresponding file extensions
folders = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Videos": [".mp4", ".avi", ".mov", ".wmv", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".c", ".cpp", ".html", ".js", ".css"],
    "Models": [".fbx"],
    "Others": []  # Files with extensions not listed above will be placed in this folder
}

# Function to clean the desktop by sorting files into the appropriate folders
def clean_desktop(source_folder, dest_folder):
    # Ensure that each folder (Documents, Images, etc.) exists in the destination directory
    for folder in folders:
        folder_path = os.path.join(dest_folder, folder)
        if not os.path.exists(folder_path):
            print("Creating " + folder + " directory")
            os.makedirs(folder_path)  # Create the folder if it doesn't exist

    # Iterate through the files in the source folder
    for item in os.listdir(source_folder):
        item_path = os.path.join(source_folder, item)

        # Skip directories, only process files
        if os.path.isdir(item_path):
            continue

        # Extract the file extension to determine which folder it belongs to
        file_extension = os.path.splitext(item)[1]

        item_moved = False  # Flag to track if the file has been moved

        # Check each folder's extensions to find a match
        for folder, extensions in folders.items():
            if file_extension.lower() in extensions:
                # Check if the file already exists in the destination folder (avoid overwriting)
                if os.path.exists(os.path.join(dest_folder, folder, item)):
                    item_moved = True  # If already exists, skip moving
                    break

                # Move the file to the corresponding folder in the destination directory
                shutil.move(item_path, os.path.join(dest_folder, folder, item))
                item_moved = True
                break

        # If the file type doesn't match any listed extensions, move it to "Others" folder
        if not item_moved:
            if os.path.exists(os.path.join(dest_folder, "Others", item)):
                continue  # Skip if the file is already in the "Others" folder

            print("File type not recognized. Moving to others folder")
            shutil.move(item_path, os.path.join(dest_folder, "Others", item))


# Main execution: calls the GUI function from window display to start the process
if __name__ == '__main__':
    windowdisplay.clean_desktop_gui()
