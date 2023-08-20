import tkinter as tk
from tkinter_function import button_creation as btn
from tkinter_function import create_top_bar as top_bar


class planet_ui:
    def __init__(self, planet):
        self.planet = planet

        # create screen for planets
        self.root = tk.Tk()
        self.root.geometry("1700x950")
        self.root.config(bg="black")

        #inserts the top bar of buttons
        
        self.main_planet_ui()
        self.root.mainloop()
    




    def main_planet_ui(self):
        self.top_frame = top_bar(self.root)
        self.top_frame.pack(fill="x", pady= 50, padx= 40)

        self.main_planet_frame = tk.Frame(self.root, bg="white")
        
        self.side_bar_frame = self.create_planet_side_bar(self.main_planet_frame)
        self.side_bar_frame.grid(row=0, column=0)

        self.test = tk.Frame(self.main_planet_frame, bg="white", width=1400, height=700)
        self.test.grid(row=0, column=1)
        self.main_planet_frame.pack()


    def create_planet_stats_bar(self):
        pass

        

        #create the side bar for planets
    def create_planet_side_bar(self, master):
        self.button_list = []
        self.planet_sidebar_frame = tk.Frame(master, bg="white")
        
        

        #stats button
        self.stats_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="Stats", width=15)
        self.button_list.append(self.stats_button)

        #build button
        self.build_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="build", width=15)
        self.button_list.append(self.build_button)

        #Technologies button
        self.Technologies_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="Technologies", width=15)
        self.button_list.append(self.Technologies_button)

        #ship button
        self.ship_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="ship_build", width=15)
        self.button_list.append(self.ship_button)
        

        for index, buttons in enumerate(self.button_list):
           buttons.grid(row=index, column=0, pady=30)
        
        return self.planet_sidebar_frame
        
planet_ui("test")