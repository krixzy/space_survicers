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
            ["L", ["Current amount",self.planet.miners, self.planet.total_factory, self.planet.science_center, self.planet.space_port]],
            ["L", ["Building power cost", gs["miners_stats"]["miners_building_power_cost"], gs["factory_stats"]["factory_building_power_cost"], gs["science_center_stats"]["science_center_building_power_cost"], gs["space_port_stats"]["space_port_building_power_cost"]]],
            ["L", ["Price", self.object_price_converter(gs["miners_stats"]["miners_price"]), self.object_price_converter(gs["factory_stats"]["factory_price"]),self.object_price_converter(gs["science_center_stats"]["science_center_price"]),self.object_price_converter(gs["space_port_stats"]["space_port_price"])]],
            ["E", ["Order_amount", " ", " ", " ", " "]],
            ["B", ["Build", lambda:self.planet.create_building_order("miners", self.planet.entry_value[0], self), lambda: self.planet.create_building_order("factory", self.planet.entry_value[1], self), lambda: self.planet.create_building_order("science_center", self.planet.entry_value[2], self), lambda: self.planet.create_building_order("space_port", self.planet.entry_value[3], self)]]
        ]
        self.Check_for_main_frame()
        self.current_frame = "building_frame"
        self.build_current_main_frame(planet_building_info_array, f"Free factorys: {self.planet.factory}", f"Current tech bonus: 0", f"building power pr factory {gs['factory_stats']['factory_building_power']}", text_size=14)


    def building_order_page(self):
        self.Check_for_main_frame()
        self.current_frame = "building_order_frame"
        self.build_current_main_frame( self.planet.building_orders,f"Free factorys: {self.planet.factory}", f"Current tech bonus: 0", f"building power pr factory {gs['factory_stats']['factory_building_power']}", text_size=14, type="row")



    def ship_building_page(self):
        self.Check_for_main_frame()
        self.current_frame = "ship_building_frame"
        self.build_current_main_frame(["test, test"], f"Free space ports: {self.planet.space_port}", f"Current tech bonus: 0", f"building power pr space port: {gs['space_port_stats']['space_port_building_power']}", type="build_ship" )


    def ship_design_page(self):
        self.Check_for_main_frame()
        self.current_frame = "ship_design_frame"
        design_array = ["", "Design ship"]
        self.build_current_main_frame(["Design options", lambda: self.design_page_popup(design_array[1])], f"Free space ports: {self.planet.space_port}", f"Current tech bonus: 0", f"building power pr space port: {gs['space_port_stats']['space_port_building_power']}", type="design_ship", design_array = design_array)

