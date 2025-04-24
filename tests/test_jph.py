import pytest

TEST_DATA = [
    {"title": "my_title", "body": "my_body", "userId": 1}
    {"title": "my_title2", "body": "my_body2", "userId": 2}
]

NEGATIVE_DATA = [
    {"title": ["my_title"], "body": "my_body", "userId": 1}
    {"title": {"my_title2": ''}, "body": "my_body2", "userId": 2}
]

@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_post(create_post_endpoint):
    create_post_endpoint.create_new_post(payload-data)
    create_post_endpoint.check_response_title_is_correct(payload['title'])


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_post_with_negative_data(start, data):
    create_post_endpoint.create_new_post(data)
    # create_post_endpoint.check_bad_request()
    create_post_endpoint.check_response_title_is_correct(payload['title'])



    
# @allure.feature('Updating a post')
# @allure.story('PUT')
# def test_put_a_post(post_id):
#     with allure.step('Prepare test data'):
#         payload = {
#             "title": "My tileUPD",
#             "body": "my bodyUPD",
#             "userId": 2
#         }

#         headers = {'Content-type': 'application/json'}
#     with allure.step('Send PUT request to update the post'):
#         response = requests.put(
#             url=f'https://jsonplaceholder.typicode.com/posts/{post_id}',
#             json=payload,
#             headers=headers
#         ).json()
#     with allure.step('Check that title is the same as sent'):
#         assert response['title'] == 'My tileUPD'    