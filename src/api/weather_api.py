import requests


class WeatherAPI:
    BASE_URL = "https://api.openweathermap.org/data/2.5"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_current_temperature(self, lat, lon):
        response = requests.get(
            self.BASE_URL + "/weather",
            params={
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": "imperial",
            },
        )

        data = response.json()

        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch weather data. Error: {data.get('message', '')}"
            )
        return data["main"]["temp"]

    def get_hourly_forecast(self, lat, lon):
        response = requests.get(
            self.BASE_URL + "/forecast",
            params={
                "lat": lat,
                "lon": lon,
                "appid": self.api_key,
                "units": "imperial",
            },
        )

        data = response.json()

        if response.status_code != 200:
            raise Exception(
                f"Failed to fetch weather data. Error: {data.get('message', '')}"
            )

        tz_offset = data["city"]["timezone"]
        return [
            {"time": entry["dt"] + tz_offset, "temp": entry["main"]["temp"]}
            for entry in data["list"]
        ]
