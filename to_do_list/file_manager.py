# file_manager.py
"""
This module handles all low-level file I/O operations for the To-Do application.
It provides a clean abstraction layer between the logic of the application
and the physical storage on the disk.
"""

import os

def get_app_dir():
    """
        Finds the folder where the actual Python script is saved.

        Returns:
            str: The full path to the project folder (e.g., 'E:/Python Projects/To_Do_App')
        """
    # __file__ is a special Python variable that contains the path to the current script.
    # abspath makes it a full path, and dirname removes the filename.
    return os.path.dirname(os.path.abspath(__file__))

def read_lines(filepath):
    """
    Opens a file, reads every line, and cleans up extra spaces/newlines.

    Args:
        filepath (str): The path to the .txt file.

    Returns:
        list: A list of clean strings. Returns empty list if file is missing or broken.
    """
    if os.path.exists(filepath):
        try:
            # encoding="utf-8" ensures special characters (like emojis) don't crash the app.
            with open(filepath, "r", encoding="utf-8") as f:
                # readlines() gets everything; .strip() cleans the 'invisible' \n characters.
                return [line.strip() for line in f.readlines()]
        except (IOError, OSError) as e:
            print(f"Error: Could not read file at {filepath}. \n{e}")
            return []
    return []

def write_lines(filepath, lines):
    """
    Takes a Python list and overwrites a .txt file with those items.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            for line in lines:
                # We add the \n (newline) back in so each task is on its own row.
                f.write(f"{line}\n")
    except (IOError, OSError) as e:
        print(f"Error: Failed to save to {filepath}. \n{e}")

def log_metadata(list_name, filename):
    """
    Appends a new list entry to the 'paths.txt' registry.
    This helps the app remember where all your different lists are stored.
    """
    # Join the app directory with the filename 'paths.txt'
    path_log = os.path.join(get_app_dir(), "paths.txt")

    with open(path_log, "a", encoding="utf-8") as f:
        f.write(f"{list_name}|{filename}\n")

def clear_file_on_disk(filepath):
    """
    Wipes all content from a specific file on the disk.
    """
    if os.path.exists(filepath):
        # Opening a file in 'w' mode and immediately closing it effectively erases it.
        with open(filepath, "w", encoding="utf-8") as f:
            pass