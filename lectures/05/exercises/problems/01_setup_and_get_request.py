"""Problem 01 (merged): setup + first GET request.

Install dependencies (once):
    pip install requests fastapi uvicorn

Task:
1. Send a GET request to https://jsonplaceholder.typicode.com/todos/1
2. Print:
   - status code
   - Content-Type header
   - raw body (response.text)
   - parsed JSON (response.json())
3. Read and print: id, title, completed
4. Add error handling with raise_for_status()

Expected result:
- You can explain the difference between raw text and parsed JSON.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/todos/1"



def main() -> None:
    response = requests.get(URL)
    response.raise_for_status()
    
    print(f"Status : {response.status_code}")
    print(f"Header: {response.headers.get('Content-Type')}")
    
    print(f"Raw body {response.text}")
    print(f"parsed {response.json()}")
    data = response.json()
    
    print(f"ID: {data.get('id')}")
    print(f"Title: {data.get('title')}")
    
    print(f"Completed {data.get('completed')}")


    # TODO: implement request flow here.
    # Suggested variables: response, data
    pass


if __name__ == "__main__":
    main()
