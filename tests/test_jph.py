import pytest

TEST_DATA = [
    {"title": "my_title", "body": "my_body", "userId": 1}
    {"title": "my_title2", "body": "my_body2", "userId": 2}
]

@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_post(create_post_endpoint):
    create_post_endpoint.create_new_post(payload-data)
    create_post_endpoint.check_response_title_is_correct(payload['title'])


