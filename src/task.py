class Task:
    def __init__(self, task_id, description, subject, priority, deadline, status="Pending"):
        self.task_id = task_id
        self.description = description
        self.subject = subject
        self.priority = priority
        self.deadline = deadline
        self.status = status

    def mark_completed(self):
        self.status = "Completed"

    def to_dict(self):
        return {
            "id": self.task_id,
            "description": self.description,
            "subject": self.subject,
            "priority": self.priority,
            "deadline": self.deadline,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["id"],
            data["description"],
            data["subject"],
            data["priority"],
            data["deadline"],
            data["status"]
        )