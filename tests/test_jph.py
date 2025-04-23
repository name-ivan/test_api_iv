import allure


def test_post_a_post(create_post_endpoint):
    with allure.step("prepare test data"):
        payload = {
            "title": "my_title",
            "body": "my_body",
            "userId": 1
        }
        headers = {"application_ttpe": "json"}


    create_post_endpoint.create_new_post(payload, headers)
    response = create_post_endpoint.response_json
    create_post_endpoint.check_response_title_is_correct(payload['title'])
    
        