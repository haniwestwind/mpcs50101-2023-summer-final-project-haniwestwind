#!//anaconda3/bin/python
# To make this program an executable, add the shebang mark like above.

import argparse
from tasks import Tasks
def main():
    parser = argparse.ArgumentParser(description="Command-line task manager.")

    # Define possible commands for the application
    parser.add_argument("--add", type=str, help="Add a new task")
    parser.add_argument("--due", type=str, default=None, help="Due date for task")
    parser.add_argument("--priority", type=int, choices=[1, 2, 3], default=1, help="Priority of task; default value is 1")
    parser.add_argument("--delete", type=int, help="Delete a task by its unique identifier")
    parser.add_argument("--done", type=int, help="Mark a task as completed by its unique identifier")
    parser.add_argument("--list", action='store_true', help="List not completed tasks")
    parser.add_argument("--report", action='store_true', help="List all tasks, including completed tasks")
    parser.add_argument("--query", type=str, nargs='+', help="Search tasks based on query term(s)")

    args = parser.parse_args()
    
    # Integrate with Tasks class here...
    task_manager = Tasks()

    if args.add:
        task_id = task_manager.add(args.add, args.due, args.priority)
        print(f"Created task {task_id}")

    elif args.delete:
        task_manager.delete(args.delete)
        print(f"Deleted task {args.delete}")

    elif args.done:
        task_manager.done(args.done)
        print(f"Completed task {args.done}")

    elif args.list:
        task_manager.list_tasks()

    elif args.report:
        task_manager.report()

    elif args.query:
        task_manager.query(args.query)

if __name__ == "__main__":
    main()