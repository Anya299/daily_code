from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Task Management API",
    description="A learning project for backend engineering.",
    version="1.0.0",
)

# Request model: data accepted when creating a task.
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    completed: bool = False

# Request model: fields that may be changed using PATCH.
class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)
    completed: bool | None = None

# Response model: data returned to the client.
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool

# Temporary storage. We will replace this with a database later.
tasks: dict[int, TaskResponse] = {}
next_id = 1

@app.get("/")
def home():
    return {"message": "Task Management API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(task_data: TaskCreate):
    global next_id

    task = TaskResponse(
        id=next_id,
        title=task_data.title,
        description=task_data.description,
        completed=task_data.completed,
    )

    tasks[next_id] = task
    next_id += 1

    return task

@app.get("/tasks", response_model=list[TaskResponse])
def get_all_tasks():
    return list(tasks.values())

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    task = tasks.get(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task

@app.patch("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, changes: TaskUpdate):
    task = tasks.get(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    updated_data = changes.model_dump(exclude_unset=True)
    updated_task = task.model_copy(update=updated_data)

    tasks[task_id] = updated_task

    return updated_task

@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    del tasks[task_id]
    return None

'''Understand the important parts

A. FastAPI() creates the application

app = FastAPI()

The app object receives HTTP requests and routes them to the appropriate functions.

B. Pydantic validates request data

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)

FastAPI uses this model to validate incoming JSON. An empty title or an overly long title produces a validation error rather than reaching the function normally.

C. Route parameters

@app.get("/tasks/{task_id}")
def get_task(task_id: int):

If the client requests /tasks/5, FastAPI converts 5 into an integer and passes it to the function.

D. HTTP exceptions

raise HTTPException(status_code=404, detail="Task not found")

This communicates a proper HTTP error instead of returning a misleading success response.

E. Partial updates

changes.model_dump(exclude_unset=True)

This includes only fields the client supplied. For example, {"completed": true} updates completion without replacing the title.

One important nuance: our storage is currently a Python dictionary. This is a learning implementation, not production persistence. The records disappear when the server restarts, and the global state isn't suitable for concurrent production use. We'll replace it with PostgreSQL and proper database sessions during this phase.'''





'''You should see a message indicating the server is running at http://127.0.0.1:8000.

Open these URLs in your browser:

http://127.0.0.1:8000/ — basic endpoint
http://127.0.0.1:8000/health — health check
http://127.0.0.1:8000/docs — interactive API documentation

The /docs page is Swagger UI, generated automatically from your FastAPI routes and request models.

Test the endpoints in Swagger UI

(POST)

Create a task

Endpoint: /tasks

In Swagger, click Try it out and submit:

{
  "title": "Learn FastAPI",
  "description": "Build my first API",
  "completed": false
}

Expected status: 201 Created.

(GET)

Read tasks

Endpoint: /tasks

Expected: a JSON array containing your task.

(GET)

Read one task

Endpoint: /tasks/1

Expected: the task with ID 1, or 404 if it doesn't exist.

(PATCH)

Update a task

Endpoint: /tasks/1

{
  "completed": true
}

Expected: the same task with completed set to true.

(DELETE)

Delete a task

Endpoint: /tasks/1

Expected: 204 No Content. The task should no longer appear in the list.

Important: create a new task before testing /tasks/1 if you have already deleted it. Restarting the server also resets this in-memory data.'''
