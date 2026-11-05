import requests

def test_events_list_is_not_empty(auth_headers, base_url):
    response = requests.get(
        f"{base_url}/events",
        headers=auth_headers,
    )
    assert response.status_code == 200

    body = response.json()
    assert len(body["data"]) > 0

def test_created_event_exists(auth_headers,base_url,created_event):
    response = requests.get(
        f"{base_url}/events/{created_event['id']}",
        headers=auth_headers,
    )
    assert response.status_code==200

def test_bad_token_is_rejected(base_url):
    bad_headers = {"Authorization": "Bearer abc123 "}   
    response = requests.get(
        f"{base_url}/events",
        headers=bad_headers,
    )
    assert response.status_code == 401

def test_unknown_event_returns_404(auth_headers, base_url):
    response = requests.get(
         f"{base_url}/events/999999999",
         headers=auth_headers,
    )
    event = response.json()["data"][0]
    assert response.status_code==404

    for key in ["id","title", "city", "price","venue","category"]:
        assert key in event, f"missing key:{key}"

    assert isinstance(event["id"], int)
    assert isinstance(event["title"], str)
    assert isinstance(event["totalSeats"], int)