"""
Created on Sunday Feb 25 13:22:21 2023

@author: Preetham Nagaraju
"""
from pathlib import Path
import csv, os, shutil

directory_folder = input("Enter the folder path to delete the file - ")

# Delete the list of file extensions mentioned in the csv file
def file_delete():
    try:
        with open(r".\file_extension_to_delete.csv") as data_file:
            data = csv.reader(data_file)
            absolute_path = Path(directory_folder)
            for row in data:
                file = list(absolute_path.rglob(row[0]))
                count = 0
                for item in file:
                    if os.path.exists(item):
                        os.remove(item)
                        count += 1
                print("************************")
                print(f'File extension {row[0]}\nDelete count = {count}')
    except:
        print("Deletion is not successful")


# Delete the list of folders mentioned in the csv file
def folder_delete():
    try:
        with open(r".\folder_extension_to_delete.csv") as data_file1:
            data = csv.reader(data_file1)
            absolute_path = Path(directory_folder)
            for val in data:
                path = list(absolute_path.rglob(val[0]))
                count = 0
                for item in path:
                    if os.path.exists(item):
                        shutil.rmtree(item)
                        count += 1
                print("************************")
                print(f'Folder name - {val[0]}\nDelete count = {count}')
    except:
        print("Deletion is not successful")

folder_delete()
file_delete()
