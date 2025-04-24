import requests
import allure
from test_api_iv.endpoints.endpoint import Endpoint

class CreatePost(Endpoint):
    
    @allure.step("Update a post")
    def make_changes_in_post(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f"{self.url}/{post_id}"
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json
        return self.response


