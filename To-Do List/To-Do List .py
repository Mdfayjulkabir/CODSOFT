# To-Do List 

tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")
