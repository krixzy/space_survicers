import tkinter as tk
from tkinter_function import button_creation as btn
from tkinter_function import create_top_bar as top_bar
from tkinter_function import standart_text as st
from planet import Planet
import time
import multiprocessing
from multiprocessing import Queue
from game_stats import game_stats as gs



class planet_ui:
    def __init__(self, planet, queue):
        self.planet = planet
        self.queue = queue
        self.current_frame = ""
        # create screen for planets
        self.root = tk.Tk()
        self.root.geometry("1700x950")
        self.root.config(bg="black")

        #inserts the top bar of buttons
        self.main_planet_ui()
        self.root.after(1000, self.update_planet)

        self.root.mainloop()
    

    def test():
        pass



    def main_planet_ui(self):

        #top bar with all its buttons
        self.top_frame = top_bar(self.root, self)
        self.top_frame.pack(fill="x", pady= 50, padx= 40)

        self.main_planet_frame = tk.Frame(self.root, bg="white")
        
        #sidebar with all its buttons
        self.side_bar_frame = self.create_planet_side_bar(self.main_planet_frame)
        
        self.create_planet_mining_stats_main_frame()

        self.main_planet_frame.pack()


    def update_planet(self):
        try:
            
                if not self.queue.empty():
                    self.planet = self.queue.get()  
                    if(self.current_frame == "stats_frame"):
                        self.create_planet_mining_stats_main_frame()
                
                
                self.root.after(3000, self.update_planet)

               



        except KeyboardInterrupt:
            print("gameendet")

