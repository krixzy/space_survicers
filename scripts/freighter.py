from ships import ship

class freighter(ship):
    def __init__(self, engine, iron_cost, copper_cost, rare_metals_cost, unobtanium_cost, name, class_type, fuel_tank, cargo_space):
        super().__init__(engine, iron_cost, copper_cost, rare_metals_cost, unobtanium_cost, name, class_type, fuel_tank)
        self.cargo_space = cargo_space