import tkinter as tk



def button_creation(master, text_add="blanck", font_size=15, font_type="Arial"):
    btn = tk.Button(master, text=text_add, font=(font_type, font_size), bg="white", padx=15, pady=15)
    return btn



def create_top_bar(master):
    frame = tk.Frame(master, bg="white")
    

    for row in range(2):
        for col in range(6):
            frame.grid_columnconfigure(col , weight=1)
            btn = button_creation(frame)
            
            btn.grid(row=row, column=col, sticky="news")
    return frame


def create_side_bar(master):
    frame = tk.Frame(master, bg="green")


    for row in range(6):
        btn = button_creation(frame)