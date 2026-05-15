tasks = []

def create_task():
    subject = input("Enter subject: ")
    task = input("Enter study task: ")
    due_date = input("Enter due date: ")
    priority = input("Enter priority (High/Medium/Low): ")

    if not task:
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