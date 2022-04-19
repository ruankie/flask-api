import requests
import pytest

BASE = 'http://127.0.0.1:5000/'

def test_hello_world():
    response = requests.get(BASE + 'helloworld')
    #print(response.json())
    assert response.json() == {'Message': 'Hello World'}

def test_greet_name():
    response = requests.get(BASE + '/hello/Billy')
    #print(response.json())
    assert response.json() == {'Message': 'Hello Billy!'}
