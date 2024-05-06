from modules import *

# Constants
SETTINGS = {
    "border_color": "#88aa77",
    "border_width": 1,
    "border_radius": 4,
    "background_color": "#111",
    "font_color": "#88aa77",
    "font_family": ['JetBrains Mono', "unionagrochem", "Poppins"],
    "percentage_color": "#88aa77",
    "percentage_background": "#666"
}

MONTHS = ["tmp", "January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

class Statistics(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master, **SETTINGS)
        self.startup_load()

    def close_panel(self):
        self.place_forget()
        self.close_btn.place_forget()

    def show_panel(self):
        self.close_btn.place(relx=0.83, rely=0.18, relwidth=0.05)
        self.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)

    def create_date_stats(self, date, details):
        frame = ctk.CTkFrame(self)
        frame.pack(fill="x")

        date_arr = date.split("-")
        month_name = MONTHS[int(date_arr[1])].upper()
        date_text = f"DATE: {date_arr[2]}, {month_name} {date_arr[0]}"
        self.date = ctk.CTkLabel(frame, text=date_text, anchor="w", font=(SETTINGS["font_family"][0], 13))
        self.date.pack(side="left", fill="x", padx=2)

        # Assuming 'target' label is meant to be dynamic
        self.target = ctk.CTkLabel(frame, text="DAILY CHALLENGE: 100%", anchor="w", font=(SETTINGS["font_family"][0], 13))
        self.target.pack(side="right", fill="x", padx=2)

        label_frames = [ctk.CTkFrame(frame) for _ in range(5)]
        for lf in label_frames:
            lf.pack(fill="x", expand=True, side="left")

        labels_info = [
            ("LESSON", 150),
            ("CATEGORY", 130),
            ("FROM", 70),
            ("TO", 70),
            ("DURATION", 40)
        ]

        for info, lf in zip(labels_info, label_frames):
            label_text, width = info
            label = ctk.CTkLabel(lf, text=label_text, text_color="#201", fg_color=SETTINGS["font_color"], font=(SETTINGS["font_family"][0], 13), width=width)
            label.pack(padx=1, fill="x")

        is_red = False
        for start, contents in details.items():
            color = "blue" if is_red else "purple"
            self.update_stats(label_frames, contents, color)
            is_red = not is_red

    def update_stats(self, label_frames, contents, color):
        for lf in label_frames:
            label = ctk.CTkLabel(lf, text=contents.get(lf.winfo_children()[0]["text"].lower(), ""), fg_color=color, font=(SETTINGS["font_family"][0], 13), width=lf.winfo_children()[0]["width"])
            label.pack(fill="x", padx=1)
            label.propagate(flag=False)

    def startup_load(self):
        try:
            with open("./SaveFiles/Stats.json", "r") as file:
                stats_dict = json.load(file)
                for date, details in stats_dict.items():
                    self.create_date_stats(date, details)
        except FileNotFoundError:
            print("Stats.json file not found.")
