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
        frame = ctk.CTkFrame(self)
        frame.place(relx=0.01, rely=0.01, relwidth=(1/4), relheight=0.98)
        self.create_buttons(frame, text="THEME")
        self.create_buttons(frame, text="LESSONS")
        self.create_buttons(frame, text="FILE SYS")
        self.create_buttons(frame, text="RESET")
        
        Lessons_panel(self)
        
    def create_buttons(self, master, text):
        self.theme_btn = ctk.CTkButton(master,corner_radius=0, text=text, font=(font_family[0], 20))
        self.theme_btn.pack(expand=True, fill="both", pady=1)
        
        
class Lessons_panel():
    def __init__(self, master):
        main_frame = ctk.CTkFrame(master, corner_radius=0)
        main_frame.place(relx=(1/4), rely=0.01, relwidth=(3/4)-0.01, relheight=0.98)
        
        #ADD menu
        add_frame = ctk.CTkFrame(main_frame,corner_radius=0, border_color=border_color, border_width=border_width)
        add_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.49)
        
        ctk.CTkLabel(add_frame, text=f"{("Wanna Add a new Lesson to track").title()}", font=(font_family[2], 13)).place(relx=0.01, rely=0.01)
        
        ctk.CTkLabel(add_frame, text=f"{("Category").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.15)
        category = ctk.CTkComboBox(add_frame, corner_radius=0)
        category.place(relx=0.21, rely=0.15)
        
        ctk.CTkLabel(add_frame, text=f"{("New category").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.3)
        
        
        
        save_btn = ctk.CTkButton(add_frame, text="SAVE",corner_radius=0,font=(font_family[0], 12))
        save_btn.place(anchor="ne", relx=0.99, rely=0.82, relwidth=0.1)
        
         #Remove menu
        del_frame = ctk.CTkFrame(main_frame, corner_radius=0,border_color=border_color, border_width=border_width)
        del_frame.place(relx=0.01, rely=0.51, relwidth=0.98, relheight=0.49)
        
        save_btn = ctk.CTkButton(del_frame, text="SAVE",corner_radius=0,font=(font_family[0], 12))
        save_btn.place(anchor="ne", relx=0.99, rely=0.82, relwidth=0.1)