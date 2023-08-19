import pickle
import os
from task import Task
import datetime 

class Tasks:
    # Hard-code the filename of the pickle file from which the program reads/writes the latest task information.
    # Make the file hidden by adding . in front of the file name. Save in home.
    home_directory = os.path.expanduser("~")
    FILENAME = home_directory + '/.todo.pickle'

    def __init__(self):
        # Check if the saved task information exists.
        if os.path.exists(Tasks.FILENAME):
            with open(Tasks.FILENAME, 'rb') as file:
                self.tasks = pickle.load(file)
        # If the file doesn't exist, start fresh with an empty list.
        else:
            self.tasks = []

    def save_tasks(self):
        # Save the tasks into the pickle file.
        with open(Tasks.FILENAME, 'wb') as file:
            pickle.dump(self.tasks, file)
            
    def add(self, name, due_date=None, priority=1):
        if len(self.tasks) > 0:
            last_id = self.tasks[len(self.tasks) - 1].id
        else:
            last_id = 0
        # Create the task with the user arguments.
        task = Task(last_id + 1, name, due_date, priority)
        # Add the task to the task list.
        self.tasks.append(task)
        # Sort the tasks by its due dates and its priority.
        self.tasks.sort(key=lambda x: (x.due_date, x.priority))
        # Save the latest task list into the pickle file.
        self.save_tasks()
        return task.id
    
    # Print the list of all the tasks
    def list_tasks(self):
        print("\nID   Age  Due Date   Priority   Task")
        print("--   ---  --------   --------   ----")
        for task in self.tasks:
            if not task.completed:
                age = (datetime.datetime.now() - task.created).days
                print(f"{task.id}    {age}d   {task.due_date}    {task.priority}        {task.name}")

    # One can query all the tasks that's related to the user provided string.
    def query(self, terms):
        print("\nID   Age  Due Date   Priority   Task")
        print("--   ---  --------   --------   ----")
        for task in self.tasks:
            # Compare after changing everything to lowercase
            if any(term.lower() in task.name.lower() for term in terms) and not task.completed:
                age = (datetime.datetime.now() - task.created).days
                print(f"{task.id}    {age}d   {task.due_date}    {task.priority}        {task.name}")

    def done(self, task_id):
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            task.completed = datetime.datetime.now()
            self.save_tasks()

    def delete(self, task_id):
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task:
            # Use the remove method of the list to remove a task.
            self.tasks.remove(task)
            # Whenever we delete a task, we update the task file as well.
            self.save_tasks()
    
    def report(self):
        print("\nID   Age  Due Date   Priority   Task                Created                       Completed")
        print("--   ---  --------   --------   ----                ---------------------------   -------------------------")
        for task in self.tasks:
            age = (datetime.datetime.now() - task.created).days
            completed = task.completed if task.completed else '-'
            print(f"{task.id}    {age}d   {task.due_date}    {task.priority}        {task.name}    {task.created}    {completed}")
