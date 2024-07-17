
from tkinter import *
import json

class ToDoList:
    def __init__(self, root):  
        self.tasks = []
        self.root = root
        self.root.configure(bg="#FFD7BE")  
        
        self.listbox = Listbox(self.root, bg="white")  
        self.entry = Entry(self.root, bg="white")  
        self.addButton = Button(self.root, text="Add Task", command=self.add_task, bg="white")
        self.delButton = Button(self.root, text="Delete Task", command=self.delete_task, bg="white")
        self.updateButton = Button(self.root, text="Update Task", command=self.update_task, bg="white")
        self.saveButton = Button(self.root, text="Save Tasks", command=self.save_tasks, bg="white")
        self.loadButton = Button(self.root, text="Load Tasks", command=self.load_tasks, bg="white")

        # GUI Layout
        self.entry.pack(pady=10)
        self.addButton.pack(pady=5)
        self.listbox.pack(pady=10, fill=BOTH, expand=True)
        self.updateButton.pack(pady=5)
        self.delButton.pack(pady=5)
        self.saveButton.pack(pady=5)
        self.loadButton.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task!= "":
            self.listbox.insert(END, task)
            self.entry.delete(0, END)

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.listbox.delete(task_index)
        except IndexError:
            print("No task selected to delete")

    def update_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            new_task = self.entry.get()
            if new_task!= "":
                self.listbox.delete(task_index)
                self.listbox.insert(task_index, new_task)
                self.entry.delete(0, END)
        except IndexError:
            print("No task selected to update")

    def save_tasks(self):
        tasks = self.listbox.get(0, END)
        with open("tasks.json", "w") as file:
            json.dump(list(tasks), file)  

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                self.listbox.delete(0, END)
                for task in tasks:
                    self.listbox.insert(END, task)
        except FileNotFoundError:
            print("No saved tasks found")

root = Tk()
root.title("Python To-Do List")
root.geometry("300x400")  
to_do_list = ToDoList(root)
root.mainloop()