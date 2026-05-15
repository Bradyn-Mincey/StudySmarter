tasks = []

def create_task():
    subject = input("Enter subject: ")
    task = input("Enter study task: ")
    due_date = input("Enter due date: ")
    priority = input("Enter priority (High/Medium/Low): ")

    if task.strip() == "":
        print("No task provided.")
        return

    task_data = {
        "subject": subject,
        "task": task,
        "due_date": due_date,
        "priority": priority
    }

    tasks.append(task_data)

    print("Study task added!")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n===== Study Tasks =====")

    for i, task in enumerate(tasks):
        print(f"""
Task #{i+1}
Subject: {task['subject']}
Task: {task['task']}
Due Date: {task['due_date']}
Priority: {task['priority']}
""")


while True:

    print("""
===== StudySmarter =====
1. Create Task
2. View Tasks
3. Exit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        create_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        print("Exiting StudySmarter...")
        break

    else:
        print("Invalid option.")