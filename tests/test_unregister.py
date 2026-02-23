from urllib.parse import quote
from src.app import activities


def test_unregister_success(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"
    assert email in activities[activity]["participants"]
    # Act
    resp = client.delete(f"/activities/{quote(activity)}/participants", params={"email": email})
    # Assert
    assert resp.status_code == 200
    assert resp.json()["message"] == f"Unregistered {email} from {activity}"
    assert email not in activities[activity]["participants"]


def test_unregister_not_registered(client):
    # Arrange
    activity = "Tennis Club"
    email = "notregistered@mergington.edu"
    assert email not in activities[activity]["participants"]
    # Act
    resp = client.delete(f"/activities/{quote(activity)}/participants", params={"email": email})
    # Assert
    assert resp.status_code == 404


def test_unregister_activity_not_found(client):
    # Arrange
    activity = "NoSuchActivity"
    email = "nobody@mergington.edu"
    # Act
    resp = client.delete(f"/activities/{quote(activity)}/participants", params={"email": email})
    # Assert
    assert resp.status_code == 404
