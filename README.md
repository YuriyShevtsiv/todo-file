📝 To-Do List (Console Application in Python)
Overview

This project is a simple console-based To-Do List application written in Python.
It allows the user to manage daily tasks by viewing, adding, and clearing tasks stored in a text file.

The project demonstrates:

File handling

User input

Menu-driven programs

Basic error handling

How the Program Works

The application uses a text file called spravy.txt to store tasks.
Each task is saved on a separate line.

When the program starts, a menu is displayed where the user can choose an action.

Menu Options

After launching the program, you will see the following menu:

1 - Показати всі справи (Show all tasks)
2 - Додати нову справу (Add a new task)
3 - Очистити всі справи (Clear all tasks)
4 - Вийти з програми (Exit)

1️⃣ Show all tasks

Reads all tasks from spravy.txt

Displays them as a numbered list

Shows a message if the file does not exist or is empty

2️⃣ Add a new task

Prompts the user to enter a new task

Saves the task to spravy.txt

Tasks are appended, not overwritten

3️⃣ Clear all tasks

Asks for confirmation before deleting

Clears the contents of spravy.txt

Prevents accidental deletion

4️⃣ Exit

Stops the program safely

How to Run the Program

Make sure you have Python 3.x installed

Save the code in a file (for example: todo_list.py)

Run the program from the terminal:

python todo_list.py

File Structure
project-folder/
│
├── todo_list.py
├── spravy.txt
└── README.md


spravy.txt will be created automatically if it does not exist.

Requirements

Python 3.x

No external libraries required (os is built-in)

Notes

Tasks are stored in UTF-8 encoding (supports Ukrainian and other languages)

Clearing tasks cannot be undone

This is a learning project and can be expanded with:

Task deletion by number

Task completion status

Saving dates or priorities

Author

Created as a learning project to practice Python file handling and menu-based programs. ✅