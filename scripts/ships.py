class ship:
    def __init__(self, engine, iron_cost, copper_cost, rare_metals_cost, unobtanium_cost, name, class_type, fuel_tank, building_power_needed, weight):
        self.current_x_position = 0
        self.current_y_position = 0
        self.engine = engine
        self.iron_cost = iron_cost
        self.copper_cost = copper_cost
        self.rare_metals_cost = rare_metals_cost
        self.unobtanium_cost = unobtanium_cost
        self.name = name
        self.class_type = class_type
        self.fuel_tank = fuel_tank
        self.building_power_needed = building_power_needed
        self.weight = weight
        
