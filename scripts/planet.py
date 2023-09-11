import time
from random import randint
from game_stats import game_stats as gs
#generate the planet class
class Planet:
    def __init__(self, planet_name):
        self.planet_name = planet_name

        #buildings
        self.miners = 5
        self.factorys = 0


        
        self.building_power = 0
        

        #planets stats
        self.planet_iron = 0.0
        self.planet_copper = 0.0
        self.planet_unobtanium = 0.0
        self.planet_rare_metals = 0.0
        self.planet_hydrogen = 0.0


        #plants mining accessibility

        self.planet_iron_accessibility = 0.0
        self.planet_copper_accessibility = 0.0
        self.planet_unobtanium_accessibility = 0.0
        self.planet_rare_metals_accessibility = 0.0
        self.planet_hydrogen_accessibility = 0.0


        #player stats
        self.player_iron = 0.0
        self.player_copper = 0.0
        self.player_unobtanium = 0.0
        self.player_rare_metals = 0.0
        self.player_hydrogen = 0.0



        # mining power


        
        #generate planets minirals and accessibility
    def generate_resources(self, iron_amount=5000, copper_amount=3000, rare_metals_amount = 1000, unobtanium_amount = 0, hydrogen_amount = 2000):
        self.planet_copper = copper_amount
        self.planet_hydrogen = hydrogen_amount
        self.planet_iron = iron_amount
        self.planet_rare_metals = rare_metals_amount
        self.palent_unobtanium = unobtanium_amount

        self.planet_copper_accessibility = randint(1, 10) / 10
        self.planet_iron_accessibility = randint(1, 10) / 10
        self.planet_hydrogen_accessibility = randint(1, 10) / 10
        self.planet_rare_metals_accessibility = randint(1, 10) / 10
        self.planet_unobtanium_accessibility = randint(1, 10) / 10

        self.copper_mining_value = self.miners * self.planet_copper_accessibility * gs["miners_stats"]["mining_power"]
        self.iron_mining_value = self.miners * self.planet_iron_accessibility * gs["miners_stats"]["mining_power"]
        self.rare_metals_mining_value = self.miners * self.planet_rare_metals_accessibility * gs["miners_stats"]["mining_power"]
        self.hydrogen_mining_value = self.miners * self.planet_hydrogen_accessibility * gs["miners_stats"]["mining_power"]
        self.unobtanium_mining_value = self.miners * self.planet_unobtanium_accessibility * gs["miners_stats"]["mining_power"]


        #mining planets and add it to your stock on planet
    def mine_planet(self):

        #mining values is the amount mined every tick, deppending on diffrent facktors 
        self.copper_mining_value = self.miners * self.planet_copper_accessibility * gs["miners_stats"]["mining_power"]
        self.iron_mining_value = self.miners * self.planet_iron_accessibility * gs["miners_stats"]["mining_power"]
        self.rare_metals_mining_value = self.miners * self.planet_rare_metals_accessibility * gs["miners_stats"]["mining_power"]
        self.hydrogen_mining_value = self.miners * self.planet_hydrogen_accessibility * gs["miners_stats"]["mining_power"]
        self.unobtanium_mining_value = self.miners * self.planet_unobtanium_accessibility * gs["miners_stats"]["mining_power"]


        if(self.copper_mining_value <= self.planet_copper):
            self.planet_copper -= self.copper_mining_value
            self.player_copper += self.copper_mining_value

        if(self.iron_mining_value <= self.planet_iron):
            self.planet_iron -= self.iron_mining_value
            self.player_iron += self.iron_mining_value

        if(self.rare_metals_mining_value <= self.planet_rare_metals):
            self.planet_rare_metals -= self.rare_metals_mining_value
            self.player_rare_metals += self.rare_metals_mining_value
        
        if(self.hydrogen_mining_value <= self.planet_hydrogen):
            self.planet_hydrogen -= self.hydrogen_mining_value
            self.player_hydrogen += self.hydrogen_mining_value
        
        
        if(self.unobtanium_mining_value <= self.planet_unobtanium):
            self.planet_unobtanium -= self.unobtanium_mining_value
            self.player_unobtanium += self.unobtanium_mining_value
            
        






# earth.mine_planet()

