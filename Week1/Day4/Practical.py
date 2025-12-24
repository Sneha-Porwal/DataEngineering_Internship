import requests

username = "Sneha-Porwal"
repo_name = "BloodManagement"

url = f"https://api.github.com/repos/{username}/{repo_name}/languages"

response = requests.get(url)

if response.status_code == 200:
    languages = response.json()
    for lang, bytes in languages.items():
        print(lang, ":", bytes)
else:
    print("Error:", response.status_code)
