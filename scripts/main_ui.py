import tkinter as tk
from tkinter_function import button_creation as btn
from tkinter_function import create_top_bar as top_bar
from tkinter_function import standart_text as st
from planet import Planet
from planet_ui import planet_ui
import time
from game_stats import game_stats as gs
from system import System




class Main_ui:
    def __init__(self):
        self.full_systems = []
        self.get_system()

        self.current_system = gs["systems"][0]
        self.current_planet = gs["systems"][0].planets[0]
        



        #ui parts
        self.root = tk.Tk()
        self.root.geometry("1750x950")
        self.root.config(bg="black")
        self.change_current_planet_chrange_current_system(self.current_planet, self.current_system)
        


        self.top_frame = top_bar(self.root, self)
        self.top_frame.pack(padx= 40)


        self.main_ui_frame = tk.Frame(self.root, bg="white")
        self.main_ui_frame.pack()

        self.root.after(2000, self.game_loop)
        self.root.mainloop()
        












    def game_loop(self):
        try:
            for systems in gs["systems"]:
              for planets in systems.planets:
                    planets.mine_planet()
                    planets.build()
            if hasattr(self, "current_planet_ui"):
                self.current_planet_ui.update_planet()
        except NameError as e:
            print(NameError)    
        self.root.after(4000, self.game_loop)
        



    def planets_in_system_frame(self):

        self.delete_current_main_fram()
        self.current_side_bar = tk.Frame(self.main_ui_frame, bg="white", width=50)
        self.current_main_frame = tk.Frame(self.main_ui_frame, bg="white", width=1200, height=600)
        self.current_main_frame.grid_propagate(False)
        self.current_side_bar.grid(row=0, column=0, padx=15)
        self.current_main_frame.grid(row=0, column=1, padx=100, pady=50)
        x = 0
        y = 0
        for planet in self.current_system.planets:
            if(x > 2):
                y += 1
                x = 0
            x+=1
            planet_button = btn(self.current_main_frame, command=self.change_current_planet_ui ,text_add=f"{planet.planet_name} \n\n Distence from sun: 0 \n\n Distence from current planet: 0 \n\n population:  ", background_coller="orange")
            planet_button.grid(row=y, column=x ,padx=20, pady=10)
            pass        



    def change_current_planet_chrange_current_system(self, new_planet, new_system):
        self.current_planet = new_planet
        self.current_system = new_system
        self.current_system_current_planet_frame = tk.Frame(self.root, bg="black")
        current_planet_text = tk.Label(self.current_system_current_planet_frame, bg="white", font=("Arial", 14), text=f"Current planet:      {self.current_planet.planet_name}")
        current_planet_text.grid(row=0, column=0, padx=80, pady=15) 
        current_system_text = tk.Label(self.current_system_current_planet_frame, bg="white", font=("Arial", 14), text=f"Current system:      {self.current_system.system_name}")
        current_system_text.grid(row=0, column=1, padx=80, pady=15)
        self.current_system_current_planet_frame.pack()




    def change_current_planet_ui(self):
        self.delete_current_main_fram()
        self.current_planet_ui = planet_ui(self.current_planet, self.root)

        pass

    def get_system(self, system_name = "Milky way"):
        new_system = System(system_name, 100, -100)
        new_system.get_planet()
        gs["systems"].append(new_system)


    def delete_current_main_fram(self):
        if hasattr(self, "current_planet_ui"):
            self.current_planet_ui.destroy()
            del self.current_planet_ui
            
        if hasattr(self, "current_main_frame"):
            self.current_main_frame.destroy()