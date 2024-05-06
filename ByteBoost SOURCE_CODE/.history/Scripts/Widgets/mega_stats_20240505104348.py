from modules import *


# Constants
border_color = "#88aa77"
border_width = 1
border_radius = 4
settings_background = "#111"
font_family = ['JetBrains Mono', "unionagrochem", "Poppins"]

class Statistics(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=settings_background, border_width=border_width, corner_radius=border_radius, border_color=border_color)
        self.startup_load()
        self.close_btn = self.create_button("CLOSE", self.close_panel, corner_radius=0)

    def close_panel(self):
        self.place_forget()
        self.close_btn.place_forget()
            
    def show_panel(self):
        self.close_btn.place(relx=0.83, rely=0.18, relwidth=0.05)
        self.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)

    def create_button(self, text, command, **kwargs):
        return ctk.CTkButton(self.master, text=text, font=(font_family[0], 13), command=command, **kwargs)

    def create_date_stats(self, date, details):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x")
        frame.pack_propagate(flag=True)
        date_arr = date.split("-")
        month = ["tmp","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        date_label = f"DATE: {date_arr[2]}, {month[int(date_arr[1])].upper()} {date_arr[0]}"
        self.create_label(frame, date_label, font_color=border_color)
        self.create_label(frame, "DAILY CHALLENGE: 100%", side="right")

        for start, contents in details.items():
            color = "blue" if start % 2 == 0 else "purple"
            self.update_stats(frame, contents["lesson"], contents["Category"], start, contents["TO"], contents["Duration"], color)

    def update_stats(self, frame, name, category, start, to, duration, color):
        labels = ["LESSON", "CATEGORY", "FROM", "TO", "DURATION"]
        for i, text in enumerate([name, category, start, to, duration]):
            self.create_label(getattr(self, labels[i].lower() + "_frame"), text)

    def create_label(self, frame, text, side="left", **kwargs):
        label = ctk.CTkLabel(frame, text=text, anchor="w", font=(font_family[0], 13))
        label.pack(side=side, fill="x", padx=2)
        label.propagate(flag=False)

    def startup_load(self):
        with open("./SaveFiles/Stats.json", "r") as file:
            stats_dict = json.load(file)
            for date, details in stats_dict.items():
                self.create_date_stats(date, details)
