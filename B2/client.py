import requests

base = "http://127.0.0.1:5000"

login = {
    "username":"admin",
    "password":"123"
}

r = requests.post(base+"/login", json=login)

token = r.json()["token"]

print("TOKEN:", token)

headers = {
    "Authorization": "Bearer " + token
}

book = {
    "id": 1,
    "title": "Clean Code",
    "author": "Robert Martin",
    "status": "available"
}

print(requests.post(base+"/books", json=book, headers=headers).json())

r = requests.get(base+"/books", headers=headers)
print("CACHE HEADER:", r.headers.get("Cache-Control"))
print(r.json())

update = {
    "id": 1,
    "title": "Clean Code 2",
    "author": "Robert Martin",
    "status": "available"
}

print(requests.put(base+"/books/1", json=update, headers=headers).json())

print(requests.patch(base+"/books/1", json={"id":1,"status":"borrowed"}, headers=headers).json())

print(requests.delete(base+"/books/1", json={"id":1}, headers=headers).json())
