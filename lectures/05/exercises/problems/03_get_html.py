"""Problem 03: GET request for HTML content.

Task:
1. Send GET to https://example.com
2. Print:
   - status code
   - Content-Type header
   - HTML body (response.text)
3. Verify content type contains text/html
4. Add raise_for_status()
"""

import requests

URL = "https://example.com"


def main() -> None:
    response =requests.get(URL)
    response.raise_for_status()
    print(f"Status: {response.status_code}" )
    print(f"Header: {response.headers.get('smth')}")
    print(f"Content: {content_type}")
    
    # TODO: implement GET request and print HTML response
   

if __name__ == "__main__":
    main()
