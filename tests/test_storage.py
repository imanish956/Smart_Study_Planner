import sys
import os
import json
import tempfile

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

import storage


def test_save_and_load_tasks():

    original_file = storage.DATA_FILE

    with tempfile.NamedTemporaryFile(
        mode="w",
        delete=False
    ) as temp_file:

        temp_path = temp_file.name

    storage.DATA_FILE = temp_path

    test_tasks = [
        {
            "id": 1,
            "description": "Test Task",
            "subject": "Python",
            "priority": "High",
            "deadline": "30-09-2026",
            "status": "Pending"
        }
    ]

    assert storage.save_tasks(test_tasks) is True

    loaded_tasks = storage.load_tasks()

    assert loaded_tasks == test_tasks

    os.remove(temp_path)

    storage.DATA_FILE = original_file