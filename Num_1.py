from pprint import pprint

import requests
url = 'https://api.openweathermap.org/data/2.5/weather'
appid = '97eeffcacfb54ec4fcfd2f17b51199d0'
params = {'q':'Krasnodar, Ru',
           'appid':appid}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

response = requests.get(url, headers = headers, params = params)
j_date = response.json()

#pprint(j_date)

print(f"В городе {j_date['name']} температура воздуха {j_date['main']['temp'] - 273.15} градусов")
