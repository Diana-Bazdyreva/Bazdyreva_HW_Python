import pytest
import requests


base_url = "https://yougile.com"
auth_token = 'NctHb3PgAukS2LH+8gKNqiNoCu+71YBlMN9o9RoxVhrA-imauVylYRhmQfQEyffx'


@pytest.mark.parametrize("title", ["Evgenia"])
def test_project_creation(title):
    headers = {
        'Authorization': f'Token {auth_token}',
        'Content-Type': 'application/json'
    }
    payload = {'title': title}
    response = requests.post(
        base_url + '/api-v2/projects',
        json=payload,
        headers=headers
    )

    assert response.status_code == 201
