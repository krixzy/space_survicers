import time
from random import randint
#generate the planet class
class Planet:
    def __init__(self, planet_name):
        self.planet_name = planet_name

        #buildings
        self.miners = 0
        self.factorys = 0


        #
        self.building_power = 0
        

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

        
        #generate planets minirals and accessibility
    def generate_planet(self, iron_amount=5000, copper_amount=3000, rare_metals_amount = 1000, unobtanium_amount = 0, hydrogen_amount = 2000):
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




        #mining planets and add it to your stock on planet
    def mine_planet(self):

        #mining values is the amount mined every tick, deppending on diffrent facktors 
        copper_mining_value = self.miners * self.planet_copper_accessibility
        iron_mining_value = self.miners * self.planet_iron_accessibility
        rare_metals_mining_value = self.miners * self.planet_rare_metals_accessibility
        hydrogen_mining_value = self.miners * self.planet_hydrogen_accessibility
        unobranium_mining_value = self.miners * self.palent_unobtanium_accessibility




        print(copper_mining_value)
        pass



# earth = Planet("Earth")
# earth.generate_planet()
# print(earth.planet_copper, earth.planet_copper_accessibility)

# earth.mine_planet()

