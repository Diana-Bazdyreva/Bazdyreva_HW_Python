import pytest
import requests
from config import base_url, auth_token, invalid_aut_token


@pytest.fixture(scope="module")
def auth_headers():
    return {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }


def test_get_company_by_id2(auth_headers):
    response = requests.get(
        f"{base_url}/api-v2/projects/{
            invalid_aut_token}", headers=auth_headers)

    assert response.status_code == 404
