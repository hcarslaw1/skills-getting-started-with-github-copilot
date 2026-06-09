def test_unregister_removes_participant_from_activity(client):
    """
    Arrange: Email is in "Chess Club" participants
    Act: Unregister that email from the activity
    Assert: Email is removed and success message returned
    """
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister?email={email}"
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"


def test_unregister_returns_404_for_nonexistent_activity(client):
    """
    Arrange: Activity name that doesn't exist
    Act: Attempt to unregister from non-existent activity
    Assert: 404 error is returned
    """
    # Arrange
    activity_name = "Fake Activity"
    email = "student@mergington.edu"
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister?email={email}"
    )
    
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_400_for_unregistered_participant(client):
    """
    Arrange: Email not in "Art Studio" participants
    Act: Attempt to unregister an email not registered for the activity
    Assert: 400 error is returned
    """
    # Arrange
    activity_name = "Art Studio"
    unregistered_email = "notregistered@mergington.edu"
    
    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister?email={unregistered_email}"
    )
    
    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not registered for this activity"
