import requests

# latitude = "43.6532" # Toronto
# latitude = "40.7128" # New York

# longitude = "79.3832" # Toronto
# longitude = "74.0060" # New York

# YOUR API KEY GOES HERE
api_key = 0


class City:
    def __init__(self, name, lat, lon, units="imperial"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        s = f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid={api_key}"

        try:
            response = requests.get(s)
        except:
            print("Something went wrong")

        self.response_json = response.json()

        self.temp = self.response_json["main"]["temp"]
        self.temp_max = self.response_json["main"]["temp_max"]
        self.temp_min = self.response_json["main"]["temp_min"]


    def temp_print(self):
        units_symbol = "F"
        if self.units == "metric":
            units_symbol = "C"
        if self.units == "standard":
            units_symbol = "K"

        print(f"In {self.name}, it is currently {self.temp}°{units_symbol}")
        print(f"Today's high: {self.temp_max}°{units_symbol}")
        print(f"Today's low: {self.temp_min}°{units_symbol}")

    
my_city = City("New York City", 40.7128, -74.0060, "imperial")
my_city.temp_print()

school_city = City("Toronto", 43.6532, -79.3832, "metric")
school_city.temp_print()