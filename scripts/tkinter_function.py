import tkinter as tk

def test_command():
    print("test")

def button_creation(master, width=True, text_add="blanck", font_size=15, font_type="Arial", background_coller="white", height=2, command=test_command):
    if(width == True):
        btn = tk.Button(master, text=text_add, font=(font_type, font_size), bg=background_coller,  padx=15, pady=15, command=command)
        return btn
    
    btn = tk.Button(master, text=text_add, font=(font_type, font_size), bg=background_coller,  padx=15, pady=15, width=width, height=height, command=command)
    return btn


def standart_text(master, text):
    label = tk.Label(master, text=text, bg="white", font=("Arial", 14))
    return label
def create_top_bar(master):
    frame = tk.Frame(master, bg="white")
    

    for row in range(2):
        for col in range(6):
            frame.grid_columnconfigure(col , weight=1)
            btn = button_creation(frame)
            
            btn.grid(row=row, column=col, sticky="news")
    return frame