#___________________________________________________________________________________________________________________________________________________________________________________________________________________________
                                                                                #current main frame builder
                                                                                


    def build_current_main_frame(self, array_of_values, building_type, building_tech, building_power, text_size = 14, type = "cul", design_array = None):
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
            self.create_canves(frame_height, self.current_main_frame)
            for index, array in enumerate(array_of_values):
                self.create_label_column(self.resource_frame, frame_height, index, array, text_size, len(array_of_values))
        
        if(type == "row"):
            frame_height = len(array_of_values) * 50
            if(frame_height > 0):
                self.create_canves(frame_height, self.current_main_frame)
                for index, item in enumerate(array_of_values):
                    self.create_label_row(self.resource_frame, frame_height, item, index)
            else:
                pass
        if(type == "design_ship"):
            self.create_canves(600, self.current_main_frame)
            current_frame = tk.Frame(self.resource_frame, bg="white", borderwidth=2, relief="solid", height=550, width=1199 / 6)
            current_frame.grid_propagate(False)
            current_frame.grid(row=0, column=0)
            for index, item in enumerate(array_of_values):
                self.create_button(index, item, current_frame, text_size, design_array[index]   )


        
        


    def create_canves(self, frame_height, master):
        self.canvas = tk.Canvas(master, height=600, width=1200)
        self.canvas.grid(row=2, column=0, columnspan=6)
        self.scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
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





    def create_label_column(self, master, frame_height, columns, value_array, text_size, columns_amount):
        current_frame = tk.Frame(master, bg="white", borderwidth=2, relief="solid", height=frame_height - 50, width=1199 / columns_amount)
        current_frame.grid_propagate(False)
        current_frame.grid(row=0, column=columns)
        if(value_array[0] == "L"):

            for index, value in enumerate(value_array[1]):
                self.create_label(index, value, current_frame, text_size)
        elif(value_array[0] == "B"):
            for index, value in enumerate(value_array[1]):
                self.create_button(index, value, current_frame, text_size)
            pass
        elif(value_array[0] == "E"):
            for index, value in enumerate(value_array[1]):
                self.create_entry(index, value, current_frame, text_size)
            pass

    def create_label(self, row, value, master, text_size):
        if(row == 0):
            master.grid_columnconfigure(row, weight=1)
           
            player_header = tk.Label(master, bg="white", borderwidth=2, relief="solid", width=50, height=2, font=("Arial", text_size), text=value)
            player_header.grid(row=row, column=0, )
        else:
            master.grid_columnconfigure(row, weight=1)
            master.grid_rowconfigure(row, weight=1)
            player_label = tk.Label(master, bg="white", font=("Arial", text_size), text=value)               
            player_label.grid(row=row, column=0)
    
    
    
    def create_button(self, row, value, master, text_size, button_text="Build"):
        if(row == 0):
            master.grid_columnconfigure(row, weight=1)
            
            player_header = tk.Label(master, bg="white", borderwidth=2, relief="solid", width=50, height=2, font=("Arial", text_size), text=value)
            player_header.grid(row=row, column=0)
        else:
            master.grid_columnconfigure(row, weight=1)
            master.grid_rowconfigure(row, weight=1)
            player_button = tk.Button(master, bg="orange",  font=("Arial", text_size), text=button_text, command=value)
            player_button.grid(row=row, column=0)
    

    def create_entry(self, row, value, master, text_size):
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











#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                                               ship building frame



    def design_page_popup(self, page_name):
        current_design_page = tk.Tk( className=f"{page_name}")
        current_design_page.geometry("1100x800+200+100")
        current_design_page.config(bg="white")
        
       
        self.design_ship_page(current_design_page)
        current_design_page.mainloop()



    def design_ship_page(self, master):
        current_frame = tk.Frame(master, bg="white", width=1000, height=700)
        current_frame.grid_propagate(False)
        current_frame.columnconfigure(0, weight=1)
        current_frame.grid(row=0, column=0, padx=50, pady=50) 
        choose_engine_label = tk.Label(current_frame, bg="white", font=("Arial", 12), text= "Choose ship type")
        choose_engine_label.grid(row=0, column=0)
        ships_researched_list = self.check_if_researched(gs.get("ship_stats").get("ship_type"))
        ship_type_menu = self.dropdown_menu(current_frame, ships_researched_list, 1, 0)
        ship_type_menu.bind("<<ComboboxSelected>>", lambda event=None:self.design_ship_main_frame(current_frame, ship_type_menu.get()))




    

    def dropdown_menu(self, master, value, row, column):
        drop_down_menu =ttk.Combobox(master, values=value)
        drop_down_menu.grid(row=row, column=column)
        return drop_down_menu 
    

    def dropdown_menu_with_label(self, master, row, column, value, text):
        drop_down_frame = tk.Frame(master, bg="white")
        drop_down_label = tk.Label(drop_down_frame, bg="white", font=("Arial", 14), text=text)
        drop_down_label.pack()
        drop_down_menu =ttk.Combobox(drop_down_frame, values=value)
        drop_down_menu.pack()
        drop_down_frame.grid(row=row, column=column)
        drop_down_frame.bind("<<ComboboxSelected>>", lambda event=None:self.freighter_stats_frame(master, self.choose_engine_value.get(), self.choose_hull_value.get(), self.choose_fuel_tank_value.get(), self.cargo_capacity.get()))
        return drop_down_menu
    
    def entry_with_label(self, master, row, column, text):
        entry_frame = tk.Frame(master, bg="white")
        entry_label = tk.Label(entry_frame, bg="white", font=("Arial", 14), text=text)
        entry_label.pack()
        entry_menu =ttk.Entry(entry_frame)
        entry_menu.pack()
        entry_frame.grid(row=row, column=column)
        return entry_menu

    def design_ship_main_frame(self, master, type):
        design_main_frame = tk.Frame(master, bg="white", borderwidth=2, relief="solid", width=900, height=600)
        design_main_frame.grid_propagate(False)
        design_main_frame.grid(row=2, column=0)
        self.choose_engine_value = self.dropdown_menu_with_label(design_main_frame, 1, 0, self.check_if_researched(gs.get("engine_stats").get("engine_types")), "Engine")
        self.choose_hull_value = self.dropdown_menu_with_label(design_main_frame, 1, 1, self.check_if_researched(gs.get("ship_stats").get("hull_types")), "Ship hull")
        self.choose_fuel_tank_value = self.dropdown_menu_with_label(design_main_frame, 1, 2, self.check_if_researched(gs.get("fuel_tank_stats").get("fuel_types")), "Fuel tank")
        if(type == "freighter"):
            self.cargo_capacity =  self.entry_with_label(design_main_frame, 2, 0, "Cargo size")
            # refresh_button = btn(design_main_frame,background_color="orange", text_add="Refresh", command=lambda event=None:self.freighter_stats_frame(master, self.choose_engine_value.get(), self.choose_hull_value.get(), self.choose_fuel_tank_value.get(), self.cargo_capacity.get()) )
            self.freighter_stats_frame(design_main_frame, self.choose_engine_value.get(), self.choose_hull_value.get(), self.choose_fuel_tank_value.get(), self.cargo_capacity.get())
            
        if(type == "scout"):
          pass     




        column_amount_list = self.count_columns(design_main_frame.winfo_children())
        frame_label = tk.Label(design_main_frame, bg="white", font=("Arial", 20), text=type).grid(row=0, column=0, columnspan= len(column_amount_list))
        
        design_main_frame.columnconfigure(column_amount_list, weight=1)



    def check_if_researched(self, list):
        return_list = []
        for key in list:
            if(list[key].get("researched")):
                return_list.append(key)
        return return_list



