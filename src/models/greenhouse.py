class Greenhouse:
    def __init__(self, length, width, gps_coordinates):
        self.length = length
        self.width = width
        self.gps_coordinates = gps_coordinates
        self.sensors = []
        self.is_heating = False
        self.is_cooling = False

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def activate_heating(self, delta=3):
        self.is_heating = True
        self.is_cooling = False
        for sensor in self.sensors:
            sensor.adjust_temperature(delta)

    def activate_cooling(self, delta=2):
        self.is_heating = False
        self.is_cooling = True
        for sensor in self.sensors:
            sensor.adjust_temperature(-delta)

    def deactivate_systems(self):
        self.is_heating = False
        self.is_cooling = False
