import requests
from datetime import datetime

api_key = 'f882fae9cb250b24c74b00969692f710'
location = input("Enter the city name: ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = str(api_data['main']['humidity'])
wind_spd = str(api_data['wind']['speed'])
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
hum = str(api_data['main']['humidity'])
wind = str(api_data['wind']['speed'])

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")
print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

s = open('Weather-stats.txt','w')
s.write("Weather Stats for - {}  || {}".format(location.upper(), date_time) + '\n')
s.write("-------------------------------------------------------------\n")
s.write("Current temperature is: {:.2f} deg C".format(temp_city) + '\n')
s.write("Current weather desc  :")
s.write(weather_desc + '\n')
s.write("Current Humidity      :")
s.write(hmdt)
s.write('%\n')
s.write("Current wind speed    :")
s.write(wind_spd)
s.write('kmph\n')
s.close()


