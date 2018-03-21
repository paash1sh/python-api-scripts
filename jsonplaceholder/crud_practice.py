# practicing REST API calls with jsonplaceholder
# jsonplaceholder is a free fake API for testing
# https://jsonplaceholder.typicode.com

import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"

# GET - fetch all posts
print("--- GET all posts ---")
response = requests.get(f"{BASE_URL}/posts")
print("status code:", response.status_code)
posts = response.json()
print("total posts:", len(posts))
print("first post:", posts[0]["title"])
print()

# GET - fetch single post
print("--- GET single post ---")
response = requests.get(f"{BASE_URL}/posts/1")
print("status code:", response.status_code)
post = response.json()
print("title:", post["title"])
print("body:", post["body"][:50], "...")
print()

# POST - create new post
print("--- POST new post ---")
new_post = {
    "title": "my test post",
    "body": "this is the body of my test post",
    "userId": 1
}
response = requests.post(f"{BASE_URL}/posts", json=new_post)
print("status code:", response.status_code)
created = response.json()
print("created post id:", created["id"])
print()

# PUT - update post
print("--- PUT update post ---")
updated_post = {
    "id": 1,
    "title": "updated title",
    "body": "updated body",
    "userId": 1
}
response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)
print("status code:", response.status_code)
print("updated title:", response.json()["title"])
print()

# DELETE - delete post
print("--- DELETE post ---")
response = requests.delete(f"{BASE_URL}/posts/1")
print("status code:", response.status_code)
if response.status_code == 200:
    print("post deleted successfully")
