def test_signup_adds_participant_to_activity(client):
    """
    Arrange: Activity "Programming Class" with initial participants
    Act: Sign up new email for the activity
    Assert: Email is added to participants list and success message returned
    """
    # Arrange
    activity_name = "Programming Class"
    new_email = "newstudent@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup?email={new_email}"
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {new_email} for {activity_name}"


def test_signup_returns_404_for_nonexistent_activity(client):
    """
    Arrange: Activity name that doesn't exist
    Act: Attempt to sign up for non-existent activity
    Assert: 404 error is returned
    """
    # Arrange
    activity_name = "Non-Existent Club"
    email = "student@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_returns_400_for_duplicate_participant(client):
    """
    Arrange: Email already in "Chess Club" participants
    Act: Attempt to sign up the same email again
    Assert: 400 error is returned with duplicate message
    """
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup?email={existing_email}"
    )
    
    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up for this activity"
