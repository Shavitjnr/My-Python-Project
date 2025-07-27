import os
import shutil


def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1][1:].lower() or 'no_extension'
            dest_dir = os.path.join(folder_path, ext)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_dir, filename))
    print(f"Files in '{folder_path}' have been organized by extension.")

def main():
    print("File Organizer - Automatically sort files by type/extension")
    folder = input("Enter the path to the folder you want to organize: ").strip()
    organize_folder(folder)

if __name__ == "__main__":
    main()
