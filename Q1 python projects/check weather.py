import requests
import json

city = input("Enter the name of the city \n")

url = f"https://api.weatherapi.com/v1/current.json?key=e58bdfe3a6ea488e92251023251403&q={city}"

r = requests.get(url)

wdic = r.json()

print(wdic["current"]["temp_c"])
