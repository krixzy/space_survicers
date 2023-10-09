from random import randint
from game_stats import game_stats as gs
from building_order import Building_order

#generate the planet class
class Planet:
    def __init__(self, planet_name):
        self.planet_name = planet_name

        #buildings
        self.miners = 10
        self.factory = 100
        self.science_center = 0
        self.space_port = 0
        self.building_orders = []

        
        

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
        self.player_iron = 1000.0
        self.player_copper = 1000.0
        self.player_unobtanium = 0.0
        self.player_rare_metals = 0.0
        self.player_hydrogen = 0.0


        self.x_position = 0
        self.y_position = 0
        # mining power


        
        #generate planets minirals and accessibility
    def generate_planet(self, first, iron_amount=5000, copper_amount=5000, rare_metals_amount = 1000, unobtanium_amount = 0, hydrogen_amount = 2000, x_position = 10, y_position = 10  ):
        



        if first:
            self.planet_copper = 100000
            self.planet_hydrogen = 10000
            self.planet_iron = 100000
            self.planet_rare_metals = 2000
            self.palent_unobtanium = 0
            self.planet_copper_accessibility = 1
            self.planet_iron_accessibility = 1
            self.planet_hydrogen_accessibility = 1
            self.planet_rare_metals_accessibility = 0.5
            self.planet_unobtanium_accessibility = 0.1
            self.x_position = 1000
            self.y_position = -1000
            pass


        else:
            self.x_position = x_position
            self.y_position = y_position
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


        self.entry_value = [""] * 4

        #mining planets and add it to your stock on planet

    def create_building_order(self, building_to_build, amount, master):
        try:
            if(self.check_price(building_to_build, amount.get())):
                self.building_orders.append(Building_order(building_to_build, amount.get(), self))
                amount.delete(0, 'end')
                master.create_popup_screen("Created ordre")
            else:
                master.create_popup_screen("Cant afford")


        except NameError:
            print(f"Building order not createt there was an error{NameError}")
    def mine_planet(self):

        #mining values is the amount mined every tick, deppending on diffrent facktors 
        self.copper_mining_value = round(self.miners * self.planet_copper_accessibility * gs["miners_stats"]["mining_power"], 1)
        self.iron_mining_value = round(self.miners * self.planet_iron_accessibility * gs["miners_stats"]["mining_power"], 1)
        self.rare_metals_mining_value = round(self.miners * self.planet_rare_metals_accessibility * gs["miners_stats"]["mining_power"], 1)
        self.hydrogen_mining_value = round(self.miners * self.planet_hydrogen_accessibility * gs["miners_stats"]["mining_power"], 1)
        self.unobtanium_mining_value = round(self.miners * self.planet_unobtanium_accessibility * gs["miners_stats"]["mining_power"], 1)


        if(self.copper_mining_value <= self.planet_copper):
            self.planet_copper -= self.copper_mining_value
            self.player_copper += self.copper_mining_value
            self.planet_copper = round(self.planet_copper, 1)
            self.player_copper = round(self.player_copper, 1)

        elif(self.planet_copper > 0):
            self.player_copper += self.planet_copper
            self.planet_copper = 0




        if(self.iron_mining_value <= self.planet_iron):
            self.planet_iron -= self.iron_mining_value
            self.player_iron += self.iron_mining_value
            self.planet_iron = round(self.planet_iron, 1)
            self.player_iron = round(self.player_iron, 1)
        
        elif(self.iron_mining_value > 0 ):
            self.player_iron += self.planet_iron
            self.planet_iron = 0




        if(self.rare_metals_mining_value <= self.planet_rare_metals):
            self.planet_rare_metals -= self.rare_metals_mining_value
            self.player_rare_metals += self.rare_metals_mining_value
            self.planet_rare_metals = round(self.planet_rare_metals, 1)
            self.player_rare_metals = round(self.player_rare_metals, 1)

        elif(self.planet_rare_metals > 0):
            self.player_rare_metals += self.planet_rare_metals
            self.planet_rare_metals = 0


        
        
        
        
        if(self.hydrogen_mining_value <= self.planet_hydrogen):
            self.planet_hydrogen -= self.hydrogen_mining_value
            self.player_hydrogen += self.hydrogen_mining_value
            self.planet_hydrogen = round(self.planet_hydrogen, 1)
            self.player_hydrogen = round(self.player_hydrogen, 1)

        elif(self.planet_hydrogen > 0):
            self.player_hydrogen += self.planet_hydrogen
            self.planet_hydrogen = 0





        if(self.unobtanium_mining_value <= self.planet_unobtanium):
            self.planet_unobtanium -= self.unobtanium_mining_value
            self.player_unobtanium += self.unobtanium_mining_value
            self.planet_unobtanium = round(self.palent_unobtanium, 1)
            self.player_unobtanium = round(self.player_unobtanium, 1)

        elif(self.planet_unobtanium > 0):
            self.player_unobtanium += self.planet_unobtanium
            self.planet_unobtanium = 0    





    def build(self):
        try:
            if(len(self.building_orders) > 0):
                for object in self.building_orders:
                    object.build()
        except NameError:
            print(f"trying to run build in planet, but this went worng {NameError}")
        pass



    def kill_order(self, incoming_id):
        try:
            for index, object_to_kill in enumerate(self.building_orders):
                print(object_to_kill)
                if id(object_to_kill) == incoming_id:
                    self.building_orders.pop(index)
        
            
        except NameError:
            print(f"the killing of a build order did not work: {NameError}")



        

    def check_price(self, building_type, amount):
        try:
            building_price = gs[f"{building_type}_stats"][f"{building_type}_price"] 
            for key in building_price:
                price = building_price[key] * int(amount)
                current = getattr(self, f"player_{key}")
                if(current >= price):
                    pass

                else:
                    return False
            for key in building_price:
                price = building_price[key] * int(amount)
                current = getattr(self, f"player_{key}")
                current -= price
                setattr(self, f"player_{key}", current)
            
            return True

        except NameError:
            print(f"the price check is not working{NameError}")

        
        
        
        
        
        























