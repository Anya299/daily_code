# Task Management API

A REST API built with FastAPI for creating, retrieving,
updating, and deleting tasks.

## Features

- Create tasks
- Retrieve all tasks or a task by ID
- Partially update tasks
- Delete tasks
- Validate request data
- Return meaningful HTTP status codes
- Automated API tests

## Tech Stack

- Python
- FastAPI
- Pydantic
- Pytest
- HTTPX

## Installation

Install dependencies:

    python -m pip install -r requirements.txt

## Run the API

    python -m uvicorn app.main:app --reload

## API Documentation

Visit http://127.0.0.1:8000/docs

## Run Tests

    python -m pytest -v

## Architecture

The API uses FastAPI for routing, Pydantic for request
validation, and an in-memory dictionary for temporary storage.

## Limitations

Data is lost when the application restarts.
The next version will use PostgreSQL for persistent storage.

## Future Improvements

- PostgreSQL integration
- SQLAlchemy ORM
- Authentication and authorization
- Pagination and filtering
- Database integration tests
- Docker deployment