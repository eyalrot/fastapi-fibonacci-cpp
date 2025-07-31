import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestAPIEndpoints:
    def test_root(self):
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "implementation" in data
        assert "endpoints" in data

    def test_fibonacci_endpoint(self):
        test_cases = [
            (0, 0),
            (1, 1),
            (10, 55),
            (20, 6765),
        ]

        for n, expected in test_cases:
            response = client.get(f"/fibonacci/{n}")
            assert response.status_code == 200
            data = response.json()
            assert data["n"] == n
            assert data["value"] == expected

    def test_fibonacci_sequence_endpoint(self):
        response = client.get("/fibonacci/sequence/10")
        assert response.status_code == 200
        data = response.json()
        assert data["n"] == 10
        assert data["sequence"] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    def test_fibonacci_info_endpoint(self):
        response = client.get("/fibonacci/info/10")
        assert response.status_code == 200
        data = response.json()
        assert data["n"] == 10
        assert data["value"] == 55
        assert data["is_even"] is False
        assert data["digits"] == 2

    def test_status_endpoint(self):
        response = client.get("/status")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "running"
        assert "implementation" in data
        assert "performance" in data


class TestAPIErrorHandling:
    def test_negative_input_fibonacci(self):
        response = client.get("/fibonacci/-1")
        assert response.status_code == 400
        assert "n must be a non-negative integer" in response.json()["detail"]

    def test_large_input_fibonacci(self):
        response = client.get("/fibonacci/10001")
        assert response.status_code == 400
        assert "n is too large" in response.json()["detail"]

    def test_negative_input_sequence(self):
        response = client.get("/fibonacci/sequence/-5")
        assert response.status_code == 400

    def test_large_input_sequence(self):
        response = client.get("/fibonacci/sequence/1001")
        assert response.status_code == 400
        assert "n is too large" in response.json()["detail"]

    def test_invalid_endpoint(self):
        response = client.get("/fibonacci/invalid")
        assert response.status_code == 422  # Unprocessable Entity


class TestAPIPerformance:
    def test_response_time_small_numbers(self):
        import time

        start = time.time()
        response = client.get("/fibonacci/100")
        elapsed = time.time() - start

        assert response.status_code == 200
        assert elapsed < 0.1  # Should respond in less than 100ms

    def test_response_time_large_numbers(self):
        import time

        start = time.time()
        response = client.get("/fibonacci/1000")
        elapsed = time.time() - start

        assert response.status_code == 200
        assert elapsed < 0.5  # Should respond in less than 500ms


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
