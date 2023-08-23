import requests


class WeatherAPI:
    BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather_data(self, lat, lon, exclude="minutely"):
        """
        Fetch the weather data for given latitude and longitude.

        :param lat: Latitude of the location.
        :param lon: Longitude of the location.
        :param exclude: Data to be excluded. By default, we exclude minutely data.
        :return: JSON response of the weather data.
        """
        params = {
            "lat": lat,
            "lon": lon,
            "exclude": exclude,
            "appid": self.api_key,
            "units": "metric",  # Celsius
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch weather data. Error: {data.get('message', '')}"
            )

        return data

    def get_current_temperature(self, lat, lon):
        """
        Get the current temperature for the given latitude and longitude.

        :param lat: Latitude of the location.
        :param lon: Longitude of the location.
        :return: Current temperature in Celsius.
        """
        data = self.get_weather_data(lat, lon)
        return data["current"]["temp"]

    def get_hourly_forecast(self, lat, lon):
        """
        Get the hourly temperature forecast for the given latitude and longitude.

        :param lat: Latitude of the location.
        :param lon: Longitude of the location.
        :return: List of hourly temperature data for the next 48 hours.
        """
        data = self.get_weather_data(lat, lon)
        return [
            {"time": entry["dt"], "temp": entry["temp"]} for entry in data["hourly"]
        ]
