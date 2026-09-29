from task import Task
from storage import load_tasks, save_tasks


class TaskManager:

    def __init__(self):
        self.tasks = [
            Task.from_dict(task)
            for task in load_tasks()
        ]

    def get_next_id(self):
        if not self.tasks:
            return 1

        return max(task.task_id for task in self.tasks) + 1

    def add_task(self, description, subject, priority, deadline):
        task = Task(
            self.get_next_id(),
            description,
            subject,
            priority,
            deadline
        )

        self.tasks.append(task)
        self.save()

        return task

    def get_all_tasks(self):
        return self.tasks

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task

        return None

    def update_task(self, task_id, description, subject, priority, deadline):
        task = self.find_task(task_id)

        if task is None:
            return False

        task.description = description
        task.subject = subject
        task.priority = priority
        task.deadline = deadline

        self.save()
        return True

    def delete_task(self, task_id):
        task = self.find_task(task_id)

        if task is None:
            return False

        self.tasks.remove(task)
        self.save()

        return True

    def complete_task(self, task_id):
        task = self.find_task(task_id)

        if task is None:
            return False

        task.mark_completed()
        self.save()

        return True

    def save(self):
        data = [task.to_dict() for task in self.tasks]
        return save_tasks(data)