from system import System

class Main():
    
    def __init__(self):
        self.systems = []
    
    def get_systems(self, system_name = "sol"):
        system_to_add = System(system_name)
        system_to_add.get_planet()
        self.systems.append(system_to_add)
        

