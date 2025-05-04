import pytest
import requests


base_url = "https://yougile.com"
auth_token = 'NctHb3PgAukS2LH+8gKNqiNoCu+71YBlMN9o9RoxVhrA-imauVylYRhmQfQEyffx'


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
