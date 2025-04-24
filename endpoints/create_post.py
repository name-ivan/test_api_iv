import requests
import allure
from test_api_iv.endpoints.endpoint import Endpoint

class CreatePost(Endpoint):
    
    @allure.step("Crete new post")
    def create_new_post(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json

    @allure.step("Check the title is the same as sent")
    def check_response_title_is_correct(self, title):
        assert self.response_json['title'] == title

    @allure.step("Check the received eroor code is 400 when the data is negative")
    def check_bad_request(self):
        assert self.response.status_code == 400
        
