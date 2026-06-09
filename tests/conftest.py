import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def reset_activities():
    """Reset activities to initial state before each test"""
    # Store the initial state
    initial_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball": {
            "description": "Competitive basketball team and practice sessions",
            "schedule": "Tuesdays, Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["james@mergington.edu"]
        },
        "Track and Field": {
            "description": "Running, jumping, and throwing events for all levels",
            "schedule": "Mondays, Wednesdays, Fridays, 4:00 PM - 5:00 PM",
            "max_participants": 25,
            "participants": ["sarah@mergington.edu", "marcus@mergington.edu"]
        },
        "Art Studio": {
            "description": "Painting, drawing, and sculpture techniques",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["isabella@mergington.edu"]
        },
        "Music Band": {
            "description": "Instrumental music ensemble and performance opportunities",
            "schedule": "Mondays, Wednesdays, 4:30 PM - 6:00 PM",
            "max_participants": 24,
            "participants": ["lucas@mergington.edu", "grace@mergington.edu"]
        },
        "Debate Club": {
            "description": "Develop argumentative and public speaking skills",
            "schedule": "Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["aiden@mergington.edu"]
        },
        "Science Club": {
            "description": "Explore biology, chemistry, and physics through hands-on experiments",
            "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["nina@mergington.edu", "ethan@mergington.edu"]
        }
    }
    
    # Clear current activities and restore initial state
    activities.clear()
    activities.update(initial_activities)
    yield
    # Cleanup after test
    activities.clear()
    activities.update(initial_activities)


@pytest.fixture
def client(reset_activities):
    """Provide a TestClient for testing the FastAPI app"""
    return TestClient(app)
