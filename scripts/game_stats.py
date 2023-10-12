game_stats = {
    "systems": [],
    "miners_stats":{
        "mining_power": 1,
        "miners_price":{
            "copper": 100,
            "iron":25
        },
        "miners_building_power_cost": 800,
        "miners_waight": 1000
    },
    "factory_stats":{
        "factory_building_power":10,
        "factory_building_power_cost":1200,
        "factory_price":{
            "copper": 100,
            "iron": 200,
        },
        "factory_waight": 5000
        
    },
    "science_center_stats":{
        "science_center_building_power_cost": 2200,
        "science_center_price":{
            "copper":250,
            "iron":500,
            "rare_metals": 100
        },
        "science_center_waight":25000
    },
    "space_port_stats":{
        "space_port_building_power_cost": 1500,
        "space_port_building_power": 5,
        "space_port_price":{
            "copper":200,
            "iron":200
        },
        "space_port_waight":50000
    },
    "ship_stats":{
        "ship_type":{
            "scout":{
               "researched": False 
            },
            "freighter":{
                "researched": True
            }
        },
        "hull_types":{
        "base hull":{
            "researched": True,
            "iron_cost": 500,
            "copper_cost": 100,
            "rare_metals":0,
            "unobtanium":0,
            "building_power_cost": 500,
            "weight": 5000
        }
        }

    },
    "engine_stats":{
        "engine_types":{
        "Base engine":{
            "researched": True,
            "iron_cost":100,
            "copper_cost": 150,
            "rare_metals": 0,
            "unobtanium": 0, 
            "power": 500,
            "fuel_cost": 10,
            "building_power_cost": 200,
            "weight": 1000
        },
        "Warp core engine":{
            "researched": True,
            "iron_cost":200,
            "copper_cost": 450,
            "rare_metals": 50,
            "unobtanium": 0, 
            "power": 1100,
            "fuel_cost": 100,
            "building_power_cost": 800,
            "weight": 1200
        },

        }

    },
    "fuel_tank_stats":{
        "fuel_types":{
        "Base fuel tank":{
            "researched": True,
            "iron_cost":200,
            "copper_cost": 50,
            "rare_metals": 0,
            "unobtanium": 0, 
            "max_fuel": 5000,
            "building_power_cost": 50,
            "weight": 5000
        },
        }

    },
    "sensor":{
        "sensor_types":{
            "researched":True
        }
    }
}