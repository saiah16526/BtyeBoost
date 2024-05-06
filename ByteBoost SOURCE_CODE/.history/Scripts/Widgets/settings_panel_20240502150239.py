from modules import *

border_color = "#88aa77"
border_width = 1
border_radius = 4
Panel_background = "#111"
font_color = border_color
font_family = ['JetBrains Mono', "unionagrochem"]
percentage_color = border_color
percentage_background = "#666"

class Settings(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)