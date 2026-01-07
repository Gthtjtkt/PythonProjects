# file_manager.py
"""
This module handles all low-level file I/O operations for the To-Do application.
It provides a clean abstraction layer between the logic of the application
and the physical storage on the disk.
"""

import os

def get_app_dir():
    # returns the absolute path to the directory where the script is running
    return os.path.dirname(os.path.abspath(__file__))

def read_lines(filepath):
    """
    Reads a text file and returns a list of stripped lines.

    Args:
        filepath (str): The absolute path to the file to be read.

    Returns:
        list: A list of strings containing the file content.
              Returns an empty list if the file does not exist.
    """
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                # .strip() removes newline characters and leading/trailing whitespace
                return [line.strip() for line in f.readlines()]
        except (IOError, OSError) as e:
            print(f"Error: Could not read file at {filepath}. {e}")
            return []
    return []

def write_lines(filepath, lines):
    with open(filepath, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}\n")

def log_metadata(list_name, filename):
    """Logs the mapping in a local paths.txt"""

    path_log = os.path.join(get_app_dir(), "paths.txt")

    with open(path_log, "a", encoding="utf-8") as f:
        f.write(f"{list_name}|{filename}\n")
