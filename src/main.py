from task_manager import TaskManager
from search import search_tasks, filter_by_status, filter_by_priority
from report import generate_report
from validator import (
    validate_description,
    validate_subject,
    validate_priority,
    validate_deadline,
    validate_task_id
)


manager = TaskManager()


def display_task(task):
    print(
        f"ID: {task.task_id} | "
        f"Description: {task.description} | "
        f"Subject: {task.subject} | "
        f"Priority: {task.priority} | "
        f"Deadline: {task.deadline} | "
        f"Status: {task.status}"
    )


def add_task():
    print("\n========== ADD TASK ==========")

    description = input("Enter task description: ")

    if not validate_description(description):
        print("Error: Description cannot be empty.")
        return

    subject = input("Enter subject: ")

    if not validate_subject(subject):
        print("Error: Subject cannot be empty.")
        return

    priority = input("Enter priority (Low/Medium/High): ")

    if not validate_priority(priority):
        print("Error: Invalid priority.")
        return

    deadline = input("Enter deadline (DD-MM-YYYY): ")

    if not validate_deadline(deadline):
        print("Error: Deadline cannot be empty.")
        return

    task = manager.add_task(
        description,
        subject,
        priority.capitalize(),
        deadline
    )

    print(f"Task added successfully! Task ID: {task.task_id}")


def view_tasks():
    print("\n========== ALL TASKS ==========")

    tasks = manager.get_all_tasks()

    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        display_task(task)


def update_task():
    print("\n========== UPDATE TASK ==========")

    task_id = input("Enter task ID: ")

    if not validate_task_id(task_id):
        print("Invalid task ID.")
        return

    task_id = int(task_id)

    task = manager.find_task(task_id)

    if task is None:
        print("Task not found.")
        return

    description = input("Enter new description: ")
    subject = input("Enter new subject: ")
    priority = input("Enter new priority (Low/Medium/High): ")
    deadline = input("Enter new deadline: ")

    if not validate_description(description):
        print("Invalid description.")
        return

    if not validate_subject(subject):
        print("Invalid subject.")
        return

    if not validate_priority(priority):
        print("Invalid priority.")
        return

    if not validate_deadline(deadline):
        print("Invalid deadline.")
        return

    manager.update_task(
        task_id,
        description,
        subject,
        priority.capitalize(),
        deadline
    )

    print("Task updated successfully.")


def delete_task():
    print("\n========== DELETE TASK ==========")

    task_id = input("Enter task ID: ")

    if not validate_task_id(task_id):
        print("Invalid task ID.")
        return

    if manager.delete_task(int(task_id)):
        print("Task deleted successfully.")
    else:
        print("Task not found.")


def complete_task():
    print("\n========== COMPLETE TASK ==========")

    task_id = input("Enter task ID: ")

    if not validate_task_id(task_id):
        print("Invalid task ID.")
        return

    if manager.complete_task(int(task_id)):
        print("Task marked as completed.")
    else:
        print("Task not found.")


def search_task():
    print("\n========== SEARCH TASK ==========")

    keyword = input("Enter keyword: ")

    results = search_tasks(
        manager.get_all_tasks(),
        keyword
    )

    if not results:
        print("No matching tasks found.")
        return

    for task in results:
        display_task(task)


def filter_tasks():
    print("\n========== FILTER TASKS ==========")

    print("1. Pending")
    print("2. Completed")
    print("3. High Priority")
    print("4. Medium Priority")
    print("5. Low Priority")

    choice = input("Choose option: ")

    if choice == "1":
        results = filter_by_status(
            manager.get_all_tasks(),
            "Pending"
        )

    elif choice == "2":
        results = filter_by_status(
            manager.get_all_tasks(),
            "Completed"
        )

    elif choice == "3":
        results = filter_by_priority(
            manager.get_all_tasks(),
            "High"
        )

    elif choice == "4":
        results = filter_by_priority(
            manager.get_all_tasks(),
            "Medium"
        )

    elif choice == "5":
        results = filter_by_priority(
            manager.get_all_tasks(),
            "Low"
        )

    else:
        print("Invalid choice.")
        return

    if not results:
        print("No tasks found.")
        return

    for task in results:
        display_task(task)


def main():

    while True:

        print("\n")
        print("========================================")
        print("   STUDENT TASK & ASSIGNMENT MANAGER")
        print("========================================")

        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Completed")
        print("6. Search Task")
        print("7. Filter Tasks")
        print("8. Generate Report")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            complete_task()

        elif choice == "6":
            search_task()

        elif choice == "7":
            filter_tasks()

        elif choice == "8":
            generate_report(manager.get_all_tasks())

        elif choice == "9":
            print("Thank you for using Student Task Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()