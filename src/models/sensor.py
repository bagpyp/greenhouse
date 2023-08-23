import random


class Sensor:
    def __init__(self, sensor_id, location, avg_temp, fluctuation):
        self.sensor_id = sensor_id
        self.location = location
        self.avg_temp = avg_temp
        self.fluctuation = fluctuation
        self.current_temp = avg_temp

    def read_temperature(self):
        self.current_temp = self.avg_temp + random.uniform(
            -self.fluctuation, self.fluctuation
        )
        return self.current_temp

    def adjust_temperature(self, delta):
        self.avg_temp += delta

    def __repr__(self):
        return f"Sensor(id={self.sensor_id}, location={self.location}, avg_temp={self.current_temp:.2f})"
