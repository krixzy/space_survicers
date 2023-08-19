import tkinter as tk
from tkinter_function import button_creation as btn
from tkinter_function import create_top_bar as top_bar


class planet_ui:
    def __init__(self):


        # create screen for planets
        self.root = tk.Tk()
        self.root.geometry("1700x950")
        self.root.config(bg="black")

        #insertin the top bar of button
        self.top_frame = top_bar(self.root)
        self.top_frame.pack(fill="x", pady= 40, padx= 40)
        self.root.mainloop()
    


    def create_side_bar(self, master):
        pass
planet_ui()