class Greenhouse:
    def __init__(self, length, width, location):
        self.length = length
        self.width = width
        self.location = location
        self.sensors = []
        self.heating_status = False
        self.cooling_status = False

    def add_sensor(self, sensor):
        """Adds a sensor to the greenhouse."""
        self.sensors.append(sensor)

    def activate_heating(self, delta):
        """Activates the heating system and adjusts all sensor temperatures."""
        self.heating_status = True
        self.cooling_status = False
        for sensor in self.sensors:
            sensor.adjust_temperature(delta)

    def activate_cooling(self, delta):
        """Activates the cooling system and adjusts all sensor temperatures."""
        self.heating_status = False
        self.cooling_status = True
        for sensor in self.sensors:
            sensor.adjust_temperature(-delta)  # Negative value for cooling

    def deactivate_systems(self):
        """Deactivates both heating and cooling systems."""
        self.heating_status = False
        self.cooling_status = False

    def __repr__(self):
        return f"Greenhouse at {self.location} of size {self.length}x{self.width} with {len(self.sensors)} sensors."
