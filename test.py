import requests
r = requests.session()
def login():
    url = "https://s.staging.mmears.com/id/login/pwd"
    data = {
        "email": "bonny@mmears.com",
        "password": "mmears2016",
        "code": "123456"
    }
    s = r.post(url=url, data=data)
    print(s.headers)
    print(s.json())
print(login())