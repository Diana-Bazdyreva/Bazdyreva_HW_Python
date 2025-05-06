import pytest
import requests
from config import base_url, auth_token


@pytest.mark.parametrize("title, id", [
    ("222", '4f66404e-400c-4ef0-a549-e403ed00b0cd'),
])
def test_project_update1(title, id):
    headers = {
        'Authorization': f'Token {auth_token}',
        'Content-Type': 'application/json'
    }
    payload = {'title': title}

    full_url = f"{base_url}/api-v2/projects/{id}"

    response = requests.put(full_url, json=payload, headers=headers)

    assert response.status_code == 200
