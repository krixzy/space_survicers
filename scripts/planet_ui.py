import tkinter as tk
from tkinter import ttk
from tkinter_function import button_creation as btn
from tkinter_function import create_top_bar as top_bar
from tkinter_function import standart_text as st
from tkinter_function import standart_build_text as sbt
from planet import Planet
import time
import multiprocessing
from multiprocessing import Queue
from game_stats import game_stats as gs



class planet_ui:
    def __init__(self, planet, root):
        self.planet = planet
        self.current_frame = ""
        # create screen for planets
        self.root = root
        #inserts the top bar of buttons
        




 
        self.main_planet_ui()
        

    

    def main_planet_ui(self):

        #top bar with all its buttons

        self.main_planet_frame = tk.Frame(self.root, bg="white")
        
        #sidebar with all its buttons
        self.side_bar_frame = self.create_planet_side_bar(self.main_planet_frame)
        
        # self.create_planet_mining_stats_main_frame()


        self.mining_stats_page()

        self.main_planet_frame.pack()


    def update_planet(self):
        try:
            if (hasattr(self, "main_planet_frame") and self.current_frame == "stats_frame"):
                self.mining_stats_page()
            if (hasattr(self, "main_planet_frame") and self.current_frame == "building_order_frame"):
                self.building_order_page()
        except NameError:
            print(f"gameendet{NameError}")



#___________________________________________________________________________________________________________________________________________________________________________________________________
                                                                            #alle button commands


    def mining_stats_page(self):
        array_of_values = [
            ["L",["Type", "Copper", "Iron", "Rare metals", "Hydrogen", "Unobtanium"]], 
            ["L",["Planet", self.planet.planet_copper, self.planet.planet_iron, self.planet.planet_rare_metals, self.planet.planet_hydrogen, self.planet.planet_unobtanium]],
            ["L",["accessibility",self.planet.planet_copper_accessibility, self.planet.planet_iron_accessibility, self.planet.planet_rare_metals_accessibility, self.planet.planet_hydrogen_accessibility, self.planet.planet_unobtanium_accessibility]],
            ["L",["Mining power", self.planet.copper_mining_value, self.planet.iron_mining_value, self.planet.rare_metals_mining_value, self.planet.hydrogen_mining_value, self.planet.unobtanium_mining_value]],
            ["L",["Player", self.planet.player_copper, self.planet.player_iron, self.planet.player_rare_metals, self.planet.player_hydrogen, self.planet.player_unobtanium]]
                ]
        self.current_frame = "stats_frame"
        self.build_current_main_frame(array_of_values, f"Miners: {self.planet.miners}", f"Current tech bonus: 0", f"mining power pr miners {gs['miners_stats']['mining_power']}" )



    def buidling_stats_page(self):
        planet_building_info_array = [
            ["L", ["Type", "Mines", "Factorys", "science_center", "space_ports"]],
            ["L", ["Current amount",self.planet.miners, self.planet.factory, self.planet.science_center, self.planet.space_port]],
            ["L", ["Building power cost", gs["miners_stats"]["miners_building_power_cost"], gs["factory_stats"]["factory_building_power_cost"], gs["science_center_stats"]["science_center_building_power_cost"], gs["space_port_stats"]["space_port_building_power_cost"]]],
            ["L", ["Price", self.object_price_converter(gs["miners_stats"]["miners_price"]), self.object_price_converter(gs["factory_stats"]["factory_price"]),self.object_price_converter(gs["science_center_stats"]["science_center_price"]),self.object_price_converter(gs["space_port_stats"]["space_port_price"])]],
            ["E", ["Order_amount", " ", " ", " ", " "]],
            ["B", ["Build", lambda:self.planet.create_building_order("miners", self.planet.entry_value[0], self), lambda: self.planet.create_building_order("factory", self.planet.entry_value[1], self), lambda: self.planet.create_building_order("science_center", self.planet.entry_value[2], self), lambda: self.planet.create_building_order("space_port", self.planet.entry_value[3], self)]]
        ]
        self.Check_for_main_frame()
        self.current_frame = "building_frame"
        self.build_current_main_frame(planet_building_info_array, f"Free factorys: {self.planet.factory}", f"Current tech bonus: 0", f"building power pr facotry {gs['factory_stats']['factory_building_power']}", text_size=14)


    def building_order_page(self):
        self.Check_for_main_frame()
        self.current_frame = "building_order_frame"
        self.build_current_main_frame( self.planet.building_orders,f"Free factorys: {self.planet.factory}", f"Current tech bonus: 0", f"building power pr facotry {gs['factory_stats']['factory_building_power']}", text_size=14, type="row")






