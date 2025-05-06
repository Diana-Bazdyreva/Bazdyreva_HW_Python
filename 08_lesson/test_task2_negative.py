import pytest
import requests
from config import base_url, auth_token, project_id

# проверка с невалидным id

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

    assert response.status_code == 404
