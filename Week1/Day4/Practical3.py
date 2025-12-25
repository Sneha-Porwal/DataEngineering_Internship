'''Rate limiting is used by APIs to control how many requests a client can make within a given time period, helping prevent server overloading.

How to handle it in Python:

1.Check the response status code after making a request
2.If the API returns 429 Too Many Requests, it means you sent too many requests
3.Pause your program for some time using time.sleep()
4.Try the request again after waiting
5.Use authentication (API key/token) to get higher limits
'''

import requests
import time

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)

if response.status_code == 429:
    print("Too many requests. Waiting...")
    time.sleep(60)   # wait for 1 minute
    response = requests.get(url)
else:
    print(response.json())

