# TaskMate

## Introduction

TaskMate is a Python-based task management application that utilizes the Model-View-Controller (MVC) design pattern. The application allows users to create, update, and manage tasks, providing a simple yet efficient way to organize your day.

## Features

- Create new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed
- Graphical User Interface
- SQLite database integration

## Installation and Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/TaskMate.git
   ```
2. Navigate to the project directory:  
   ```bash
   cd TaskMate
   ```
3. Install the required packages:  
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the `main.py` script to start the application:
```bash
python main.py
```

## Project Structure

- `main.py`: Entry point for the application.
- `model`: Contains the data-related logic.
- `view`: Houses the graphical interface code.
- `controller`: Handles user inputs and updates the model and view accordingly.
- `tasks.db`: SQLite database for storing tasks.
- `UML.drawio` : UML diagram for the database

## Table

### Task

- id: Provides a unique identifier for each task.
- title: Holds the name or title of the task.
- description: Holds any additional information about the task.
- due_date: Optional, holds the date when the task is supposed to be completed.
- completed: Holds a boolean value to represent whether the task has been completed.
- created_at: Automatically stores the timestamp when the task is created.

[Diagram](assets/diagram.png)

## Contributing

If you would like to contribute to TaskMate, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.