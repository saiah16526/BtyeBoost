from modules import *


class Into_page():
    def __init__(self, master):
        self.SETTINGS = load_settings()
        # Create a frame to display the introductory page
        self.intro_frame = ctk.CTkFrame(master, fg_color=self.SETTINGS["BACKGROUND"])  # Adjust fg_color as needed
        self.intro_frame.place(relx=0.03, rely=0.6, relwidth=0.3, relheight=0.4, anchor="nw")

        # Display date and time
        datetime_display = DateTimeFrame(self.intro_frame)

        # Display quotes
        quotes_display = QuotesFrame(self.intro_frame)
        

class DateTimeFrame():
    def __init__(self, master):
        self.SETTINGS = load_settings()
        self.create_widgets(master)

    def create_widgets(self, parent):
        self.day_label = ctk.CTkLabel(parent, text_color=self.SETTINGS["BORDER_COLOR"], font=(self.SETTINGS["FONT_FAMILY"][0], 95))
        self.day_label.place(relx=0.07, rely=0.01, anchor="nw")

        self.weekday_label = ctk.CTkLabel(parent, text_color=self.SETTINGS["BORDER_COLOR"], font=(self.SETTINGS["FONT_FAMILY"][0], 20))
        self.weekday_label.place(relx=0.5, rely=0.12)

        self.time_label = ctk.CTkLabel(parent, text_color=self.SETTINGS["BORDER_COLOR"], font=(self.SETTINGS["FONT_FAMILY"][0], 35))
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

        parent.after(1000, lambda : self.update_time(parent))

class QuotesFrame():
    def __init__(self, master):
        self.SETTINGS = load_settings()
        self.create_widgets(master)

    def create_widgets(self, parent):
        title_label = ctk.CTkLabel(parent, text_color=self.SETTINGS["BORDER_COLOR"], text="Dijkstra's Law", font=(self.SETTINGS["FONT_FAMILY"][2], 20))
        title_label.place(relx=0.07, rely=0.5)

        quote_label = ctk.CTkLabel(parent, text_color=self.SETTINGS["BORDER_COLOR"], text="Picking up a new game is like learning a new language: you fumble with the controls and hope you don't embarrass yourself in front of NPCs", justify="left", font=(self.SETTINGS["FONT_FAMILY"][2], 12), wraplength=250)
        quote_label.place(relx=0.05, rely=0.62)
        
        def load_quote():
            with open('./SaveFiles/law.json', "r") as file:
                laws_dict = json.load(file)
                category_list = list(laws_dict.keys())
                selected_category = random.choice(category_list)
                sub_category = list((laws_dict[selected_category]).keys())
                selected_sub_category = random.choice(sub_category)
                print(laws_dict[selected_category][selected_sub_category])

        load_quote()