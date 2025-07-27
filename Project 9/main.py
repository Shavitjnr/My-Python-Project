import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

TASKS_FILE = "tasks.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = self.load_tasks()
        self.create_widgets()
        self.refresh_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.listbox = tk.Listbox(self.frame, width=40, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=5)

        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = tk.Button(self.button_frame, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self.button_frame, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def refresh_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[x]" if task["completed"] else "[ ]"
            self.listbox.insert(tk.END, f"{status} {task['title']}")

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter task:")
        if title:
            self.tasks.append({"title": title, "completed": False})
            self.refresh_tasks()

    def complete_task(self):
        idx = self.listbox.curselection()
        if not idx:
            messagebox.showinfo("Complete Task", "Select a task to complete.")
            return
        i = idx[0]
        self.tasks[i]["completed"] = True
        self.refresh_tasks()

    def delete_task(self):
        idx = self.listbox.curselection()
        if not idx:
            messagebox.showinfo("Delete Task", "Select a task to delete.")
            return
        i = idx[0]
        del self.tasks[i]
        self.refresh_tasks()

    def on_close(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
