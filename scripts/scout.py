from ships import ship

class scout(ship):
    def __init__(self, engine, iron_cost, copper_cost, rare_metals_cost, unobtanium_cost, name, class_type, fuel_tank, building_power_needed, weight, sensor):
        super().__init__(engine, iron_cost, copper_cost, rare_metals_cost, unobtanium_cost, name, class_type, fuel_tank, building_power_needed, weight)
        self.sensor = sensor
        