#_______________________________________________________________________________________________________________________________________________________________________
                                                                                #mining stats side
                                                                                
                    
    def create_planet_mining_stats_main_frame(self):
        self.current_frame = "stats_frame"
        self.current_main_frame = tk.Frame(self.main_planet_frame, bg="white", width=1200, height=600)
        self.current_main_frame.grid_propagate(False)
        self.current_main_frame.grid(row=0, column=1, padx=100, pady=50)
        self.mining_stats_stats_frame()
        print(self.planet.planet_copper)
        #texts with stats from current plant
        self.planet_name = tk.Label(self.current_main_frame, text=f"Planet: {self.planet.planet_name}", font=("Arial", 20), bg="white")
        self.planet_name.grid(row=0, column=3, padx= 140)

        self.planet_miners_stats = tk.Label(self.current_main_frame, text=f"Miners: {self.planet.miners}", font=("Arial", 14), bg="white")
        self.planet_miners_stats.grid(row=1, column=2, padx=140, pady=40)

        self.planet_mining_tech_bonus = tk.Label(self.current_main_frame, text=f"Current tech bonus: 0", font=("Arial", 14), bg="white")
        self.planet_mining_tech_bonus.grid(row=1, column=4, padx=140, pady=40)
    
    def mining_stats_stats_frame(self):

        self.resource_frame = tk.Frame(self.current_main_frame, bg="white", width=1000, height=450, borderwidth=3, relief="solid" )
        self.resource_frame.grid_propagate(False)
        self.resource_frame.grid(row=2, column=2, columnspan=3)
        self.mining_stats_resource_type_frame()
        self.mining_stats_resource_planet_amount_frame()
        self.mining_stats_resource_planet_accessibility_frame()
        self.mining_stats_mining_power_frame()
        self.mining_stats_player_resource_frame()
 

    def mining_stats_resource_type_frame(self):
        self.resource_type_frame = tk.Frame(self.resource_frame, bg="white", borderwidth=2, relief="solid", height=444, width=199)
        self.resource_type_frame.grid_propagate(False)
        self.resource_type_frame.grid_columnconfigure(0, weight=1)
        self.resource_type_frame.grid_rowconfigure(1, weight=1)
        self.resource_type_frame.grid_rowconfigure(2, weight=1)
        self.resource_type_frame.grid_rowconfigure(3, weight=1)
        self.resource_type_frame.grid_rowconfigure(4, weight=1)
        self.resource_type_frame.grid_rowconfigure(5, weight=1)
        self.resource_type_frame.grid(row=0, column=0)


        self.resource_type = tk.Label(self.resource_type_frame, text="Type", bg="white", font=("Arial", 14), borderwidth=2, relief="solid", width=20, height=2)
        self.resource_type.grid(row=0, column=0)
        self.resource_copper = st(self.resource_type_frame, "Copper")
        self.resource_copper.grid(row=1, column=0)
        self.resource_iron = st(self.resource_type_frame, "Iron")
        self.resource_iron.grid(row=2, column=0)
        self.resource_unobtanium = st(self.resource_type_frame, "Unobtanium")
        self.resource_unobtanium.grid(row=5, column=0)
        self.resource_rare_metals = st(self.resource_type_frame, "Rare metals")
        self.resource_rare_metals.grid(row=3, column=0)
        self.resource_hydrogen = st(self.resource_type_frame, "Hydrogen")
        self.resource_hydrogen.grid(row=4, column=0)



    def mining_stats_resource_planet_amount_frame(self):
        self.resource_planet_amount_frame = tk.Frame(self.resource_frame, bg="white", borderwidth=2, relief="solid", height=444, width=199)
        self.resource_planet_amount_frame.grid_propagate(False)
        self.resource_planet_amount_frame.grid_columnconfigure(0, weight=1)
        self.resource_planet_amount_frame.grid_rowconfigure(1, weight=1)
        self.resource_planet_amount_frame.grid_rowconfigure(2, weight=1)
        self.resource_planet_amount_frame.grid_rowconfigure(3, weight=1)
        self.resource_planet_amount_frame.grid_rowconfigure(4, weight=1)
        self.resource_planet_amount_frame.grid_rowconfigure(5, weight=1)
        self.resource_planet_amount_frame.grid(row=0, column=1)



        self.resource_planet_amount = tk.Label(self.resource_planet_amount_frame, text="Planet", bg="white", borderwidth=2, relief="solid", width=20, height=2, font=("Arial", 14))
        self.resource_planet_amount.grid(row=0, column=0)
        self.resource_planet_amount_copper = st(self.resource_planet_amount_frame, f"{self.planet.planet_copper}")
        self.resource_planet_amount_copper.grid(row=1, column=0)
        self.resource_planet_amount_iron = st(self.resource_planet_amount_frame, f"{self.planet.planet_iron}")
        self.resource_planet_amount_iron.grid(row=2, column=0)
        self.resource_planet_amount_rare_metals = st(self.resource_planet_amount_frame, f"{self.planet.planet_rare_metals}")
        self.resource_planet_amount_rare_metals.grid(row=3, column=0)
        self.resource_planet_amount_hydrogen = st(self.resource_planet_amount_frame, f"{self.planet.planet_hydrogen}")
        self.resource_planet_amount_hydrogen.grid(row=4, column=0)
        self.resource_planet_amount_unobtanium = st(self.resource_planet_amount_frame, f"{self.planet.planet_unobtanium}")
        self.resource_planet_amount_unobtanium.grid(row=5, column=0)


    def mining_stats_resource_planet_accessibility_frame(self):
        self.resource_accessibility_frame = tk.Frame(self.resource_frame, bg="white", borderwidth=2, relief="solid", height=444, width=199)
        self.resource_accessibility_frame.grid_propagate(False)
        self.resource_accessibility_frame.grid_columnconfigure(0, weight=1)
        self.resource_accessibility_frame.grid_rowconfigure(1, weight=1)
        self.resource_accessibility_frame.grid_rowconfigure(2, weight=1)
        self.resource_accessibility_frame.grid_rowconfigure(3, weight=1)
        self.resource_accessibility_frame.grid_rowconfigure(4, weight=1)
        self.resource_accessibility_frame.grid_rowconfigure(5, weight=1)
        self.resource_accessibility_frame.grid(row=0, column=2)


        self.resource_accessibility = tk.Label(self.resource_accessibility_frame, bg="white", text=f"accessibility", borderwidth=2, relief="solid", width=20, height=2, font=("Arial", 14))
        self.resource_accessibility.grid(row=0, column=0)
        self.resource_accessibility_copper = st(self.resource_accessibility_frame, f"{self.planet.planet_copper_accessibility}")
        self.resource_accessibility_copper.grid(row=1, column=0)
        self.resource_accessibility_iron = st(self.resource_accessibility_frame, f"{self.planet.planet_iron_accessibility}")
        self.resource_accessibility_iron.grid(row=2, column=0)
        self.resource_accessibility_rare_metals = st(self.resource_accessibility_frame, f"{self.planet.planet_rare_metals_accessibility}")
        self.resource_accessibility_rare_metals.grid(row=3, column=0)
        self.resource_accessibility_hydrogen = st(self.resource_accessibility_frame, f"{self.planet.planet_hydrogen_accessibility}")
        self.resource_accessibility_hydrogen.grid(row=4, column=0)
        self.resoruce_accessibility_unobtanium = st(self.resource_accessibility_frame, f"{self.planet.planet_unobtanium_accessibility}")
        self.resoruce_accessibility_unobtanium.grid(row=5, column=0)

        
        


    def mining_stats_mining_power_frame(self):
        self.resource_mining_power_frame = tk.Frame(self.resource_frame, bg="white", borderwidth=2, relief="solid", height=444, width=199)
        self.resource_mining_power_frame.grid_propagate(False)
        self.resource_mining_power_frame.grid_columnconfigure(0, weight=1)
        self.resource_mining_power_frame.grid_rowconfigure(1, weight=1)
        self.resource_mining_power_frame.grid_rowconfigure(2, weight=1)
        self.resource_mining_power_frame.grid_rowconfigure(3, weight=1)
        self.resource_mining_power_frame.grid_rowconfigure(4, weight=1)
        self.resource_mining_power_frame.grid_rowconfigure(5, weight=1)
        self.resource_mining_power_frame.grid(row=0, column=3)



        self.resource_mining_power = tk.Label(self.resource_mining_power_frame, bg="white", borderwidth=2, relief="solid", width=20, height=2, font=("Arial", 14), text=f"Mining power")
        self.resource_mining_power.grid(row=0, column=0)
        self.resource_mining_power_copper = st(self.resource_mining_power_frame, f"{self.planet.copper_mining_value}")
        self.resource_mining_power_copper.grid(row=1, column=0)
        self.resource_mining_power_iron = st(self.resource_mining_power_frame, f"{self.planet.iron_mining_value}")
        self.resource_mining_power_iron.grid(row=2, column=0)
        self.resource_mining_power_rare_metals = st(self.resource_mining_power_frame, f"{self.planet.rare_metals_mining_value}")
        self.resource_mining_power_rare_metals.grid(row=3, column=0)
        self.resource_mining_power_hydrogen = st(self.resource_mining_power_frame, f"{self.planet.hydrogen_mining_value}")
        self.resource_mining_power_hydrogen.grid(row=4, column=0)
        self.resource_mining_power_unobtanium = st(self.resource_mining_power_frame, f"{self.planet.unobtanium_mining_value}")
        self.resource_mining_power_unobtanium.grid(row=5, column=0)


    def mining_stats_player_resource_frame(self):
        self.player_resource_frame = tk.Frame(self.resource_frame, bg="white", borderwidth=2, relief="solid", height=444, width=199)
        self.player_resource_frame.grid_propagate(False)
        self.player_resource_frame.grid_columnconfigure(0, weight=1)
        self.player_resource_frame.grid_rowconfigure(1, weight=1)
        self.player_resource_frame.grid_rowconfigure(2, weight=1)
        self.player_resource_frame.grid_rowconfigure(3, weight=1)
        self.player_resource_frame.grid_rowconfigure(4, weight=1)
        self.player_resource_frame.grid_rowconfigure(5, weight=1)
        self.player_resource_frame.grid(row=0, column=4)


        self.player_resource = tk.Label(self.player_resource_frame, bg="white", borderwidth=2, relief="solid", width=20, height=2, font=("Arial", 14), text=f"player")
        self.player_resource.grid(row=0, column=0)
        self.player_resource_copper = st(self.player_resource_frame, f"{self.planet.player_copper}")
        self.player_resource_copper.grid(row=1, column=0)
        self.player_resource_iron = st(self.player_resource_frame, f"{self.planet.player_iron}")
        self.player_resource_iron.grid(row=2, column=0)
        self.player_resource_rare_metals = st(self.player_resource_frame, f"{self.planet.player_rare_metals}")
        self.player_resource_rare_metals.grid(row=3, column=0)
        self.player_resource_hydrogen = st(self.player_resource_frame, f"{self.planet.player_hydrogen}")
        self.player_resource_hydrogen.grid(row=4, column=0)
        self.player_resource_unobtanium = st(self.player_resource_frame, f"{self.planet.player_unobtanium}")
        self.player_resource_unobtanium.grid(row=5, column=0)

  

