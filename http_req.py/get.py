# import requests module
import requests

url = "https://api.isevenapi.xyz/api/iseven/5"

# basic GET
response = requests.get(url)

# status code (200 = OK, 404 = not found, etc)
print(response.status_code)

# response body as a string
print(response.text)

# response body as a dictionary (if the response body is JSON)\
json_body = response.json()
print(json_body)

# get an item from the json
item = json_body["iseven"]
print(item)
