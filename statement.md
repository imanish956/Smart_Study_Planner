# Project Statement

## Project Title

Student Task & Assignment Manager

---

## 1. Problem Statement

Students regularly manage multiple academic assignments, homework, projects, tests, and other tasks. When these tasks are tracked manually, it can become difficult to remember deadlines and identify which tasks are completed or still pending.

The Student Task & Assignment Manager provides a simple Python-based solution for organizing academic tasks in one place.

The system allows students to create tasks, view and modify them, mark tasks as completed, search for specific tasks, filter tasks according to different conditions, and view overall task completion statistics.

---

## 2. Project Scope

The scope of the project includes the development of a command-line Python application for managing academic tasks.

The system supports:

* Creating academic tasks.
* Viewing existing tasks.
* Updating task information.
* Deleting tasks.
* Marking tasks as completed.
* Searching for tasks.
* Filtering tasks by status and priority.
* Generating task statistics.
* Saving task data using JSON file storage.
* Validating user input.
* Handling invalid input safely.
* Testing important application components.

The project is intended for individual student use.

---

## 3. Target Users

The primary target users are:

* College students.
* School students.
* Students managing multiple assignments.
* Students who want a simple task tracking system.

---

## 4. High-Level Features

### 4.1 Task Management

Users can:

* Add tasks.
* View tasks.
* Update tasks.
* Delete tasks.
* Mark tasks as completed.

### 4.2 Task Search

Users can search for tasks using:

* Task description.
* Subject name.

### 4.3 Task Filtering

Users can filter tasks according to:

* Pending status.
* Completed status.
* High priority.
* Medium priority.
* Low priority.

### 4.4 Task Reporting

The system provides:

* Total task count.
* Completed task count.
* Pending task count.
* Completion percentage.

### 4.5 Data Storage

Task information is stored in a JSON file so that the data remains available when the program is restarted.

### 4.6 Input Validation

The system validates user-provided information such as:

* Task description.
* Subject.
* Priority.
* Deadline.
* Task ID.

---

## 5. Functional Modules

The project contains the following major functional modules:

### Module 1: Task Management

Responsible for creating, viewing, updating, deleting, and completing tasks.

### Module 2: Search and Filtering

Responsible for searching tasks and filtering them according to status and priority.

### Module 3: Data Storage

Responsible for reading and writing task information using JSON.

### Module 4: Reporting

Responsible for calculating and displaying task statistics.

### Module 5: Validation

Responsible for checking user input before processing it.

---

## 6. Expected Input

The system accepts:

* Task description.
* Subject.
* Priority.
* Deadline.
* Task ID.
* Search keywords.
* Menu selections.

---

## 7. Expected Output

The system produces:

* Task information.
* Success messages.
* Error messages.
* Search results.
* Filtered task lists.
* Completion statistics.
* Task reports.

---

## 8. Technologies

The project uses:

* Python
* JSON
* Pytest
* Git
* GitHub

---

## 9. Project Limitations

The current version is a command-line application and is designed for local individual use.

It does not currently provide:

* Cloud synchronization.
* Multi-user accounts.
* Mobile application support.
* Automatic notifications.
* Online database storage.

---

## 10. Future Scope

Future versions may include:

* Graphical user interface.
* Database integration.
* Automatic deadline reminders.
* Calendar integration.
* Multi-user support.
* Cloud synchronization.
* Mobile application.
* Progress visualization.
