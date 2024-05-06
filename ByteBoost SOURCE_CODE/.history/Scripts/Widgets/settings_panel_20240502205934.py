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
        
        ctk.CTkLabel(self, text="Language", text_color=font_color, font=(font_family[2], 15)).place(relx=0.01, rely=0.01)
        ctk.CTkComboBox(self, values=["English", "French", "Kiswahili"]).place(relx=0.2, rely=0.01)