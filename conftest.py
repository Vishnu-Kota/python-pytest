import os
from datetime import datetime, timedelta, timezone

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def token():
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "email": os.getenv("EVENTHUB_EMAIL"),
        "password": os.getenv("EVENTHUB_PASSWORD"),
    })
    assert response.status_code == 200
    return response.json()["token"]


@pytest.fixture
def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def created_event(auth_headers):
    event = {
        "title": f"pytest event {datetime.now().timestamp()}",
        "category": "Conference",
        "venue": "Test Venue",
        "city": "Bangalore",
        "eventDate": (datetime.now(timezone.utc) + timedelta(days=7)).isoformat(),
        "price": 100,
        "totalSeats": 50,
    }
    response = requests.post(f"{BASE_URL}/events", json=event, headers=auth_headers)
    assert response.status_code == 201
    created = response.json()["data"]

    yield created

    requests.delete(f"{BASE_URL}/events/{created['id']}", headers=auth_headers)