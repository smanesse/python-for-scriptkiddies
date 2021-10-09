import requests

url = "https://google.com/"
my_proxies = {"http": "http://127.0.0.1:8080",
                    "https": "http://127.0.0.1:8080"}

response = requests.get(url, proxies=my_proxies, verify=False)
print(response.text)

