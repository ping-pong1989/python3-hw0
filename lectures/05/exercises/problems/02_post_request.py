"""Problem 02: POST request to JSONPlaceholder.

Task:
1. Send POST to https://jsonplaceholder.typicode.com/posts
2. Send JSON payload with fields: title, body, userId
3. Print:
   - status code
   - raw body
   - parsed JSON
4. Confirm response includes your data + id

Note: JSONPlaceholder simulates writes; data is not truly persisted.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/posts"

payload = {'title': 'smth', 'body': "send post request", "userid": 1}

def main() -> None:
    response = requests.post(
        URL,
        json = payload,
        
)
    print(f"Status: {response.status_code}")
    print(f"Raw body: {response.text}")
    data = response.json()
    print(f"parsed JSON: {response.json()}")
    # TODO: create payload dict
    # TODO: send POST request with json=payload
    # TODO: print response details
 
    if "id" in data:
        print("Good")

if __name__ == "__main__":
    main()
