# Music Production Manager

## Overview

Music Production Manager is a Django web application designed to help users organize and manage their music production projects in one place.

The application allows users to track their music projects from the initial idea to the final release, manage tasks and notes, store track versions, and analyze their creative activity.

## Features

- Create, view, edit, and delete music projects.
- Store project details, including genre, status, BPM, musical key, release date, duration, description, and cover image.
- Organize projects by genre and production status.
- Search projects by title.
- Filter projects by genre and status.
- Navigate through projects using pagination.
- Create and manage tasks for each project.
- Create and manage project notes.
- Store and manage different versions of a track.
- View a dashboard with project and task statistics.
- Analyze project distribution by status and genre.
- Generate charts using Matplotlib.
- Analyze project data using Pandas.

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap 5
- Pandas
- Matplotlib

## Project Structure

- `config/` — main Django project configuration.
- `projects/` — music project models, forms, views, templates, and tests.
- `analytics/` — dashboard and music production analytics.
- `templates/` — shared HTML templates.
- `static/` — static files, including CSS.
- `media/` — uploaded project cover images.
- `manage.py` — Django management utility.
- `requirements.txt` — project dependencies.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd MusicProductionManager
```

Replace `YOUR_REPOSITORY_URL` with the actual repository URL.

If you already have the project files, open the project directory in your terminal instead.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and configure the environment variables required by the project, including `SECRET_KEY`.

Do not commit secret keys or other sensitive configuration values to version control.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

## Testing

Run all automated tests:

```bash
python manage.py test
```

Run tests for the projects application:

```bash
python manage.py test projects
```

Run tests for the analytics application:

```bash
python manage.py test analytics
```

## Purpose

This project was developed as coursework to demonstrate the practical application of Django, relational database models, CRUD operations, form validation, search and filtering, data visualization, and automated testing in a web application.

## Future Improvements

- Add multilingual support.
- Expand analytics and reporting.
- Improve project management workflows.
- Introduce additional music production statistics.
