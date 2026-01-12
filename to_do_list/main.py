# main.py

import os
import file_manager as fm
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

class TodoApp:

    # __init__ is a special method called a 'Constructor'.
    # It runs AUTOMATICALLY the moment you create the app (app = TodoApp(root)).
    # 'self' represents the specific instance of the app you are currently building.
    # 'root' is the main window passed in from outside.
    def __init__(self, root):

        # We store the window (root) inside 'self.root' so other functions can access it later.
        self.root = root

        # Standard window setup: Title bar text and dimensions in pixels (Width x Height)
        self.root.title("Professional To-Do Manager")
        self.root.geometry("600x600")

        # ------------------------- Assigning variables ------------------------
        # We use 'self.' so these variables stay alive as long as the window is open.
        # If we just used 'current_tasks' (without self), it would vanish after __init__ finishes.
        self.current_tasks = []
        self.current_filename = ""
        self.app_dir = fm.get_app_dir()

        # ---------------------------- UI Elements ---------------------------
        # tk.Label: A widget used to display text.
        # root: Tells the label to live inside the main window.
        # text: The initial words shown.
        # fg: 'Foreground' color (the color of the text).
        self.label_status = tk.Label(root, text = "Active to do list: None", fg = "blue")

        # .pack(): This is a 'Geometry Manager'. It actually places the widget on the window.
        # pady=10: Adds 10 pixels of 'Padding' (empty space) above and below the label.
        self.label_status.pack(pady = 10)

        # -------------------- Listbox to show tasks --------------------
        # Is rendered above the options menu
        # Displays the tasks in the current list

        # width/height: Measured in characters/lines, not pixels.
        # width=50: About 50 characters wide. height=20: Shows 20 lines at a time.
        self.task_listbox = tk.Listbox(root, width=50, height=20)

        # padx=15: Adds space on the left and right sides so it's not touching the window edges.
        self.task_listbox.pack(pady = 10, padx = 15)

        # ----------------------------- Buttons ----------------------------
        # tk.Button syntax:
        # root: Put it in the main window.
        # text: What is written on the button.
        # command: THE MOST IMPORTANT PART. This tells Python which function to run
        #          when the user clicks the button. Notice there are NO () after the function name.
        #          We are passing the function like a recipe, not cooking it yet!

        # .pack(fill="x"): Tells the button to stretch horizontally to fill the window.
        # padx=50: Adds space on the sides so the button isn't stretched to the very edge.
        tk.Button(root, text="New List",         command=self.create_new_list).pack(fill = "x", padx = 50)
        tk.Button(root, text="Load List",        command=self.load_list).pack(fill = "x", padx = 50)
        tk.Button(root, text="Add Task",         command=self.add_task).pack(fill = "x", padx = 50)
        tk.Button(root, text="Delete Task",      command=self.delete_task).pack(fill = "x", padx = 50)
        tk.Button(root, text="Save Active List", command=self.save_list).pack(fill = "x", padx = 50)

        # --------------------------- Menu Bar -----------------------
        # Calls another function to build the top file menu.
        self.setup_menu()

    def setup_menu(self):
        """
        Creates the top horizontal menu bar (File, Edit, etc.).
        """
        # 1. Create the main bar that sits at the very top
        menubar = tk.Menu(self.root)

        # 2. Create a 'dropdown' menu.
        # 'tearoff=0' prevents the user from popping the menu out into a separate window.
        file_menu = tk.Menu(menubar, tearoff = 0)

        # 3. Add individual clickable options to the dropdown
        file_menu.add_command(label="New List",    command=self.create_new_list)
        file_menu.add_command(label='Save',        command=self.save_list)
        file_menu.add_command(label='Load',        command=self.load_list)
        file_menu.add_command(label='Delete Task', command=self.delete_task)

        # 4. A separator is just a horizontal line to organize the menu visually
        file_menu.add_separator()
        file_menu.add_command(label='Exit',        command=self.root.quit)

        # 5. 'Cascade' creates the 'File' button that you click to see the menu
        menubar.add_cascade(label='File', menu=file_menu)

        # 6. Tell the main window to actually display this menubar
        self.root.config(menu=menubar)

    def create_new_list(self):
        """
        Handles naming a new file and clearing the current workspace.
        """
        # simpledialog.askstring pops up a tiny window with a text box
        name = simpledialog.askstring("New List", "Please enter the name of the list:")

        if name: # If the user didn't hit 'Cancel'
            # os.path.join handles the backslashes (/) correctly for Windows or Mac
            filename = os.path.join(self.app_dir, f"{name}.txt")

            # Update the App's memory
            self.current_filename = filename
            self.current_tasks = []

            # Clear the screen and update the blue label
            self.update_ui(name)

            # Write this new path into your paths.txt log
            fm.log_metadata(name, filename)
            messagebox.showinfo("Success", f"List created locally: {name}.txt")

    def add_task(self):
        """
        Adds a new item to the internal list AND the visual listbox.
        """
        # Error Handling: Check if a file is actually open before adding tasks
        if not self.current_filename:
            messagebox.showerror("Error", "Create a list first.")
            return # Stop the function here

        task = simpledialog.askstring("Add Task", "Please enter the name of the task:")

        if task:
            # Add to the Python list (data memory)
            self.current_tasks.append(task)
            # Add to the Tkinter Listbox (visual display)
            # tk.END tells it to put the new task at the very bottom
            self.task_listbox.insert(tk.END, task)

    def delete_task(self):
        """
        Identifies the highlighted task and removes it from memory and UI.
        """
        if not self.current_filename:
            messagebox.showerror("Error", "No Active List.")
            return

        # make sure task is selected
        # .curselection() returns a TUPLE of the index numbers of highlighted items.
        # Example: if you click the first item, selection is (0,)
        selection = self.task_listbox.curselection() # user selects what task to delete with their cursor

        if not selection:
            messagebox.showwarning("No Selection", "Select a task to delete.")
            return

        # Extract the index number (0, 1, 2...) from the tuple
        index = selection[0]

        # Look up the text of that task in our memory list
        task = self.current_tasks[index]

        # askyesno returns True (Yes) or False (No)
        confirm = messagebox.askyesno(
            "Confirm delete",
            f"Delete this task? \n\n{task}"
        )

        if confirm:
            # .pop() removes the item from the Python list
            self.current_tasks.pop(index)

            # .delete() removes the item from the Tkinter Listbox visually
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


# --- THE BOOTSTRAPPER ---
# This line checks: "Is this file being run directly?" (instead of being imported).
# It's the starting gun for your program.
if __name__ == "__main__":
    # 1. Initialize the Tkinter engine. 'root' is the actual OS-level window.
    root = tk.Tk()

    # 2. Create the App. We pass 'root' into 'TodoApp' so the class knows where to draw.
    #    This triggers the __init__ method above.
    app = TodoApp(root)

    # 3. root.mainloop() is an INFINITE LOOP.
    #    It keeps the window open and waits for you to click something.
    #    Without this, the window would pop up and close in 0.01 seconds.
    root.mainloop()
