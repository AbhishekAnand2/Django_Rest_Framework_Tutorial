import requests


# Endpoints are the places where we have to made a request to.
# endpoint = "https://httpbin.org/"
endpoint = "http://localhost:9000/api/" # or http://127.0.0.1:9000/

get_response = requests.get(endpoint, params={"abc":123}, json={"query": "Hello World!"}) #HTTP Request
print(get_response.text) # Print raw text response
print(get_response.status_code) # Status code returned
print(get_response.json())


# HTTP Request -> HTML (These are the requests that humans made using browser)
# REST API HTTP Request -> JSON (These are the Http Request which an API can make)
# JavaScript Object Notation -> Python Dict
# print(get_response.json())
# print(get_response.status_code) 