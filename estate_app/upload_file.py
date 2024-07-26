# import requests

# # Define the URL and the file path
# url = 'https://localhost:8000/api/method/upload_file'
# file_path = '/home/neha/Downloads/pic.jpg'

# # API key and secret
# api_key = 'c70b9b776f8b2f2'
# api_secret = 'e088ba0a5ac1734'

# # Prepare the headers
# headers = {
#     'Authorization': f'token {api_key}:{api_secret}'
# }

# # Prepare the files payload
# files = {
#     'file': open(file_path, 'rb'),
#     'is_private': (None, '0')
# }

# # Make the POST request
# response = requests.post(url, headers=headers, files=files,verify=False)

# # Print the response
# print(response.json())

# import ssl
# import requests

# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# url = 'https://localhost:8000/api/method/upload_file'
# file_path = '/home/neha/Downloads/pic.jpg'
# api_key = 'c70b9b776f8b2f2'
# api_secret = 'e088ba0a5ac1734'

# headers = {
#     'Authorization': f'token {api_key}:{api_secret}'
# }

# files = {
#     'file': open(file_path, 'rb'),
#     'is_private': (None, '0')
# }

# response = requests.post(url, headers=headers, files=files, verify=ssl_context)
# print(response.json())


import requests
from requests.auth import HTTPBasicAuth

# Your ERPNext/Frappe instance URL
base_url = "http://localhost:8000"

# Your API key and secret
api_key = "c70b9b776f8b2f2"
api_secret = "e088ba0a5ac1734"

# File to upload
# file_path = "/home/neha/projects/test_bench/frappe-bench/apps/estate_app/estate_app/api/upload.txt"
file_path="/home/neha/Pictures/Screenshots/Screenshot from 2024-05-24 12-16-15.png"

# API endpoint to upload file
upload_url = f"{base_url}/api/method/upload_file"

# Read the file content
with open(file_path, 'rb') as file:
    # Prepare the request
    files = {
        'file': file,
        'is_private': (None, '1'),  # Set to '0' if the file should be public
    }
    
    # Send the request with SSL verification disabled (for testing purposes)
    try:
        response = requests.post(upload_url, files=files, auth=HTTPBasicAuth(api_key, api_secret), verify=False)
        
        # Check the response
        if response.status_code == 200:
            print("File uploaded successfully")
            print("Response:", response.json())
        else:
            print("Failed to upload file")
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)