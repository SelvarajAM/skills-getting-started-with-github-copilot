from urllib.parse import quote
from src.app import activities


def test_signup_success(client):
    # Arrange
    activity = "Tennis Club"
    email = "newstudent@mergington.edu"
    assert email not in activities[activity]["participants"]
    # Act
    resp = client.post(f"/activities/{quote(activity)}/signup", params={"email": email})
    # Assert
    assert resp.status_code == 200
    assert resp.json()["message"] == f"Signed up {email} for {activity}"
    assert email in activities[activity]["participants"]


def test_signup_duplicate(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"
    assert email in activities[activity]["participants"]
    # Act
    resp = client.post(f"/activities/{quote(activity)}/signup", params={"email": email})
    # Assert
    assert resp.status_code == 400


def test_signup_activity_not_found(client):
    # Arrange
    activity = "Nonexistent Activity"
    email = "nobody@mergington.edu"
    # Act
    resp = client.post(f"/activities/{quote(activity)}/signup", params={"email": email})
    # Assert
    assert resp.status_code == 404
