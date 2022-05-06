import requests
import smtplib

API_KEY = "INSERT API KEY HERE"
LATITUDE = 40.379589 #INSERT YOUR LAT HERE
LONGITUDE = -3.706790 #INSERT LONG HERE
EMAIL= "INSERT EMAIL HERE" #INSERT EMAIL HERE
PASSWORD = "INSERT PASSWORD HERE" #INSERT EMAIL HERE
TO_EMAIL = "INSERT WHO YOU'RE SENDING TO HERE" #INSERT WHO YOU'RE EMAILING TO HERE

PARAMETERS = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY,
}

response = requests.get(url='http://api.openweathermap.org/data/2.5/onecall', params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()

twelve_hours = weather_data['hourly'][:12]

will_rain = False

for weather in twelve_hours:
    id_list = weather['weather'][0]['id']
    if int(id_list) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP('smtp.google.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=TO_EMAIL,
                            msg="Subject:It's going to rain\n\nTake an umbrella!")



