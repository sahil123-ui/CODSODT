# todo.py

tasks = []

def show_tasks():
    print("\nTo-Do List:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")
    print()

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def delete_task():
    show_tasks()
    task_no = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks.pop(task_no)
        print("Task deleted!")
    else:
        print("Invalid task number!")

while True:
    print("\n1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")
