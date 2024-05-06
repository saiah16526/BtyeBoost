from modules import *

border_color = "#88aa77"
border_width = 1
border_radius = 4
Settings_background = border_color
font_color = border_color
font_family = ['JetBrains Mono', "unionagrochem"]
percentage_color = border_color
percentage_background = "#666"

class Settings(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=Settings_background)
        self.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)