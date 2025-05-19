import requests
import pytest
import time


@pytest.fixture(scope='session')
def hello():
    print("hello")
    yield
    print("bye")

@pytest.mark.smoke
def test_get_one_post(new_post_id):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response == {}

@pytest.mark.smoke
def test_get_all_posts(hello):
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) + 100

@pytest.mark.regression    
def test_post_a_post():
    body = {
        "title": "sdsdsdsd",
        "body": "sddfxsdsd",
        "userId": 1 
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    assert response.json()['id'] == 101
    assert response.status_code == 201, 'Status code is incorrect'

def test_add_post(hello):
    print ('test')
    body = {
        "title": "testing_title",
        "body": "testing_body",
        "userId": 1
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=body, headers=headers)
    assert 1 == 1



@pytest.mark.regression         
def test_one():
    assert 1 == 1

@pytest.mark.parametrize("logins", ["", "   ", "&*&*)", "прв"])
def test_two(logins):
    print(logins)
    assert 2 == 2
    
def test_three():
    assert 3 == 3









