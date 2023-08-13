import time

class Planet:
    def __init__(self, planet_name):
        self.planet_name = planet_name

        #buildings
        self.miners = 0
        

        #planets stats
        self.planet_iron = 0.0
        self.planet_copper = 0.0
        self.palent_unobtanium = 0.0
        self.planet_rare_metals = 0.0
        self.planet_hydrogen = 0.0


        #plants mining accessibility

        self.planet_iron_accessibility = 0.0
        self.planet_copper_accessibility = 0.0
        self.palent_unobtanium_accessibility = 0.0
        self.planet_rare_metals_accessibility = 0.0
        self.planet_hydrogen_accessibility = 0.0


        #player stats
        self.player_iron = 0.0
        self.player_copper = 0.0
        self.player_unobtanium = 0.0
        self.player_rare_metals = 0.0
        self.player_hydrogen = 0.0
    

