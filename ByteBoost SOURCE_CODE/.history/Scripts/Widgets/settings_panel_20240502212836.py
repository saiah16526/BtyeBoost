from modules import *

border_color = "#88aa77"
border_width = 1
border_radius = 4
Settings_background = "#111"
font_color = border_color
font_family = ['JetBrains Mono', "unionagrochem", "Poppins"]
percentage_color = border_color
percentage_background = "#666"

class Settings(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=Settings_background, border_width=border_width, corner_radius=border_radius, border_color=border_color)
        self.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)
        
        ctk.CTkLabel(self, text="THEME :", text_color=font_color, font=(font_family[0], 18)).place(relx=0.01, rely=0.01)
        Input(self, "BACKGROUND:", pos=(0.01, 0.1))
        Input(self, "TEXT_COLOR:", pos=(0.35, 0.1))
        Input(self, "BUTTONS:", pos=(0.69, 0.1), offset=0.04)
        Input(self, "PROGRESS_THEME:", pos=(0.24, 0.19), offset=(-0.05))
        
class Input():
    def __init__(self, master, text, pos, offset = 0):
        self.x = pos[0]
        self.y = pos[1]
        label_input = ctk.CTkLabel(master, text_color=font_color, text=text, font=(font_family[0], 14), anchor="w")
        label_input.place(relx=self.x, rely=self.y)

        self.entry = ctk.StringVar()
        ctk.CTkEntry(master,textvariable=self.entry ,width=90,height=20,border_width=0,corner_radius=3).place(relx=self.x + 0.165 - offset, rely=self.y + 0.01, anchor="nw")