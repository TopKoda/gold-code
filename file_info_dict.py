"""
Level Up In Tech - week 13 project

Dictionary example - retrieve file information from a specified directory.
Use current directory if no path parameter supplied.

Johnny Mac - 07 Apr 2023
"""
import os

def gather_file_info(path=None):
    if not path:
        path = os.getcwd()

    file_info_list = []

    def collect_file_info(directory):
        for entry in os.scandir(directory):
            if entry.is_file():
                file_info = {
                    "path": entry.path,
                    "name": entry.name,
                    "size": f"{entry.stat().st_size} bytes"
                }
                file_info_list.append(file_info)
            elif entry.is_dir():
                collect_file_info(entry.path)

    collect_file_info(path)
    return file_info_list

def display_file_info(file_info_list):
    for file_info in file_info_list:
        print(f"File path: {file_info['path']}\nFile name: {file_info['name']}\nFile size: {file_info['size']}\n")

if __name__ == "__main__":
    user_path = input("Enter the directory path you want scanned (or leave empty for the current working directory): ").strip() or None
    gathered_file_info = gather_file_info(user_path)
    display_file_info(gathered_file_info)
