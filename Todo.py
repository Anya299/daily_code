from datetime import datetime

tasks = []

def add_task():
    title = input("Enter task title: ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    
    try:
        deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
    except:
        print("Invalid date format!")
        return
    
    task = {
        "title": title,
        "priority": priority,
        "deadline": deadline_date,
        "completed": False
    }
    
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    
    sorted_tasks = sorted(tasks, key=lambda x: (x["deadline"], x["priority"]))
    
    for i, task in enumerate(sorted_tasks):
        status = "✔" if task["completed"] else "✘"
        print(f"{i+1}. {task['title']} | {task['priority']} | {task['deadline'].date()} | {status}")
    print()

def complete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to complete: ")) - 1
        tasks[task_no]["completed"] = True
        print("Task marked as completed!\n")
    except:
        print("Invalid input!\n")

def menu():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice!\n")

menu()
