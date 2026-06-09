def test_root_redirects_to_index(client):
    """
    Arrange: Client is ready
    Act: Call GET /
    Assert: Redirect response to /static/index.html
    """
    # Act
    response = client.get("/", follow_redirects=False)
    
    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"
