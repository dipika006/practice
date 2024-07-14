import requests


def try_add():
    abc = 45
    bcd = 34
    response = requests.get(f"http://127.0.0.1:8002/add?a={abc}&b={bcd}")
    a = response.text
    print(a)


def try_json():
    response = requests.get("http://127.0.0.1:8002/profile")
    a = response.json()
    print(a, type(a))
    print(a.get("firstname", "No firstname found!"))


def try_post_json():
    response = requests.post("http://127.0.0.1:8002/login", json={"username": "John"})
    a = response.json()
    print(a, type(a))


def try_post_form():
    response = requests.post("http://127.0.0.1:8002/login1", data={"username": "John"})
    a = response.json()
    print(a, type(a))


try_add()
try_json()
try_post_json()
try_post_form()
