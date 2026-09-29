def validate_description(description):
    return bool(description.strip())


def validate_subject(subject):
    return bool(subject.strip())


def validate_priority(priority):
    return priority.lower() in ["low", "medium", "high"]


def validate_deadline(deadline):
    return bool(deadline.strip())


def validate_task_id(task_id):
    try:
        return int(task_id) > 0
    except ValueError:
        return False