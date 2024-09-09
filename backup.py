"""
backup.py is a file to backup the current flask app

Steps to backup the website
---
1. Run the backup.py
2. It will automatically create the zip file which includes all the backup files


"""

from datetime import date
from shutil import ignore_patterns, copytree, make_archive, rmtree
import os

# Configuration
NAME = 'Flask_structure'
BASE_DIR  = os.path.dirname(__file__)

# Files and folders to ignore
""" It will not backup these folders """
IGNORE_FOLDERS = ignore_patterns('env', '__pycache__', '*.zip', ".git")

# Backup folder name 
FOLDER_NAME = f'Backup_{NAME}_{date.today()}'
backup_folder = os.path.join(BASE_DIR, FOLDER_NAME)
print("Created backup directory name")

# Create a temporary backup folder
copytree(BASE_DIR, backup_folder, ignore=IGNORE_FOLDERS)
print("Created temporary directory")

# Create zip file
make_archive(FOLDER_NAME, 'zip', FOLDER_NAME)
print("Created zip file")
print(f"Successfully! created backup of {NAME}")

# Remove temporary folder
rmtree(os.path.join(BASE_DIR, FOLDER_NAME))