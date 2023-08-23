import random


class Sensor:
    def __init__(self, sensor_id, location, current_temp=25, fluctuation=0.5):
        self.sensor_id = sensor_id
        self.location = location
        self.current_temp = current_temp
        self.fluctuation = fluctuation

    def read_temperature(self):
        self.current_temp = self.current_temp + random.uniform(
            -self.fluctuation, self.fluctuation
        )
        return self.current_temp

    def update_temperature(self, temperature):
        self.current_temp = temperature

    def __repr__(self):
        return f"Sensor(id={self.sensor_id}, location={self.location}, current_temp={self.current_temp:.2f})"
