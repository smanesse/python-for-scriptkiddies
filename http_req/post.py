import requests

url = "https://jsonplaceholder.typicode.com/posts"

# json body can be a dictionary
body = {"title":"asdf","body":"post_body","userId":1}

# make the POST
response = requests.post(url, data=body)

print(response.text)
