import requests
import sys

SERVER_URL = 'http://localhost:8888'


def upload_file(file_path):
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(f'{SERVER_URL}/upload', files=files)
        if response.ok:
            print("File uploaded successfully")
        else:
            print(f"Upload failed with status code {response.status_code}")
            print(response.text)


def list_files():
    response = requests.get(f'{SERVER_URL}/list')
    if response.status_code == 200:
        files = response.json().get('files', [])
        print("Files on server:")
        for file in files:
            print(file['name'])
    else:
        print("Failed to fetch files")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("python screwdriver.py upload /path/to/file.mp3")
        print("python screwdriver.py list")
        sys.exit(1)

    if sys.argv[1] == "upload":
        if len(sys.argv) != 3:
            print("Usage: python screwdriver.py upload /path/to/file.mp3")
            sys.exit(1)

        file_path = sys.argv[2]
        upload_file(file_path)

    elif sys.argv[1] == "list":
        list_files()
