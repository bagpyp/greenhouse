import random


class Sensor:
    def __init__(self, location, current_temp=71, fluctuation=0.5):
        self.location = location
        self.current_temp = current_temp
        self.fluctuation = fluctuation

    @property
    def reading(self):
        self.current_temp = self.current_temp + random.uniform(
            -self.fluctuation, self.fluctuation
        )
        return self.current_temp

    def update_temperature(self, temperature):
        self.current_temp = temperature

    def __repr__(self):
        return f"Sensor(location={self.location}, current_temp={self.current_temp:.2f})"
