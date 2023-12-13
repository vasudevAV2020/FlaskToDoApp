# FlaskToDoApp

This is a simple ToDo application built with Flask.

## Features

- Add, update, and delete tasks.
- View tasks in a table format.
- Navigate between home, about, and update pages.

## Folder Structure
"""
ToDoApp/
│
├── app.py
├── requirements.txt
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── about.html
│ └── update.html
├── Dockerfile
└── env/
└── (Virtual environment - optional)
"""

- **`app.py`**: Contains the Flask application code.
- **`requirements.txt`**: Includes Python dependencies.
- **`templates/`**: Contains HTML templates for the application.
- **`Dockerfile`**: Configuration file to build a Docker image.
- **`env/`**: Directory for a virtual environment (optional).

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/ToDoApp.git
    ```

2. Set up the virtual environment (optional):

    ```bash
    # Navigate to the project directory
    cd ToDoApp

    # Create a virtual environment (optional)
    python -m venv env

    # Activate the virtual environment (Windows)
    env\Scripts\activate

    # Activate the virtual environment (Mac/Linux)
    source env/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    # Run the app directly
    python app.py

    # Build and run the Docker container (if Docker installed)
    docker build -t ToDoApp .
    docker run -p 5000:5000 ToDoApp
    ```

5. Access the application in a web browser at `http://localhost:5000`.
