import requests
import datetime as dt


MY_LAT = 30.201920,
MY_LONG = 71.453056,

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}

response = requests.get(url= "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
timing_of_multan_city = (sunrise, sunset)
print(timing_of_multan_city)

now = dt.datetime.now()
hour = now.hour
print(hour)
