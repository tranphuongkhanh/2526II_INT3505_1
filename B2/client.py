import requests

base = "http://127.0.0.1:5000/books"

book = {
    "id": 1,
    "title": "Clean Code",
    "author": "Robert Martin",
    "status": "available"
}

print(requests.post(base, json=book).json())
print(requests.get(base).json())

update = {
    "id": 1,
    "title": "Clean Code 2",
    "author": "Robert Martin",
    "status": "available"
}

print(requests.put(base+"/1", json=update).json())

print(requests.patch(base+"/1", json={"id":1,"status":"borrowed"}).json())

print(requests.delete(base+"/1", json={"id":1}).json())