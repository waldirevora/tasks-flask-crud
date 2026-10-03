import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

# CREATE
def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descricao da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])

# READ ALL
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

# READ ONE
def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["id"] == task_id

# UPDATE
def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "title": "Título atualizado",
            "description": "Descrição atualizada",
            "completed": True
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        # Valida se as alterações foram salvas consultando a tarefa
        response_get = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response_get.status_code == 200
        assert response_get.json()["title"] == payload["title"]
        assert response_get.json()["completed"] == payload["completed"]

# DELETE
def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200

        # Confirma que a tarefa não existe mais
        response_get = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response_get.status_code == 404