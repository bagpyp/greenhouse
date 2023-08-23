import datetime
import time

from api.weather_api import WeatherAPI
from config.properties import properties, initialize
from models.greenhouse import Greenhouse
from models.sensor import Sensor

initialize()

# Greenhouse location (San Francisco for example)
LATITUDE = 37.7749
LONGITUDE = -122.4194


def main():
    # Initialize Greenhouse and Sensors
    greenhouse = Greenhouse(length=10, width=10, gps_coordinates=(LATITUDE, LONGITUDE))
    internal_sensor = Sensor(sensor_id=1, location=(5, 5), current_temp=24)
    greenhouse.add_sensor(internal_sensor)
    external_sensor = Sensor(sensor_id=2, location=(-1, -1), current_temp=26)

    # Simulation for the next 24 hours
    weather_api = WeatherAPI(properties["OPENWEATHERMAP_API_KEY"])
    hourly_forecast = weather_api.get_hourly_forecast(LATITUDE, LONGITUDE)

    simulation_hours = 24
    for hour in range(simulation_hours):
        # Simulated external temperature from the forecast
        external_temperature = hourly_forecast[hour]["temp"]
        external_sensor.update_temperature(external_temperature)

        # Calculate effect of external temperature on greenhouse
        delta = (
            external_temperature - internal_sensor.read_temperature()
        ) * 0.1  # This factor (0.1) can be adjusted

        # Incorporate effect of heating/cooling system (this can be made more sophisticated)
        if greenhouse.is_heating:
            delta += 2  # heating can increase temperature by 2°C
        if greenhouse.is_cooling:
            delta -= 2  # cooling can decrease temperature by 2°C

        # Update the greenhouse internal temperature based on calculated delta
        new_temperature = internal_sensor.read_temperature() + delta
        internal_sensor.update_temperature(new_temperature)

        # Print status for the current hour of simulation
        time_str = datetime.datetime.utcfromtimestamp(
            hourly_forecast[hour]["time"]
        ).strftime("%H:%M:%S")
        print(
            f"[{time_str}] External Temp: {external_temperature}°C, Greenhouse Temp: {internal_sensor.reading:.2f}°C"
        )

        # Control logic for heating and cooling (basic version)
        if internal_sensor.read_temperature() < 18:  # Desired lower limit is 18°C
            greenhouse.activate_heating()
        elif internal_sensor.read_temperature() > 26:  # Desired upper limit is 26°C
            greenhouse.activate_cooling()
        else:
            greenhouse.deactivate_systems()

        time.sleep(1)


if __name__ == "__main__":
    main()
