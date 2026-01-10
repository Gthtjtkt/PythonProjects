# main.py

import os
import file_manager as fm
import ui_utils as ui
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional To-Do Manager")
        self.root.geometry("600x600")

        # Assigning variables
        self.current_tasks = []
        self.current_filename = ""
        self.app_dir = fm.get_app_dir()

        # ---------- UI Elements ------------
        self.label_status = tk.Label(root, text = "Active to do list: None", fg = "blue")
        self.label_status.pack(pady = 10)

        # -------- Listbox to show tasks ---------
        # Is rendered above the options menu
        # Displays the tasks in the current list
        self.task_listbox = tk.Listbox(root, width=50, height=20)
        self.task_listbox.pack(pady = 10, padx = 15)

        # -------- Buttons --------------
        tk.Button(root, text="New List", command=self.create_new_list).pack(fill = "x", padx = 50)
        tk.Button(root, text="Load List", command=self.load_list).pack(fill = "x", padx = 50)
        tk.Button(root, text="Add Task", command=self.add_task).pack(fill = "x", padx = 50)
        tk.Button(root, text="Delete Task", command=self.delete_task).pack(fill = "x", padx = 50)
        tk.Button(root, text="Save Active List", command=self.save_list).pack(fill = "x", padx = 50)

        # ------- Menu Bar ----------
        self.setup_menu()

    def setup_menu(self):
        menubar = tk.Menu(self.root)

        # File Menu
        # Appears in the top right corner of the window
        file_menu = tk.Menu(menubar, tearoff = 0)
        file_menu.add_command(label = "New List", command=self.create_new_list)
        file_menu.add_command(label='Save', command=self.save_list)
        file_menu.add_command(label='Load', command=self.load_list)
        file_menu.add_command(label='Delete Task', command=self.delete_task)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.root.quit)
        menubar.add_cascade(label='File', menu=file_menu)

        self.root.config(menu=menubar)

    def create_new_list(self):
        name = simpledialog.askstring("New List", "Please enter the name of the list:")
        if name:
            # force storage into the app's folder
            filename = os.path.join(self.app_dir, f"{name}.txt")
            self.current_filename = filename
            self.current_tasks = []
            self.update_ui(name)
            fm.log_metadata(name, filename)
            messagebox.showinfo("Success", f"List created locally: {name}.txt")

    def add_task(self):
        if not self.current_filename:
            messagebox.showerror("Error", "Create a list first.")
            return
        task = simpledialog.askstring("Add Task", "Please enter the name of the task:")
        if task:
            self.current_tasks.append(task)
            self.task_listbox.insert(tk.END, task)

    def delete_task(self):
        # make sure list isn't active
        if not self.current_filename:
            messagebox.showerror("Error", "No Active List.")
            return

        # make sure task is selected
        selection = self.task_listbox.curselection() # user selects what task to delete with their cursor
        if not selection:
            messagebox.showwarning("No Selection", "Select a task to delete.")
            return

        index = selection[0]
        task = self.current_tasks[index]

        # Confirm the user actually wants to delete the task
        confirm = messagebox.askyesno(
            "Confirm delete",
            f"Delete this task? \n\n{task}"
        )

        if confirm:
            # remove from list
            self.current_tasks.pop(index)

            # Remove from UI
            self.task_listbox.delete(index)

    def save_list(self):
        if self.current_filename:
            fm.write_lines(self.current_filename, self.current_tasks)
            messagebox.showinfo("Success", f"List saved locally: {self.current_filename}")
        else:
            messagebox.showerror("Error", "No active list to save.")

    def load_list(self):

        filepath = filedialog.askopenfilename(
            title="Load To-Do List:",
            initialdir=self.app_dir,
            filetypes=[("Test Files", "*.txt")]
        )

        if not filepath:
            return

        try:
            tasks = fm.read_lines(filepath)

            self.current_filename = filepath
            self.current_tasks = tasks

            self.task_listbox.delete(0, tk.END)
            for task in tasks:
                self.task_listbox.insert(tk.END, task)

            list_name = os.path.basename(filepath)
            self.label_status.config(text=f"Active List: {list_name}")

            messagebox.showinfo("Loaded", f"Loaded List: {list_name}")

        except Exception as e:
            messagebox.showerror("Error", f"Error while loading list: \n{e}")

    def update_ui(self, name):
        self.label_status.config(text=f"Active list: {name}")
        self.task_listbox.delete(0, tk.END)

if __name__ == "__main__":

    # Create instance of the tkinter ui object and name it root
    root = tk.Tk()

    # pass this
    app = TodoApp(root)
    root.mainloop()
