from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Hello from Github Actions & GHCR!"
    assert response.json["version"] == "1.0.0"