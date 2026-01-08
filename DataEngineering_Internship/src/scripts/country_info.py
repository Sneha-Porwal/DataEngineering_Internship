from src.common.api_client import get_json

URL = "https://restcountries.com/v3.1/name/india"
PARAMS = {"fields": "name,population,region"}

if __name__ == "__main__":
    print(get_json(URL, PARAMS))
