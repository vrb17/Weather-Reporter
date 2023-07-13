import requests
import config

user_input = input("Enter location: ")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={config.api_key}")

# print(weather_data.status_code)----- if 200 is printed out then request was successful
degree = u'\N{DEGREE SIGN}'

if weather_data.json()['cod'] == '404':
    print("No location found")
else: 
    weather = weather_data.json()['weather'][0]['main']
    temperature = weather_data.json()['main']['temp']
    longitude = weather_data.json()['coord']['lon']
    latitude = weather_data.json()['coord']['lat']
    description = weather_data.json()['weather'][0]['description']
    feel_like = weather_data.json()['main']['feels_like']
    min = weather_data.json()['main']['temp_min']
    max = weather_data.json()['main']['temp_max']
    winds = weather_data.json()['wind']['speed']

    print('------------------------------------------------------')
    print(f"Weather data in {user_input}")
    print(f"Coordinates: {longitude}, {latitude}")
    print(f"Description: {weather}, {description}")
    print(f"Temperature: {temperature}{degree}F")
    print(f"Feels like: {feel_like}{degree}F, Min: {min}{degree}F, Max: {max}{degree}F")
    print(f"Wind speed: {winds}mph")

    
    

