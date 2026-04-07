# Day 10 — To-Do CLI App

tasks = []

# Function to add task
def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

# Function to show tasks
def show_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

# Function to delete task
def delete_task():
    show_tasks()
    if len(tasks) == 0:
        return
    
    num = int(input("Enter task number to delete: "))
    
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        print(f"Task '{removed}' deleted!")
    else:
        print("Invalid task number.")

# Main loop
while True:
    print("\n--- To-Do App ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")