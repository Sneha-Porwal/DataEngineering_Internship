import requests

url = "https://restcountries.com/v3.1/name/india"
params = {
    "fields": "name,population,region"
}

response = requests.get(url, params=params)

print(response.url)   # shows full URL with parameters
print(response.json())
