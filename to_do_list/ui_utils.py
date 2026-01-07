# ui_utils.py
import tkinter as tk
from tkinter import filedialog

def select_directory_via_gui():
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