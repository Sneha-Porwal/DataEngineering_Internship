

import requests

username = "Sneha-Porwal"
url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        print("Repository:", repo["name"])
else:
    print("Error:", response.status_code)