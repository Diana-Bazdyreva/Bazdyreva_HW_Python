import pytest
import requests


base_url = "https://yougile.com"
auth_token = 'NctHb3PgAukS2LH+8gKNqiNoCu+71YBlMN9o9RoxVhrA-imauVylYRhmQfQEyffx'
project_id = '4f66404e-400c-4ef0-a549-e403ed00b0cd'


@pytest.fixture(scope="module")
def auth_headers():
    return {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }


def test_get_company_by_id(auth_headers):
    response = requests.get(
        f"{base_url}/api-v2/projects/{project_id}", headers=auth_headers)

    assert response.status_code == 200
