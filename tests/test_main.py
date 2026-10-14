import pytest
from fastapi.testclient import TestClient

import app.main as main_module

client = TestClient(main_module.app)

@pytest.fixture(autouse=True)
def reset_tasks():
    main_module.tasks.clear()
    main_module.next_id = 1

def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn FastAPI",
            "description": "Build an API",
        },
    )

    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["title"] == "Learn FastAPI"
    assert response.json()["completed"] is False

def test_get_all_tasks():
    client.post("/tasks", json={"title": "Task A"})
    client.post("/tasks", json={"title": "Task B"})

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_missing_task():
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

def test_update_task():
    created = client.post(
        "/tasks",
        json={"title": "Original title"},
    )
    task_id = created.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={"completed": True},
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Original title"
    assert response.json()["completed"] is True

def test_delete_task():
    created = client.post(
        "/tasks",
        json={"title": "Delete me"},
    )
    task_id = created.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 204
    assert client.get(f"/tasks/{task_id}").status_code == 404

def test_empty_title_is_rejected():
    response = client.post(
        "/tasks",
        json={"title": ""},
    )

    assert response.status_code == 422

#A backend engineer doesn't rely only on clicking buttons. We need automated tests that can run repeatedly.
'''You should see 7 passing tests.

If you get an import error, first check that you are running pytest from inside the day19_fastapi folder and that both __init__.py files exist.

What did we just test?
A successful request
Resource creation
Reading multiple records
A missing resource
A partial update
Deletion
Input validation

This is the beginning of a real backend testing strategy.'''
