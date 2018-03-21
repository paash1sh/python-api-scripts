# practicing with users and comments endpoints
# also trying to understand response structure better

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# get all users
print("=== USERS ===")
response = requests.get(f"{BASE_URL}/users")
users = response.json()
print(f"found {len(users)} users")
for user in users[:3]:
    print(f"  - {user['name']} ({user['email']})")
print()

# get comments for a post
print("=== COMMENTS for post 1 ===")
response = requests.get(f"{BASE_URL}/posts/1/comments")
comments = response.json()
print(f"found {len(comments)} comments")
for comment in comments:
    print(f"  - {comment['name']}: {comment['body'][:40]}...")
print()

# get todos for a user
print("=== TODOS for user 1 ===")
response = requests.get(f"{BASE_URL}/users/1/todos")
todos = response.json()
completed = [t for t in todos if t["completed"]]
pending = [t for t in todos if not t["completed"]]
print(f"total: {len(todos)}, completed: {len(completed)}, pending: {len(pending)}")
print()

# checking response headers
print("=== RESPONSE HEADERS ===")
response = requests.get(f"{BASE_URL}/posts/1")
print("content-type:", response.headers.get("Content-Type"))
print("response time:", response.elapsed.total_seconds(), "seconds")
