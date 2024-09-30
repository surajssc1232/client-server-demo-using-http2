import httpx

def main():
    url = "http://localhost:8080/hello"
    headers = {"Accept": "text/plain"}

    with httpx.Client(http2=True) as client:
        response = client.get(url, headers=headers)
        if response.status_code == 200:
            print(f"Response: {response.text}")
        else:
            print(f"Request failed: {response.status_code}")

if __name__ == "__main__":
    main()