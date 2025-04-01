from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_submit_message_authorized(monkeypatch):
    def mock_send_message_to_kafka(msg):
        assert msg["content"] == "Hello Kafka!"

    monkeypatch.setattr("app.kafka_producer.send_message_to_kafka", mock_send_message_to_kafka)

    response = client.post(
        "/messages/submit",
        json={"content": "Hello Kafka!"},
        headers={"Authorization": "Bearer admin-token"}
    )
    assert response.status_code == 200
    assert response.json() == {"status": "submitted"}


def test_submit_message_unauthorized():
    response = client.post(
        "/messages/submit",
        json={"content": "Should fail"},
        headers={"Authorization": "Bearer user-token"}
    )
    assert response.status_code == 403
