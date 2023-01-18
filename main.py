import tkinter as tk

class TodoApp:
    def __init__(self):
        self.tasks = []

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Todo List")

        # Create a Label and Entry widget to add tasks
        self.task_label = tk.Label(self.root, text="Task:")
        self.task_label.grid(row=0, column=0)
        self.task_entry = tk.Entry(self.root)
        self.task_entry.grid(row=0, column=1)

        # Create a button to add tasks
        self.add_button = tk.Button(self.root, text="Add", command=self.add_task)
        self.add_button.grid(row=0, column=2)

        # Create a Listbox to display tasks
        self.tasks_list = tk.Listbox(self.root)
        self.tasks_list.grid(row=1, column=0, columnspan=3)

        # Create a button to delete tasks
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, columnspan=3)

        # Start the main loop
        self.root.mainloop()

    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append(task)
        self.tasks_list.insert(tk.END, task)

    def delete_task(self):
        selected_tasks = self.tasks_list.curselection()
        for task in selected_tasks:
            self.tasks.pop(task)
            self.tasks_list.delete(task)

if __name__ == "__main__":
    todo_app = TodoApp()