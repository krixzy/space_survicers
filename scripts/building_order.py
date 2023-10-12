from game_stats import game_stats as gs



class Building_order:

    def __init__(self, building_to_build, amount, master):
        self.factory_assigned = 0
        self.buildings_to_build = building_to_build
        self.amount = int(amount)
        self.accumulated_building_power = 0
        self.master = master
        self.id = id(self)
        self.building_percentage = 0




    def build(self):
 
        building_power = gs["factory_stats"]["factory_building_power"] * self.factory_assigned
        building_cost = gs[f"{self.buildings_to_build}_stats"][f"{self.buildings_to_build}_building_power_cost"]
        self.accumulated_building_power += building_power
        self.calculate_building_percentage(building_cost)
        while (self.accumulated_building_power >= building_cost):
            if(self.buildings_to_build == "factory"):
                current_building = getattr(self.master, f"total_{self.buildings_to_build}")
                current_building += 1
                setattr(self.master, f"total_{self.buildings_to_build}", current_building)
            current_building = getattr(self.master, self.buildings_to_build)
            current_building += 1
            setattr(self.master, self.buildings_to_build, current_building)
            self.accumulated_building_power -= building_cost
            self.amount -= 1
            self.calculate_building_percentage(building_cost)


            if(self.amount <= 0):
                self.master.factory += self.factory_assigned
                self.master.kill_order(self.id)
                self.accumulated_building_power = 0
                


    def calculate_building_percentage(self, building_cost):
        self.building_percentage = round(self.accumulated_building_power / building_cost * 100, 2)

    def add_factory(self, ui_page):
        try:
            if(self.master.factory > 0):
                self.master.factory -= 1
                self.factory_assigned += 1
                self.ui_page = ui_page
                ui_page.update_planet()
        except NameError:
            print(f"an error happend when trying to add {NameError}")


    def remove_factory(self, ui_page):
        try:
            if(self.factory_assigned > 0):
                self.master.factory += 1
                self.factory_assigned -= 1
                ui_page.update_planet()
        except NameError:
            print(f"an error happend when trying to remove {NameError}")