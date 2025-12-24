import requests

url = "https://restcountries.com/v3.1/name/india"

params = {
    "fields": "name,population,region"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
