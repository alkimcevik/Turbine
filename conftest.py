import pytest
import requests
from requests.auth import HTTPBasicAuth
import os
import time

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Check if the test has finished running
    if rep.when == "call":
        session_id = getattr(item, 'session_id', None)
        if session_id:
            print(f"BrowserStack session_id: {session_id}")  # Print the session_id for debugging
            url = f"https://api.browserstack.com/automate/sessions/{session_id}.json"
            auth = HTTPBasicAuth(os.getenv('BROWSERSTACK_USERNAME'), os.getenv('BROWSERSTACK_ACCESS_KEY'))
            headers = {
                "Content-Type": "application/json"
            }

            # Determine the status and reason based on the test outcome
            if rep.failed:
                status = "failed"
                reason = "Test failed"
            else:
                status = "passed"
                reason = "Test passed"

            data = {
                "status": status,
                "reason": reason,
                "name": item.name
            }

            try:
                response = requests.put(url, auth=auth, headers=headers, json=data, timeout=10)
                print("Browserstack status code:", response.status_code)
                # print("Response Text:", response.text)
            except requests.exceptions.RequestException as e:
                print(f"Failed to send request to BrowserStack: {e}")

@pytest.fixture(autouse=True)
def pause_between_tests():
    time.sleep(3)  # Pause before each test