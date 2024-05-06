from modules import *

border_color = "#88aa77"
border_width = 1
border_radius = 4
Settings_background = "#111"
font_color = border_color
font_family = ['JetBrains Mono', "unionagrochem", "Poppins"]
percentage_color = border_color
percentage_background = "#666"

class Statistics(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=Settings_background, border_width=border_width, corner_radius=border_radius, border_color=border_color)
        self.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)
        
        self.create_date_stats()

    def create_date_stats(self):
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="x")
        
        date_frame = ctk.CTkFrame(frame)
        date_frame.pack(fill="x")
        self.date = ctk.CTkLabel(date_frame, text="DATE: 4, OCTOBER 2004", anchor="w",font=(font_family[0], 13))
        self.date.pack(side="left", expand=True)
        self.target = ctk.CTkLabel(date_frame, text="DAILY CHALLENGE: 100%",anchor="w", font=(font_family[0], 13))
        self.target.pack(side="right", expand=True)
        
        self.name_frame = ctk.CTkFrame(frame,corner_radius=0,width=160)
        self.category_frame = ctk.CTkFrame(frame,corner_radius=0, width=130)
        self.from_frame = ctk.CTkFrame(frame,corner_radius=0, width=80)
        self.to_frame = ctk.CTkFrame(frame,corner_radius=0, width=80)
        self.duration_frame = ctk.CTkFrame(frame,corner_radius=0,)
        
        self.name_frame.pack(side="left", expand=True, fill="both")
        self.category_frame.pack(side="left", expand=True, fill="both")
        self.from_frame.pack(side="left", expand=True, fill="both")
        self.to_frame.pack(side="left", expand=True, fill="both")
        self.duration_frame.pack(side="left", expand=True, fill="both")
        
        ctk.CTkLabel(self.name_frame, text="LESSON", font=(font_family[0], 13)).pack(fill="x", expand=True)
        ctk.CTkLabel(self.category_frame, text="CATEGORY", font=(font_family[0], 13)).pack(fill="x", expand=True)
        ctk.CTkLabel(self.from_frame, text="FROM", font=(font_family[0], 13)).pack(fill="x", expand=True)
        ctk.CTkLabel(self.to_frame, text="TO", font=(font_family[0], 13)).pack(fill="x", expand=True)
        ctk.CTkLabel(self.duration_frame, text="DURATION", font=(font_family[0], 13)).pack(fill="x", expand=True)
        
    def update_stats(self):
        
        
