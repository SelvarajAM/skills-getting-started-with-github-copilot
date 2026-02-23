from src.app import activities


def test_get_activities(client):
    # Arrange
    expected = activities
    # Act
    resp = client.get("/activities")
    # Assert
    assert resp.status_code == 200
    assert resp.json() == expected
