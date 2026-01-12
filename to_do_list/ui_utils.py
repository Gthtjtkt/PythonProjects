# ui_utils.py
"""
This module contains 'Utility' functions for the User Interface.
These are generic tools that help the main application interact
with the user via pop-up windows or the console.
"""
import tkinter as tk
from tkinter import filedialog

def select_directory_via_gui():
    """
    Opens a standard Windows/Mac/Linux folder selection dialog.
    This allows the user to pick a folder with their mouse instead
    of typing a path like 'C:/Users/Documents'.
    """
    # 1. We temporarily start the Tkinter engine
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    root.destroy()
    return path

def get_valid_input(prompt):
    while True:
        val = input(prompt).strip()
        if val: return val
        print("Input cannot be empty.")