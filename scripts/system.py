import planet

class System():
    def __init__(self, system_name):
        self.system_name = system_name
        self.planets = []

    def get_planet(self, planet_name = "Earth"):
        self.planets.append(planet.Planet(planet_name))
    



