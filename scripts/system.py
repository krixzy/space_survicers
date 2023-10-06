from planet import Planet

class System():
    def __init__(self, system_name, x, y):
        self.system_name = system_name
        self.planets = []
        self.x_position = x
        self.y_position = y

    def get_planet(self, planet_name = "Earth"):
        planet = Planet(planet_name)
        planet.generate_planet(True)
        
        self.planets.append(planet) 
    



