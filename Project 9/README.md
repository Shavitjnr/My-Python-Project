# To-Do List GUI Application

A simple and user-friendly To-Do List application with a graphical interface, built using Python and Tkinter. This project allows you to efficiently manage your daily tasks: add, complete, and delete items, with all tasks saved automatically to a local JSON file for persistence.

---

## 📋 Features
- **Intuitive GUI:** Built with Tkinter for a clean and responsive experience.
- **Add Tasks:** Quickly add new tasks via a dialog box.
- **Complete Tasks:** Mark tasks as completed with a single click.
- **Delete Tasks:** Remove tasks you no longer need.
- **Persistent Storage:** All tasks are saved to `tasks.json` in the project directory.
- **No External Dependencies:** Uses only Python's standard library.

---

## 🛠️ Requirements
- **Python:** 3.6 or higher (tested with 3.12)
- **Tkinter:** Standard with most Python installations. If missing, install with:
  ```bash
  sudo apt-get install python3-tk
  # or for Python 3.12+
  sudo apt-get install python3.12-tk
  ```

---

## 🚀 Installation & Usage
1. **Clone or Download this Project Folder**
2. **(Optional) Review `requirements.txt`**
   - No external packages are required.
3. **Run the Application:**
   ```bash
   python3 main.py
   ```
4. **Using the App:**
   - Add a task: Click "Add Task" and enter your task.
   - Complete a task: Select a task and click "Complete Task".
   - Delete a task: Select a task and click "Delete Task".
   - Tasks are saved automatically when you close the app or click "Save Tasks".

---

## 📁 File Structure
```
Project 9/
├── main.py           # Main application code (Tkinter GUI)
├── requirements.txt  # Notes on dependencies (none required)
├── tasks.json        # (Auto-created) Stores your tasks
└── README.md         # Project documentation
```

---

## 📝 About This Project
This To-Do List app was created as part of a Python project collection to demonstrate practical GUI development and file persistence using only the standard library. It is ideal for beginners learning Python GUIs or anyone needing a lightweight, local task manager.

Feel free to use, modify, or extend this project for your own needs!
