# Flask Task Management App

## Overview

This is a simple Task Management web application built using Flask, a lightweight web framework in Python. The app allows users to manage their tasks with features like adding, editing, deleting, and marking tasks as complete. The application includes a welcoming landing page and a clean, user-friendly interface with basic styling.

## Features

- **Add Tasks:** Users can add new tasks to the task list.
- **Edit Tasks:** Users can edit existing tasks to update the task description.
- **Delete Tasks:** Users can delete tasks they no longer need.
- **Complete Tasks:** Users can mark tasks as complete, and the completed tasks will be visually distinguished from the incomplete ones.

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Styling:** Basic custom CSS
- **Development Environment:** Python virtual environment (`venv`)

## Project Structure

/flask_task_app ├── venv/ # Virtual environment directory ├── application.py # Main Flask application file ├── templates/ # Directory for HTML templates │ ├── index.html # Home page template │ ├── welcome.html # Welcome page template │ └── edit.html # Task editing template └── static/ # Directory for static files like CSS └── styles.css # Custom CSS for styling the app


## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)
- `virtualenv` (optional but recommended)

### Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

### Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate


### Install dependencies:

```
pip install Flask

### Run the application

```
python application.py