#__________________________________________________________________________________________________________________________________________________________________________________________________________
                                                                                            #building side



    def create_planet_build_frame(self):
        self.current_frame = "building_frame"
        self.current_main_frame = tk.Frame(self.main_planet_frame, bg="white", width=1200, height=700)
        self.current_main_frame.grid_propagate(False)
        self.current_main_frame.grid(row=0, column=1)





        #create the side bar for planets
    def create_planet_side_bar(self, master):
        self.button_list = []
        self.planet_sidebar_frame = tk.Frame(master, bg="white")
        
        

        #stats button
        self.stats_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="Mining stats", width=15, command=self.create_planet_mining_stats_main_frame, font_size= 14)
        self.button_list.append(self.stats_button)

        #build button
        self.build_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="Build", width=15, command=self.create_planet_build_frame)
        self.button_list.append(self.build_button)

        #Technologies button
        self.Technologies_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="Technologies", width=15)
        self.button_list.append(self.Technologies_button)

        #ship button
        self.ship_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="Ship_build", width=15)
        self.button_list.append(self.ship_button)
        

        for index, buttons in enumerate(self.button_list):
           buttons.grid(row=index, column=0, pady=30)
        
        self.planet_sidebar_frame.grid(row=0, column=0, padx=15)
        return self.planet_sidebar_frame
        











def main_loop():
    earth = Planet("Earth")
    earth.generate_resources()

    queue = Queue()


    process1 = multiprocessing.Process(target=planet_ui, args=(earth, queue))
    process2 = multiprocessing.Process(target=game_engine, args=(earth, queue))

    process2.start()
    process1.start()

    process1.join()
    process2.terminate()  # Afslutter spilmotoren
def game_engine(planet, queue):
    while True:
        time.sleep(6)
        planet.mine_planet()
        queue.put(planet)
        

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main_loop()