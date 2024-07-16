import requests
from time import sleep

def download_content(urls):
    contents = []
    for url in urls:
        retries = 3
        while retries > 0:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise HTTPError for bad responses
                contents.append(response.content)
                break
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
                retries -= 1
                sleep(1)  # Wait before retrying
        else:
            contents.append(None)
    return contents

def download_content_operations():
    urls = input("Enter URLs (comma-separated): ").split(',')
    contents = download_content(urls)
    for i, content in enumerate(contents):
        print(f"Content of URL {i+1}: {'Downloaded' if content else 'Failed to download'}")

download_content_operations()
