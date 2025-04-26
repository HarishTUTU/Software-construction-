import datetime
import time

# Task class to store task details
class Task:
    def __init__(self, task_name, reminder_time=None):
        self.task_name = task_name
        self.reminder_time = reminder_time

    def __str__(self):
        return f"Task: {self.task_name}, Reminder: {self.reminder_time}"

# Function to add a task
def add_task(tasks):
    task_name = input("Enter task: ")
    reminder_input = input("Enter reminder time (HH:MM, or leave empty for no reminder): ")
    
    if reminder_input:
        try:
            reminder_time = datetime.datetime.strptime(reminder_input, "%H:%M").time()
        except ValueError:
            print("Invalid time format. Please use HH:MM.")
            return
    else:
        reminder_time = None

    task = Task(task_name, reminder_time)
    tasks.append(task)
    print(f"Task '{task_name}' added.")

# Function to show all tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks):
            print(f"{idx + 1}. {task}")

# Function to check and show reminders
def check_reminders(tasks):
    current_time = datetime.datetime.now().time()
    for task in tasks:
        if task.reminder_time and task.reminder_time <= current_time:
            print(f"Reminder: It's time for '{task.task_name}'!")

# Main loop for the To-Do List app
def main():
    tasks = []

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Check Reminders")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            check_reminders(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        
        time.sleep(60)  # Wait a minute before checking reminders again

if __name__ == "__main__":
    main()
