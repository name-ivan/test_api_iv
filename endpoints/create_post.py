import requests
import allure

class CreatePost():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = None
    
    @allure.step("Crete new post")
    def create_new_post(self, payload, headers):
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json

    @allure.step("Check the title is the same as sent")
    def check_response_title_is_correct(self, title):
        assert self.response_json['title'] == title