#__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                                               freighter stats frame


    def freighter_stats_frame(self, master, engine_value, hull_value, fuel_tank_value, cargo_size):
        # column_span = self.count_columns(master.winfo_children())
        freighter_stats_frame = tk.Frame(master, bg="white").grid(row=3, column=1)






#___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                                                 side bar











        #create the side bar for planets
    def create_planet_side_bar(self, master):
        self.button_list = []
        self.planet_sidebar_frame = tk.Frame(master, bg="white")
        print()
        

        #stats button
        self.stats_button = btn(self.planet_sidebar_frame, background_color="orange", text_add="Mining stats", width=15, command=lambda:self.mining_stats_page())
        self.button_list.append(self.stats_button)

        #build button
        self.build_button = btn(self.planet_sidebar_frame, background_color="orange", text_add="Build", width=15, command=lambda:self.buidling_stats_page())
        self.button_list.append(self.build_button)
        
        # build order button        
        self.build_order_button = btn(self.planet_sidebar_frame, background_color="orange", text_add="Building orders", width=15, command=lambda:self.building_order_page())
        self.button_list.append(self.build_order_button)

        #Technologies button
        self.Technologies_button = btn(self.planet_sidebar_frame, background_color="orange", text_add="Technologies", width=15)
        self.button_list.append(self.Technologies_button)

        #ship build button
        self.ship_build_button = btn(self.planet_sidebar_frame, background_color="orange", text_add="Ship build", width=15, command=lambda:self.ship_building_page())
        self.button_list.append(self.ship_build_button)
        
        #ship designe button
        self.ship_design_button = btn(self.planet_sidebar_frame, background_color="orange", text_add="Ship design", width=15, command=lambda:self.ship_design_page())
        self.button_list.append(self.ship_design_button)
        

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


    def count_columns(self, childrien):
        highest_number = 0
        for value in childrien:
           if(value.grid_info().get("column") > highest_number):
               highest_number = value.grid_info().get("column")
        return [i for i in range(0, highest_number + 1)]

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




