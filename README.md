# weather-reporter
This code provides the user with specific weather data including minimum and maximum temperatures, precise coordinates, a weather description 
as well as wind speeds. 

Users are provided with a clear interface to input a location. Weather data is then fetched from the OpenWeatherMap API and relevant 
information is extracted from the JSON response. The weather data is then presented to the user. It demonstrates the process of making an 
HTTP request, handling JSON data, and utilizing user input and API responses to provide useful information.

Importing Required Modules:
- The code imports the requests module, which allows making HTTP requests to the API.
- The config module (assumed to be a custom module) is imported to access the API key required for authentication.

User Input:
- The code prompts the user to enter a location.

Fetching Weather Data:
- The requests.get() method is used to send a GET request to the OpenWeatherMap API.
- The URL passed to the get() method is composed using an f-string, incorporating the user_input and the API key from config.api_key.

Extracting Weather Information:
- If the status code is not 404 (indicating a successful request), the code proceeds to extract relevant weather information from the JSON
  response.
- The extracted information includes the weather condition, temperature, longitude and latitude coordinates, weather description, "feels
  like" temperature, minimum temperature, maximum temperature, and wind speed.

The coordinates, weather condition, description, temperature (in Fahrenheit), "feels like" temperature, minimum and maximum temperatures, and wind speed are displayed.
