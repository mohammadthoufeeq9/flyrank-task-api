# FlyRank Internship – Task Management API

A simple REST API built using **Python and FastAPI** as part of the FlyRank AI Backend Internship (Week 2 – Assignment 1).

The project demonstrates CRUD (Create, Read, Update, Delete) operations for managing tasks using FastAPI.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Git and GitHub
- Swagger UI

## Project Features

- Create new tasks.
- Retrieve all tasks.
- Retrieve an individual task using its ID.
- Update existing tasks using PUT.
- Delete tasks.
- Automatic task ID generation.
- Input validation.
- HTTP exception handling.

## Task Structure

Each task contains the following fields:

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique task ID |
| title | String | Task title |
| done | Boolean | Task completion status |

Example:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "done": false
}
```

## API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{task_id}` | Retrieve a specific task |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update an existing task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 404 | Not Found |

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd flyrank-task-api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install fastapi uvicorn
```

### 6. Run the application

```bash
uvicorn main:app --reload
```

## API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Open the following URL after starting the server:

http://127.0.0.1:8000/docs

You can test all available endpoints directly through Swagger UI.

## Data Storage

This project currently uses an **in-memory Python list** to store tasks.

No database is connected at this stage.

Task data will be lost whenever the server restarts.

## Learning Outcomes

- Understanding REST APIs.
- Implementing CRUD operations.
- Working with HTTP methods.
- Using path parameters.
- Validating request data with Pydantic.
- Handling HTTP exceptions.
- Testing APIs using Swagger UI.

