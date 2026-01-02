import requests

url = "https://restcountries.com/v3.1/name/india"
params = {
    "fields": "name,population,region"
}

response = requests.get(url, params=params)

print(response.url)   
print(response.json())
