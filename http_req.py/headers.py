import requests

url = "https://dummy.restapiexample.com/api/v1/create"
my_data =   {"name":"test", "salary":"123", "age":"23"}
my_cookies = {"PHPSESSID": "059BE6C6A783CD784"}
my_headers = {"User-Agent":"python stuff"}
response = requests.post(url, data=my_data, cookies=my_cookies, headers=my_headers)
print(response.text)
