import datetime
from pprint import pprint

from api.weather_api import WeatherAPI
from config.properties import properties, initialize
from models.greenhouse import Greenhouse
from models.sensor import Sensor
from view.plot import plot

# load api key from .env
initialize()

# greenhouse location (Portland for example)
LATITUDE = 45.5152
LONGITUDE = -122.6784
LOW, HIGH = 72, 75


def main():
    weather_api = WeatherAPI(properties["OPENWEATHERMAP_API_KEY"])
    hourly_forecast = weather_api.get_hourly_forecast(LATITUDE, LONGITUDE)
    current_temp = weather_api.get_current_temperature(LATITUDE, LONGITUDE)

    greenhouse = Greenhouse(length=10, width=10)
    internal_sensor = Sensor(location=(5, 5), current_temp=current_temp)
    external_sensor = Sensor(location=(-1, -1), current_temp=current_temp)  # external

    results = [
        {
            "timestamp": datetime.datetime.now().strftime(properties["TIME_FORMAT"]),
            "outside_temp": current_temp,
            "inside_temp": current_temp,
            "heating": False,
            "cooling": False,
        }
    ]
    for prediction in hourly_forecast:
        external_temperature = prediction["temp"]
        external_sensor.update_temperature(external_temperature)

        # rate of temperature change in the greenhouse
        delta = (
            external_temperature - internal_sensor.reading
        ) * 0.1  # this number is inversely proportional to how insulated the greenhouse is

        if greenhouse.is_heating:
            delta += 2  # heating can increase temperature by 2
        if greenhouse.is_cooling:
            delta -= 1.9  # cooling will only lower temperature by 1.9

        new_temperature = internal_sensor.reading + delta
        internal_sensor.update_temperature(new_temperature)

        time_str = datetime.datetime.utcfromtimestamp(prediction["time"]).strftime(
            properties["TIME_FORMAT"]
        )

        results.append(
            {
                "timestamp": time_str,
                "outside_temp": external_temperature,
                "inside_temp": internal_sensor.reading,
                "heating": greenhouse.is_heating,
                "cooling": greenhouse.is_cooling,
            }
        )

        # basic heating/cooling control logic
        if internal_sensor.reading < LOW:  # lower limit
            greenhouse.activate_heating()
        elif internal_sensor.reading > HIGH:  # upper limit
            greenhouse.activate_cooling()
        else:
            greenhouse.deactivate_systems()

    pprint(results)
    plot(results)


if __name__ == "__main__":
    main()
