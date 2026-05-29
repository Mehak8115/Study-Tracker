# Study Tracker API

A CRUD-based REST API built with FastAPI, SQLAlchemy, and SQLite for tracking study sessions. The project demonstrates API development, database integration, dependency injection, and ORM-based data management.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Project Structure

```
study_tracker_api/
├── main.py        # API routes and app entry point
├── models.py      # SQLAlchemy database models
├── schemas.py     # Pydantic request/response schemas
├── database.py    # Database connection and session setup
└── study_tracker.db  # SQLite database file
```

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv myenv
myenv\Scripts\activate
```

2. Install dependencies:
```bash
pip install fastapi sqlalchemy uvicorn
```

3. Run the server:
```bash
cd study_tracker_api
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:5000`

Interactive docs at `http://127.0.0.1:5000/docs`

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/sessions` | Create a new study session |
| GET | `/sessions` | Get all study sessions |
| GET | `/sessions/{id}` | Get a session by ID |
| PUT | `/sessions/{id}` | Update a session by ID |
| DELETE | `/sessions/{id}` | Delete a session by ID |

## Request Body

Used for `POST` and `PUT` requests:

```json
{
  "topic": "FastAPI",
  "hours_spent": 2.5,
  "status": "completed"
}
```

## Response Example

```json
{
  "id": 1,
  "topic": "FastAPI",
  "hours_spent": 2.5,
  "status": "completed"
}
```
