# to_do_list.py

import os
import tkinter as tk
from tkinter import filedialog



FILENAME = "tasks.txt"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("Tasks saved.")

def view_tasks(tasks):
    for task in tasks:
        print(task)

def add_task(tasks):
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"Task added: {task}")

def main():

    tasks = load_tasks()

    while True:
        print("\nMenu")
        print("1. View tasks")
        print("2. Add task")
        print("3. Save tasks")
        print("4. Save and exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Try again.")

main()