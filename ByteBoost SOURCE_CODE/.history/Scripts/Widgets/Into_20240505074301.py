from modules import *

border_color = "#88aa77"
Intro_background = "#111"
font_color = border_color
font_family = ['JetBrains Mono', "unionagrochem", "Poppins"]

class Into_page():
    def __init__(self, master):
        # Create a frame to display the introductory page
        intro_frame = ctk.CTkFrame(master, fg_color=Intro_background)  # Adjust fg_color as needed
        intro_frame.place(relx=0.03, rely=0.6, relwidth=0.3, relheight=0.4, anchor="nw")

        # Display date and time
        datetime_display = DateTimeFrame(intro_frame)

        # Display quotes
        quotes_display = QuotesFrame(intro_frame)
        

class DateTimeFrame():
    def __init__(self, master):
        self.create_widgets(master)

    def create_widgets(self, parent):
        self.day_label = ctk.CTkLabel(parent, text_color=font_color, font=(font_family[0], 95))
        self.day_label.place(relx=0.07, rely=0.01, anchor="nw")

        self.weekday_label = ctk.CTkLabel(parent, text_color=font_color, font=(font_family[0], 20))
        self.weekday_label.place(relx=0.5, rely=0.12)

        self.time_label = ctk.CTkLabel(parent, text_color=font_color, font=(font_family[0], 35))
        self.time_label.place(relx=0.5, rely=0.23)

        self.update_time(parent)

    def update_time(self, parent):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime('%H:%M')
        self.time_label.configure(text=formatted_time)

        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        current_weekday = weekdays[current_time.weekday()].upper()
        self.weekday_label.configure(text=current_weekday)

        current_day = str(current_time.day)
        formatted_day = f"0{current_day}" if current_time.day < 10 else current_day
        self.day_label.configure(text=formatted_day)

        parent.after(1000, self.update_time)

class QuotesFrame():
    def __init__(self, master):
        self.create_widgets(master)

    def create_widgets(self, parent):
        title_label = ctk.CTkLabel(parent, text_color=font_color, text="Dijkstra's Law", font=(font_family[2], 20))
        title_label.place(relx=0.07, rely=0.5)

        quote_label = ctk.CTkLabel(parent, text_color=font_color, text="Picking up a new game is like learning a new language: you fumble with the controls and hope you don't embarrass yourself in front of NPCs", justify="left", font=(font_family[2], 12), wraplength=250)
        quote_label.place(relx=0.05, rely=0.62)
