"""
File Organizer
--------------
Scans a target folder and sorts files into subfolders based on
their file extension (e.g. Images/, Documents/, Videos/).

Usage: python 4_file_organizer.py /path/to/folder
"""

import os
import shutil
import sys

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".json"],
}


def get_category(extension):
    for category, extensions in CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Other"


def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    moved_count = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue  # skip subfolders

        _, extension = os.path.splitext(filename)
        if not extension:
            continue  # skip files with no extension

        category = get_category(extension)
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

        destination = os.path.join(category_folder, filename)
        # Avoid overwriting existing files with the same name
        if os.path.exists(destination):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(destination):
                destination = os.path.join(category_folder, f"{base}_{counter}{ext}")
                counter += 1

        shutil.move(file_path, destination)
        print(f"Moved: {filename} -> {category}/")
        moved_count += 1

    print(f"\nDone. {moved_count} file(s) organized.")


def main():
    if len(sys.argv) > 1:
        target_folder = sys.argv[1]
    else:
        target_folder = input("Enter the folder path to organize: ").strip()

    organize_folder(target_folder)


if __name__ == "__main__":
    main()
