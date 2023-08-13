import planet
import system
class Main():
    
    def __init__(self):
        self.systems = []
    
    def get_systems(self, system_name = "sol"):
        system_to_add = system.System(system_name)
        system_to_add.get_planet()
        self.systems.append(system_to_add)
        print(self.systems[0].system_name)
        print(self.systems[0].planets[0].planet_name)


test = Main()
test.get_systems()


