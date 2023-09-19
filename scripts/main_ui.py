import tkinter as tk
from tkinter_function import button_creation as btn
from tkinter_function import create_top_bar as top_bar
from tkinter_function import standart_text as st
from planet import Planet
import time
from game_stats import game_stats as gs
from system import System



class Main_ui:
    def __init__(self):
        self.full_systems = []
        self.get_system()
        self.current_system = self.full_systems[0]
        print(self.current_system.system_name)



        #ui parts
        self.root = tk.Tk()
        self.root.geometry("1700x950")
        self.root.config(bg="black")
        

        self.top_frame = top_bar(self.root, self)
        self.top_frame.pack(pady= 50, padx= 40)


        self.main_ui_frame = tk.Frame(self.root, bg="white")
        self.main_ui_frame.pack()


        self.root.mainloop()
        




        
    def planets_in_systems(self):
        print("test")


        self.current_side_bar = tk.Frame(self.main_ui_frame, bg="white", width=50)
        self.current_main_frame = tk.Frame(self.main_ui_frame, bg="white", width=1200, height=600)
        self.current_main_frame.grid_propagate(False)
        self.current_side_bar.grid(row=0, column=0, padx=15)
        self.current_main_frame.grid(row=0, column=1, padx=100, pady=50)
        for planet in self.current_system.planets:
            planet_button = btn(self.current_main_frame, text_add=f"{planet.planet_name} \n\n Distence from sun: 0 \n\n Distence from current planet: 0 \n\n population:  ", background_coller="orange")
            planet_button.grid(row=0, column=0)
            pass        


    def get_system(self, system_name = "Milky_way"):
        new_system = System(system_name)
        new_system.get_planet()
        self.full_systems.append(new_system)
