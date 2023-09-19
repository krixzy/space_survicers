import tkinter as tk

def test_command():
    print("planets_in_systems")

def button_creation(master, width=True, text_add="blanck", font_size=15, font_type="Arial", background_coller="white", height=2, command=test_command):
    if(width == True):
        btn = tk.Button(master, text=text_add, font=(font_type, font_size), bg=background_coller,  padx=15, pady=15, command=command, justify="center")
        return btn
    
    btn = tk.Button(master, text=text_add, font=(font_type, font_size), bg=background_coller,  padx=15, pady=15, width=width, height=height, command=command, justify="center")
    return btn


def standart_text(master, text):
    label = tk.Label(master, text=text, bg="white", font=("Arial", 14))
    return label






def create_top_bar(master, main_ui_class):
    frame = tk.Frame(master, bg="white")
    button_list = []
    planet_button = button_creation(frame, text_add="Planets", command=main_ui_class.planets_in_systems, width=21)
    button_list.append(planet_button)
    planet_button.grid(row=0, column=0, sticky="news")
    
    planet_button2 = button_creation(frame, text_add="Planets", command=main_ui_class.planets_in_systems, width=21)
    button_list.append(planet_button2)
    planet_button2.grid(row=0, column=1, sticky="news")
    
    planet_button3 = button_creation(frame, text_add="Planets", command=main_ui_class.planets_in_systems, width=21)
    button_list.append(planet_button3)
    planet_button3.grid(row=0, column=2, sticky="news")
    
    planet_button4 = button_creation(frame, text_add="Planets", command=main_ui_class.planets_in_systems, width=21)
    button_list.append(planet_button4)
    planet_button4.grid(row=0, column=3, sticky="news")
    
    planet_button5 = button_creation(frame, text_add="Planets", command=main_ui_class.planets_in_systems, width=21)
    button_list.append(planet_button5)
    planet_button5.grid(row=0, column=4, sticky="news")
    
    planet_button6 = button_creation(frame, text_add="Planets", command=main_ui_class.planets_in_systems, width=21)
    button_list.append(planet_button6)
    planet_button6.grid(row=0, column=5, sticky="news")
    
    planet_button7 = button_creation(frame, text_add="Planets", command=main_ui_class.planets_in_systems, width=21)
    button_list.append(planet_button7)
    planet_button7.grid(row=1, column=2, sticky="news")
    
    planet_button8 = button_creation(frame, text_add="Planets", command=main_ui_class.planets_in_systems, width=21)
    button_list.append(planet_button8)
    planet_button8.grid(row=1, column=0, sticky="news")
    
    planet_button9 = button_creation(frame, text_add="Planets", command=main_ui_class.planets_in_systems, width=21)
    button_list.append(planet_button9)
    planet_button9.grid(row=1, column=1, sticky="news")
    
    planet_button10 = button_creation(frame, text_add="Planets", command=main_ui_class.planets_in_systems, width=21)
    button_list.append(planet_button10)
    planet_button10.grid(row=1, column=3, sticky="news")
    
    planet_button11 = button_creation(frame, text_add="Planets", command=main_ui_class.planets_in_systems, width=21)
    button_list.append(planet_button11)
    planet_button11.grid(row=1, column=5, sticky="news")
    
    planet_button12 = button_creation(frame, text_add="Planets", command=main_ui_class.planets_in_systems, width=21)
    button_list.append(planet_button12)
    planet_button12.grid(row=1, column=4, sticky="news")


    for index in range(len(button_list)):
        frame.columnconfigure(index, weight=1)
            
    return frame