#_______________________________________________________________________________________________________________________________________________________________________
                                                                                #current main frame builder
                                                                                


    def build_current_main_frame(self, array_of_values, building_type, building_tech, building_power, text_size = 14, type = "cul", label_with = 100, label_height = 5):
        self.current_main_frame = tk.Frame(self.main_planet_frame, bg="white", width=1250, height=650)
        self.current_main_frame.grid_propagate(False)
        self.current_main_frame.grid(row=0, column=1, padx=50, pady=10)
         #texts with stats from current plant
        self.planet_name = tk.Label(self.current_main_frame, text=f"Planet: {self.planet.planet_name}", font=("Arial", 20), bg="white")
        self.planet_name.grid(row=0, column=3, padx= 140)

        self.planet_miners_stats = tk.Label(self.current_main_frame, text=building_type, font=("Arial", 16), bg="white")
        self.planet_miners_stats.grid(row=1, column=2, padx=100, pady=10)

        middle_labels = tk.Label(self.current_main_frame, text=building_power, font=("Arial", 16), bg="white")
        middle_labels.grid(row=1, column=3, padx=100, pady=10)  

        self.planet_mining_tech_bonus = tk.Label(self.current_main_frame, text=building_tech, font=("Arial", 16), bg="white")
        self.planet_mining_tech_bonus.grid(row=1, column=4, padx=100, pady=10)


        if(type == "cul"):
            frame_height = len(array_of_values[0][1]) * 100
            self.create_canves(frame_height)
            for index, array in enumerate(array_of_values):
                self.create_label_column(self.resource_frame, frame_height, index, array, label_height, label_with, text_size, len(array_of_values))
        
        if(type == "row"):
            frame_height = len(array_of_values) * 50
            if(frame_height > 0):
                self.create_canves(frame_height)
                for index, item in enumerate(array_of_values):
                    self.create_label_row(self.resource_frame, frame_height, item, index)

            else:
                pass

        
        


    def create_canves(self, frame_height):
        self.canvas = tk.Canvas(self.current_main_frame, height=600, width=1200)
        self.canvas.grid(row=2, column=0, columnspan=6)
        self.scrollbar = ttk.Scrollbar(self.current_main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=7, rowspan=3, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        self.resource_frame = tk.Frame(self.canvas, bg="white", height=frame_height, width=1200 )
        self.resource_frame.grid_propagate(False)
        self.resource_frame.pack()
        self.canvas.create_window((0,0), window=self.resource_frame, anchor="nw")





    def create_label_row(self, master, frame_height, item, index):
        current_frame = tk.Frame(master, bg="white", borderwidth=2, relief="solid", height=50, width=1199)
        current_frame.grid_propagate(False)
        current_frame.grid(row=index, column=0)
        tk.Label(current_frame, bg="white", text= f"Order: {index}               Building type: {item.buildings_to_build}               Current order amount: {item.amount}               Current factorys assigned: {item.factory_assigned}              ", font=("Arial", 14)).grid(row=0, column=0, padx=10)
        tk.Button(current_frame,  bg="orange", text= "+", font=("Arial", 20), command=lambda: item.add_factory(self)).grid(row=0, column=1)
        tk.Button(current_frame, bg="orange", text="-", font=("Arial", 20), command=lambda: item.remove_factory(self)).grid(row=0, column=2)
        tk.Label(current_frame, bg="white", text=f"   {item.building_percentage}%", font=("Arial", 14)).grid(row=0, column=3)





    def create_label_column(self, master, frame_height, columns, value_array, label_height, label_with, text_size, columns_amount):
        current_frame = tk.Frame(master, bg="white", borderwidth=2, relief="solid", height=frame_height - 50, width=1199 / columns_amount)
        current_frame.grid_propagate(False)
        current_frame.grid(row=0, column=columns)
        if(value_array[0] == "L"):

            for index, value in enumerate(value_array[1]):
                self.create_label(index, value, current_frame, label_height, label_with, text_size)
        elif(value_array[0] == "B"):
            for index, value in enumerate(value_array[1]):
                self.create_button(index, value, current_frame, label_height, label_with, text_size)
            pass
        elif(value_array[0] == "E"):
            for index, value in enumerate(value_array[1]):
                self.create_entry(index, value, current_frame, label_height, label_with, text_size)
            pass

    def create_label(self, row, value, master, label_height, label_with, text_size):
        if(row == 0):
            master.grid_columnconfigure(row, weight=1)
           
            player_header = tk.Label(master, bg="white", borderwidth=2, relief="solid", width=50, height=2, font=("Arial", text_size), text=value)
            player_header.grid(row=row, column=0, )
        else:
            master.grid_columnconfigure(row, weight=1)
            master.grid_rowconfigure(row, weight=1)
            player_label = tk.Label(master, bg="white", font=("Arial", text_size), text=value)               
            player_label.grid(row=row, column=0)
    
    
    
    def create_button(self, row, value, master, label_height, label_with, text_size):
        if(row == 0):
            master.grid_columnconfigure(row, weight=1)
            
            player_header = tk.Label(master, bg="white", borderwidth=2, relief="solid", width=50, height=2, font=("Arial", text_size), text=value)
            player_header.grid(row=row, column=0)
        else:
            master.grid_columnconfigure(row, weight=1)
            master.grid_rowconfigure(row, weight=1)
            player_button = tk.Button(master, bg="orange",  font=("Arial", text_size), text="Build", command=value)
            player_button.grid(row=row, column=0)
    

    def create_entry(self, row, value, master, label_height, label_with, text_size):
        if(row == 0):
            master.grid_columnconfigure(row, weight=1)
           
            player_header = tk.Label(master, bg="white", borderwidth=2, relief="solid", width=50, height=2, font=("Arial", text_size), text=value)
            player_header.grid(row=row, column=0)
        else:
            master.grid_columnconfigure(row, weight=1)
            master.grid_rowconfigure(row, weight=1)
            player_entry = tk.Entry(master, bg="white")
            player_entry.grid(row=row, column=0)
            self.planet.entry_value[row - 1] = player_entry






















#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                                                 side bar











        #create the side bar for planets
    def create_planet_side_bar(self, master):
        self.button_list = []
        self.planet_sidebar_frame = tk.Frame(master, bg="white")
        
        

        #stats button
        self.stats_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="Mining stats", width=15, command=lambda:self.mining_stats_page())
        self.button_list.append(self.stats_button)

        #build button
        self.build_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="Build", width=15, command=lambda:self.buidling_stats_page())
        self.button_list.append(self.build_button)
        
                
        self.build_order_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="Building orders", width=15, command=lambda:self.building_order_page())
        self.button_list.append(self.build_order_button)

        #Technologies button
        self.Technologies_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="Technologies", width=15)
        self.button_list.append(self.Technologies_button)

        #ship button
        self.ship_button = btn(self.planet_sidebar_frame, background_coller="orange", text_add="Ship_build", width=15)
        self.button_list.append(self.ship_button)
        

        for index, buttons in enumerate(self.button_list):
           buttons.grid(row=index, column=0, pady=20)
        
        self.planet_sidebar_frame.grid(row=0, column=0, padx=15)
        return self.planet_sidebar_frame
        






#_________________________________________________________________________________________________________________________________________________________________________________________________________________________
                                                                                            #Extra small methods

    def object_price_converter(self, price_array):
        return_string = f""
        for key in price_array:
            return_string += f"{key}: {price_array[key]}\n"

        return return_string



    def Check_for_main_frame(self):
        if hasattr(self, "current_main_frame"):
            self.current_main_frame.destroy()
        




    def destroy(self):
        self.main_planet_frame.destroy()


    def on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")











    

    def create_popup_screen(self, popup_text):
        try:
            
            popup_root =tk.Tk()
            popup_root.geometry("350x50")
            popup_root.config(bg="white")
            win_x, win_y = popup_root.winfo_pointerxy()
            popup_root.geometry(f"+{win_x}+{win_y}")
            tk.Label(popup_root, text=popup_text, font=("Arial", 25), bg="white").pack()
            popup_root.after(500, popup_root.destroy)
            popup_root.mainloop()


            
        except NameError:
            print(f"popup screen not working {NameError}")




