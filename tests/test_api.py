import pytest
import requests
from requests.exceptions import Timeout
from jsonschema import validate, ValidationError
from unittest.mock import patch

# Fixture for base URL and headers setup
@pytest.fixture(scope="module")
def base_url_headers():
    return {
        'base_url': 'https://jsonplaceholder.typicode.com',
        'headers': {'Content-type': 'application/json; charset=UTF-8'}
    }

# Fixture for authentication token (not required for JSONPlaceholder but included for demonstration)
# @pytest.fixture(scope="module")
# def auth_token():
#     return {'Authorization': 'Bearer yourtokenhere'}

# Fixture for post data
@pytest.fixture
def post_payload():
    return {'title': 'create', 'body': 'body', 'userId': 1}

# Test schema
post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["id", "userId", "title", "body"]
}

# Test case for GET
def test_get_post(base_url_headers):
    """Test to fetch a single post and validate its structure."""
    url = f"{base_url_headers['base_url']}/posts/1"
    response = requests.get(url, headers=base_url_headers['headers'])
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=post_schema)
    except ValidationError as e:
        pytest.fail(f"Response validation failed: {e}")

# Test case for POST
def test_create_post(base_url_headers, post_payload):
    """Test to create a new post and verify the response code and data."""
    url = f"{base_url_headers['base_url']}/posts"
    response = requests.post(url, headers=base_url_headers['headers'], json=post_payload)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["title"] == post_payload["title"]
    assert response_json["body"] == post_payload["body"]
    assert response_json["userId"] == post_payload["userId"]
    try:
        validate(instance=response_json, schema=post_schema)
    except ValidationError as e:
        pytest.fail(f"Response validation failed: {e}")

# Test case for PUT
def test_update_post(base_url_headers, post_payload):
    """Test to update a post and check for proper updates."""
    updated_payload = post_payload.copy()
    updated_payload['title'] = 'updated title'
    url = f"{base_url_headers['base_url']}/posts/1"
    response = requests.put(url, headers=base_url_headers['headers'], json=updated_payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["title"] == "updated title"

# Test case for DELETE
def test_delete_post(base_url_headers):
    """Test to delete a post and confirm its removal."""
    url = f"{base_url_headers['base_url']}/posts/1"
    response = requests.delete(url, headers=base_url_headers['headers'])
    assert response.status_code == 200  # Note: Placeholder API doesn't truly delete, but returns 200