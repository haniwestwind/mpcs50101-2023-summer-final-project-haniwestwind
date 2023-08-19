import datetime


class Task:
    '''
    Task class defines the abstract concept of a task.
    In our application, a task contains information such as the description, when the task was created, the due date, priority, etc.
    '''
    # Make the ID variable as a class variable to assign a unique id when a new task is created. 
    ID = 1

    def __init__(self, id, name, due_date=None, priority=1):
        # Store the date and time when the task was created.
        self.created = datetime.datetime.now()
        # Keep track of whether the task is completed or not. None is default for when it's incomplete.
        self.completed = None
        # Store the name of the task.
        self.name = name
        # Assign a unique id to each task.
        self.id = id
        # Set the priority of the task. 
        self.priority = priority
        # Some tasks do not have a due date. That case, just mark it with - character.
        self.due_date = due_date if due_date else '-'
