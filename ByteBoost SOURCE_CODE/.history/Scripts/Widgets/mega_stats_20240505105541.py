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
        self.MONTH_NAMES = ["tmp", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.FONT_FAMILY = ("Arial", 13)
        self.FONT_COLOR = "#201"
        self.startup_load()
        
        def close_panel(self):
            self.place_forget()
            self.close_btn.place_forget()
            
        self.close_btn = ctk.CTkButton(master, text="CLOSE",corner_radius=0, font=(font_family[0], 13), command=lambda: close_panel(self))
        
    def show_panel(self):
        self.close_btn.place(relx=0.83, rely=0.18, relwidth=0.05)
        self.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)  
        
    def create_date_stats(self, date, details):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x")

        date_arr = date.split("-")
        month_name = self.MONTH_NAMES[int(date_arr[1])]

        date_frame = ctk.CTkFrame(frame)
        date_frame.pack(fill="x")

        self.date = ctk.CTkLabel(date_frame, text=f"DATE: {date_arr[2]}, {month_name.upper()} {date_arr[0]}", anchor="w", font=self.FONT_FAMILY)
        self.date.pack(side="left", fill="x", padx=2)

        self.target = ctk.CTkLabel(date_frame, text="DAILY CHALLENGE: 100%", anchor="w", font=self.FONT_FAMILY)
        self.target.pack(side="right", fill="x", padx=2)

        labels_frame = ctk.CTkFrame(frame)
        labels_frame.pack(fill="x")

        labels = ["LESSON", "CATEGORY", "FROM", "TO", "DURATION"]
        widths = [150, 130, 70, 70, 40]
        frames = [self.name_frame, self.category_frame, self.from_frame, self.to_frame, self.duration_frame]

        for label_text, width, frame in zip(labels, widths, frames):
            label = ctk.CTkLabel(frame, text=label_text, text_color=self.FONT_COLOR, fg_color=self.FONT_COLOR, font=self.FONT_FAMILY, width=width)
            label.pack(padx=1, fill="x")
            frame.pack(fill="x", expand=True, side="left")
            frame.propagate(flag=False)

        is_red = False
        for start, contents in details.items():
            color = "blue" if is_red else "purple"
            is_red = not is_red
            self.update_stats(contents["lesson"], contents["Category"], start, contents["TO"], contents["Duration"], color)

    def update_stats(self, name, category, start, to, duration, color):
        frames = [self.name_frame, self.category_frame, self.from_frame, self.to_frame, self.duration_frame]
        texts = [name, category, start, to, duration]

        for frame, text in zip(frames, texts):
            label = ctk.CTkLabel(frame, fg_color=color, text=text, font=self.FONT_FAMILY, width=frame.winfo_reqwidth())
            label.pack(fill="x", padx=1)
            frame.propagate(flag=False)

    def startup_load(self):
        with open("./SaveFiles/Stats.json", "r") as file:
            stats_dict = json.load(file)
            for date, details in stats_dict.items():
                self.create_date_stats(date, details)
        
        
