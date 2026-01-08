import time
import requests

URL = "https://restcountries.com/v3.1/all"

response = requests.get(URL)

if response.status_code == 429:
    print("Rate limit hit. Retrying...")
    time.sleep(60)
    response = requests.get(URL)

print(response.json())
