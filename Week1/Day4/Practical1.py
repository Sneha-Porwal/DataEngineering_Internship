import requests

url = "https://api.github.com/users/Sneha-Porwal/repos"

response = requests.get(url)

if response.status_code == 200:
    repos = response.json()   #convert json to python object
    for repo in repos:
        print("Repository:", repo["name"])
else:
    print("Error:", response.status_code)