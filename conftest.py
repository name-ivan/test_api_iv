import pytest
from test_api_iv.endpoints.create_post import CreatePost

@pytest.fixture()
def create_post_endpoint():
    return CreatePost()