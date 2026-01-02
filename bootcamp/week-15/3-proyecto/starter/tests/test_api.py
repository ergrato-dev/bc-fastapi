# ============================================
# API Tests
# Semana 15 - Proyecto Integrador
# ============================================
#
# Completa los TODOs para escribir tests
# que cubran toda la funcionalidad.
# ============================================

from fastapi.testclient import TestClient


# ============================================
# Health Tests
# ============================================
class TestHealth:
    """Tests for health endpoints"""

    def test_health_check(self, client: TestClient) -> None:
        """Test basic health endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "version" in data

    def test_liveness(self, client: TestClient) -> None:
        """Test liveness probe"""
        response = client.get("/health/live")
        assert response.status_code == 200
        assert response.json()["status"] == "alive"

    def test_readiness(self, client: TestClient) -> None:
        """Test readiness probe"""
        response = client.get("/health/ready")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert "database" in data


# ============================================
# Tasks Tests
# ============================================
class TestTasks:
    """Tests for tasks CRUD endpoints"""

    # ============================================
    # TODO 1: Test crear tarea
    # ============================================
    def test_create_task(self, client: TestClient) -> None:
        """Test creating a new task"""
        task_data = {
            "title": "Test Task",
            "description": "Test description",
            "priority": "high",
        }
        response = client.post("/api/v1/tasks", json=task_data)

        assert response.status_code == 201
        data = response.json()
        assert data["title"] == task_data["title"]
        assert data["description"] == task_data["description"]
        assert data["priority"] == task_data["priority"]
        assert data["completed"] is False
        assert "id" in data
        assert "created_at" in data

    # ============================================
    # TODO 2: Test validación
    # ============================================
    def test_create_task_validation(self, client: TestClient) -> None:
        """Test task creation validation"""
        # Empty title should fail
        response = client.post("/api/v1/tasks", json={"title": ""})
        assert response.status_code == 422

        # Missing title should fail
        response = client.post("/api/v1/tasks", json={"description": "No title"})
        assert response.status_code == 422

    # ============================================
    # TODO 3: Test obtener tarea
    # ============================================
    def test_get_task(self, client: TestClient) -> None:
        """Test getting a task by ID"""
        # Create task first
        create_response = client.post(
            "/api/v1/tasks",
            json={"title": "Get Test"},
        )
        task_id = create_response.json()["id"]

        # Get task
        response = client.get(f"/api/v1/tasks/{task_id}")
        assert response.status_code == 200
        assert response.json()["id"] == task_id

    def test_get_task_not_found(self, client: TestClient) -> None:
        """Test getting non-existent task"""
        response = client.get("/api/v1/tasks/99999")
        assert response.status_code == 404

    # ============================================
    # TODO 4: Test listar tareas
    # ============================================
    def test_list_tasks(self, client: TestClient) -> None:
        """Test listing tasks with pagination"""
        # Create multiple tasks
        for i in range(5):
            client.post("/api/v1/tasks", json={"title": f"Task {i}"})

        # List all
        response = client.get("/api/v1/tasks")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 5
        assert len(data["items"]) == 5

    def test_list_tasks_pagination(self, client: TestClient) -> None:
        """Test pagination"""
        # Create 15 tasks
        for i in range(15):
            client.post("/api/v1/tasks", json={"title": f"Task {i}"})

        # Page 1 with size 10
        response = client.get("/api/v1/tasks?page=1&size=10")
        data = response.json()
        assert len(data["items"]) == 10
        assert data["pages"] == 2

        # Page 2
        response = client.get("/api/v1/tasks?page=2&size=10")
        data = response.json()
        assert len(data["items"]) == 5

    # ============================================
    # TODO 5: Test actualizar tarea
    # ============================================
    def test_update_task(self, client: TestClient) -> None:
        """Test updating a task"""
        # Create task
        create_response = client.post(
            "/api/v1/tasks",
            json={"title": "Original Title"},
        )
        task_id = create_response.json()["id"]

        # Update
        response = client.put(
            f"/api/v1/tasks/{task_id}",
            json={"title": "Updated Title", "completed": True},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Updated Title"
        assert data["completed"] is True

    def test_update_task_not_found(self, client: TestClient) -> None:
        """Test updating non-existent task"""
        response = client.put(
            "/api/v1/tasks/99999",
            json={"title": "Update"},
        )
        assert response.status_code == 404

    # ============================================
    # TODO 6: Test eliminar tarea
    # ============================================
    def test_delete_task(self, client: TestClient) -> None:
        """Test deleting a task"""
        # Create task
        create_response = client.post(
            "/api/v1/tasks",
            json={"title": "To Delete"},
        )
        task_id = create_response.json()["id"]

        # Delete
        response = client.delete(f"/api/v1/tasks/{task_id}")
        assert response.status_code == 204

        # Verify deleted
        get_response = client.get(f"/api/v1/tasks/{task_id}")
        assert get_response.status_code == 404

    def test_delete_task_not_found(self, client: TestClient) -> None:
        """Test deleting non-existent task"""
        response = client.delete("/api/v1/tasks/99999")
        assert response.status_code == 404


# ============================================
# Root Tests
# ============================================
class TestRoot:
    """Tests for root endpoint"""

    def test_root(self, client: TestClient) -> None:
        """Test root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "version" in data
