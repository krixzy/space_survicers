from planet import Planet

class System():
    def __init__(self, system_name):
        self.system_name = system_name
        self.planets = []

    def get_planet(self, planet_name = "Earth"):
        planet = Planet(planet_name)
        planet.generate_resources()
        self.planets.append(planet) 
    



