import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from task import Task


def test_create_task():
    task = Task(
        1,
        "Complete Python assignment",
        "Python",
        "High",
        "30-09-2026"
    )

    assert task.task_id == 1
    assert task.description == "Complete Python assignment"
    assert task.subject == "Python"
    assert task.priority == "High"
    assert task.status == "Pending"


def test_mark_completed():
    task = Task(
        1,
        "Study Python",
        "Python",
        "Medium",
        "30-09-2026"
    )

    task.mark_completed()

    assert task.status == "Completed"


def test_task_to_dict():
    task = Task(
        1,
        "Study Python",
        "Python",
        "Medium",
        "30-09-2026"
    )

    data = task.to_dict()

    assert data["id"] == 1
    assert data["description"] == "Study Python"
    assert data["status"] == "Pending"