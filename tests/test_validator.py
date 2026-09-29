import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from validator import (
    validate_description,
    validate_subject,
    validate_priority,
    validate_deadline,
    validate_task_id
)


def test_valid_description():
    assert validate_description("Complete Python assignment") is True


def test_empty_description():
    assert validate_description("") is False


def test_valid_subject():
    assert validate_subject("Python") is True


def test_valid_priority():
    assert validate_priority("High") is True
    assert validate_priority("Medium") is True
    assert validate_priority("Low") is True


def test_invalid_priority():
    assert validate_priority("Very High") is False


def test_valid_deadline():
    assert validate_deadline("30-09-2026") is True


def test_valid_task_id():
    assert validate_task_id("1") is True


def test_invalid_task_id():
    assert validate_task_id("abc") is False