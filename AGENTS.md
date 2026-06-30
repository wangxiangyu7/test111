# Repository Guidelines

This repository contains one Flask application in `bookmark-manager/`.

## Working Directory

- Run git commands from the repository root.
- Run application commands from `bookmark-manager/`, unless a command explicitly says otherwise.

## Application Setup

```bash
cd bookmark-manager
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python run.py
```

The development server listens on `http://127.0.0.1:5000` by default.

## Project Structure

- `bookmark-manager/run.py` creates and runs the Flask app.
- `bookmark-manager/app/__init__.py` configures Flask, SQLAlchemy, and database table creation.
- `bookmark-manager/app/models.py` contains SQLAlchemy models.
- `bookmark-manager/app/routes.py` contains Flask routes and view logic.
- `bookmark-manager/app/templates/` contains Jinja templates.
- `bookmark-manager/app/static/css/style.css` contains custom CSS.

## Development Notes

- Keep changes scoped to the Flask app unless the ticket requires repository-level edits.
- Preserve the current simple Flask blueprint structure.
- Use SQLAlchemy APIs for database changes rather than raw SQL.
- Keep user-facing text consistent with the surrounding template language and style.
- Do not commit generated local files such as `.venv/`, `instance/`, `*.db`, `__pycache__/`, or `.env`.

## Verification

There is no test suite in the repository currently. For code changes, at minimum run:

```bash
cd bookmark-manager
python -m compileall app run.py
```

For behavior changes, also start the app with `python run.py` and manually exercise the affected route in a browser.
