def test_get_activities_returns_all_activities(client):
    """
    Arrange: Client is ready with activities initialized
    Act: Call GET /activities
    Assert: All activities are returned with correct structure
    """
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert response.status_code == 200
    assert len(data) == 9
    assert "Chess Club" in data
    assert "Programming Class" in data
    assert "Gym Class" in data


def test_get_activities_contains_correct_structure(client):
    """
    Arrange: Client is ready
    Act: Call GET /activities and inspect activity structure
    Assert: Each activity has required fields
    """
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    activity = data["Chess Club"]
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity
    assert isinstance(activity["participants"], list)
    assert len(activity["participants"]) == 2


def test_get_activities_returns_current_participants(client):
    """
    Arrange: Client is ready
    Act: Call GET /activities
    Assert: Participants list reflects initial state
    """
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert "michael@mergington.edu" in data["Chess Club"]["participants"]
    assert "daniel@mergington.edu" in data["Chess Club"]["participants"]
