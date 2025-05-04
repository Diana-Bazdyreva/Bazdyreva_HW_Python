import pytest
import requests

# проверка с невалидным id

base_url = "https://yougile.com"
auth_token = 'NctHb3PgAukS2LH+8gKNqiNoCu+71YBlMN9o9RoxVhrA-imauVylYRhmQfQEyffx'
project_id = '4f66404e-400c-4ef0-a549-e403ed00b0'


@pytest.mark.parametrize("new_title", [
    "123456"
])
def test_project_update(new_title):
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'title': new_title
    }

    full_url = f"{base_url}/api-v2/projects/{project_id}"

    response = requests.put(full_url, json=payload, headers=headers)

    assert response.status_code == 201
