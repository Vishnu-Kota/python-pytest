![tests](https://github.com/Vishnu-Kota/python-pytest/actions/workflows/tests.yml/badge.svg)

# EventHub API tests (pytest)

API test suite for the EventHub practice app, written in Python with pytest and requests.

## What it covers

- **Login once per run:** a session-scoped `token` fixture logs in and shares the bearer token through an `auth_headers` fixture.
- **Test data with cleanup:** a `created_event` fixture creates an event through the API, yields it to the test, and deletes it afterwards.
- **Positive tests:** the events list is not empty, and a newly created event can be fetched by id.
- **Negative tests:** a bad token returns 401, and an unknown event id returns 404.
- **Schema check:** an event has the expected keys, with the right types.
- **Data-driven tests:** loan-amount boundary values with `@pytest.mark.parametrize`.

## Stack

Python 3.13 · pytest · requests · python-dotenv · pytest-html · GitHub Actions

## Run locally

1. Create a `.env` file (it is gitignored):
   ```
   BASE_URL=https://api.eventhub.rahulshettyacademy.com/api
   EVENTHUB_EMAIL=your-email
   EVENTHUB_PASSWORD=your-password
   ```
2. Install and run:
   ```
   pip install -r requirements.txt
   pytest -v --html=report.html --self-contained-html
   ```

## CI

Every push and pull request to `main` runs the suite in GitHub Actions. Credentials come from repository secrets, and the HTML report is uploaded as a build artifact.

Companion repo (Playwright + TypeScript UI and API tests): [Vishnu-Kota/playwright](https://github.com/Vishnu-Kota/playwright)
