import requests

base = "http://127.0.0.1:5000/books"

headers = {
    "API-Key": "123456"
}

book = {
    "id": 1,
    "title": "Clean Code",
    "author": "Robert Martin",
    "status": "available"
}

print(requests.post(base, json=book, headers=headers).json())

r = requests.get(base, headers=headers)
print("CACHE HEADER:", r.headers.get("Cache-Control"))
print(r.json())

update = {
    "id": 1,
    "title": "Clean Code 2",
    "author": "Robert Martin",
    "status": "available"
}

print(requests.put(base+"/1", json=update, headers=headers).json())

print(requests.patch(base+"/1", json={"id":1,"status":"borrowed"}, headers=headers).json())

print(requests.delete(base+"/1", json={"id":1}, headers=headers).json())
