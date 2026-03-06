import requests

base = "http://127.0.0.1:5000"

book = {
    "id": 1,
    "title": "Clean Code",
    "author": "Robert Martin",
    "status": "available"
}

print(requests.post(base+"/add_book", json=book).json())
print(requests.get(base+"/get_books").json())

update = {
    "id": 1,
    "title": "Clean Code 2",
    "author": "Robert Martin",
    "status": "available"
}

print(requests.put(base+"/update_book", json=update).json())

print(requests.patch(base+"/patch_book", json={"id":1,"status":"borrowed"}).json())

print(requests.delete(base+"/delete_book", json={"id":1}).json())