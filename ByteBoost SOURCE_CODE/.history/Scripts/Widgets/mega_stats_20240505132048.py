from modules import *

border_color = "#88aa77"
border_width = 1
border_radius = 4
Settings_background = "#1f1"
font_color = border_color
font_family = ['JetBrains Mono', "unionagrochem", "Poppins"]
percentage_color = border_color
percentage_background = "#666"

class Statistics(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=Settings_background, border_width=border_width, corner_radius=border_radius, border_color=border_color)
        self.startup_load()
        def close_panel(self):
            self.place_forget()
            self.close_btn.place_forget()
            
        close_img = ImageTk.PhotoImage(Image.open("./Images/Icons/close.png").resize((30, 30)))
        self.close_btn = ctk.CTkButton(master,fg_color=border_color ,height=10,text="",image=close_img,corner_radius=3, font=(font_family[0], 13), command=lambda: close_panel(self))
        
    def show_panel(self):
        self.close_btn.place(relx=0.83, rely=0.18, relwidth=0.045)
        self.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)
            
            
    def create_date_stats(self, date, details):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(fill="x")
        frame.pack_propagate(flag=True)
        date_arr = (date.split("-"))
        months = ["tmp","january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        
        date_frame = ctk.CTkFrame(frame)
        date_frame.pack(fill="x")
        self.date = ctk.CTkLabel(date_frame, text=f"DATE: {date_arr[2]}, {(months[int(date_arr[1])]).upper()} {date_arr[0]}", anchor="w",font=(font_family[0], 13))
        self.date.pack(side="left", fill="x", padx=2)
        self.target = ctk.CTkLabel(date_frame, text="DAILY CHALLENGE: 100%",anchor="w", font=(font_family[0], 13))
        self.target.pack(side="right", fill="x", padx=2)
        
        self.name_frame = ctk.CTkFrame(frame,fg_color="transparent",corner_radius=0)
        self.category_frame = ctk.CTkFrame(frame,fg_color="transparent",corner_radius=0)
        self.from_frame = ctk.CTkFrame(frame,fg_color="transparent",corner_radius=0)
        self.to_frame = ctk.CTkFrame(frame,fg_color="transparent",corner_radius=0)
        self.duration_frame = ctk.CTkFrame(frame,fg_color="transparent",corner_radius=0)
        
        self.name_frame.pack(fill="x",expand=True,side="left")
        self.category_frame.pack(fill="x",expand=True,side="left")
        self.from_frame.pack(fill="x",expand=True,side="left")
        self.to_frame.pack(fill="x",expand=True,side="left")
        self.duration_frame.pack(fill="x",expand=True,side="left")
 
        
        def update_stats(labels_data, font_color="#201", font_family=None):
            font_style = (font_family[0], 13) if font_family else None
            print(font_style)
            for frame, text, width in labels_data:
                label = ctk.CTkLabel(
                    master=frame,
                    fg_color=font_color,
                    text_color="#201",
                    text=text,
                    font=font_style,
                    width=width
                )
                label.pack(padx=1, fill="x")
                label.propagate(flag=False)

        # Usage:
        labels_data = [
            (self.name_frame, "LESSON", 150),
            (self.category_frame, "CATEGORY", 130),
            (self.from_frame, "FROM", 70),
            (self.to_frame, "TO", 70),
            (self.duration_frame, "DURATION", 40)
        ]

        update_stats(labels_data, font_family=font_family, font_color=font_color)

            
        color_cycle = itertools.cycle(["blue", "purple"])
        for start , contents in details.items():
            color = next(color_cycle)  # Get the next color from the cycle
            self.update_stats(contents["lesson"], contents["Category"], start, contents["TO"], contents["Duration"], color)
    def update_stats(self, name, category, start, to, duration, color):
        frame_info = [
            (self.name_frame, name, 150),
            (self.category_frame, category, 130),
            (self.from_frame, start, 70),
            (self.to_frame, to, 70),
            (self.duration_frame, duration, 40)
        ]

        font_style = (font_family[0], 13)

        for frame, text, width in frame_info:
            label = ctk.CTkLabel(
                master=frame,
                fg_color=color,
                text=text,
                font=font_style,
                width=width
            )
            label.pack(fill="x", padx=1)
            label.propagate(flag=False)

            
    def startup_load(self):
        with open("./SaveFiles/Stats.json", "r") as file:
            stats_dict = json.load(file)
            for date, details in stats_dict.items():
                self.create_date_stats(date, details)
        
        
