class Greenhouse:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.is_heating = False
        self.is_cooling = False

    def activate_heating(self):
        self.is_heating = True
        self.is_cooling = False

    def activate_cooling(self):
        self.is_heating = False
        self.is_cooling = True

    def deactivate_systems(self):
        self.is_heating = False
        self.is_cooling = False
