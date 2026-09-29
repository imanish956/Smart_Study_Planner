def search_tasks(tasks, keyword):
    keyword = keyword.lower()

    results = []

    for task in tasks:
        if (
            keyword in task.description.lower()
            or keyword in task.subject.lower()
        ):
            results.append(task)

    return results


def filter_by_status(tasks, status):
    return [
        task for task in tasks
        if task.status.lower() == status.lower()
    ]


def filter_by_priority(tasks, priority):
    return [
        task for task in tasks
        if task.priority.lower() == priority.lower()
    ]