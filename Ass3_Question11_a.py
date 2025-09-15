import requests

def get_api_data():
    """
    Makes a GET request to a public API and prints the response.
    """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    print(f"Making a GET request to: {url}")
    try:
        response = requests.get(url)
        # Raise an HTTPError for bad responses (4xx or 5xx)
        response.raise_for_status()
        data = response.json()
        print("\nAPI Response:")
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Run bit

get_api_data()
