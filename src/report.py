def generate_report(tasks):

    total = len(tasks)

    completed = sum(
        1 for task in tasks
        if task.status == "Completed"
    )

    pending = total - completed

    if total > 0:
        completion_rate = (completed / total) * 100
    else:
        completion_rate = 0

    print("\n========== TASK REPORT ==========")

    print(f"Total Tasks      : {total}")
    print(f"Completed Tasks  : {completed}")
    print(f"Pending Tasks    : {pending}")
    print(f"Completion Rate  : {completion_rate:.2f}%")

    print("=================================")