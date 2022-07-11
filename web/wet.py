
import requests, json
from datetime import date, datetime
import time
api_key = "729d99bd52f8edc51126144a21673993"


base_url = "http://api.openweathermap.org/data/2.5/weather?"


city_name = 'darvin'

#complete_url = base_url + "appid=" + api_key + "&q=" + city_name

#print(complete_url)
complete_url = 'http://0.0.0.0:8000/rep.json'

response = requests.get(complete_url)
x = response.json()


        

#print(time.strftime('%A',time.localtime(1657281600)))

print(x['weather'][0]['description'])

import subprocess
subprocess.Popen(["python3","error.py"])