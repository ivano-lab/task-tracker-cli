# Task Tracker CLI

## Description

This project provides a solid foundation for managing tasks via a CLI using Python.

## Features

- Add tasks
- Update tasks
- Delete tasks
- List all tasks
- Filter tasks by status (completed, pending, in progress)

## Installation

To install and run this project, you need to have Python 3 or higher installed on your machine. You can download Python from the official website: [python.org](https://www.python.org/downloads/).

## Running the Application

To run the application, navigate to the task_cli directory in your terminal and use the following commands:

Add a new task:

```python task_cli.py add "Buy groceries"```

Update a task:

python task_cli.py update 1 "Buy groceries and cook dinner"

Delete a task:

```python task_cli.py delete 1```

Mark a task as in progress:

```python task_cli.py mark-in-progress 1```

Mark a task as done:

```python task_cli.py mark-done 1```

List all tasks:

```python task_cli.py list```

List done tasks:

```python task_cli.py list done```

List todo tasks:

```python task_cli.py list todo```

List in-progress tasks:

```python task_cli.py list in-progress```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
