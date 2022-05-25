import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)

# TODO This line will handle all types of exception by itself, We don't need to handle each exception manually
response.raise_for_status()
data = response.json()
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

iss_position = (latitude, longitude)
print(iss_position)
