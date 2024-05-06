from Widgets.mini_stats import StatsWrapper
from Widgets.mega_stats import Statistics
from modules import *

class TimerFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        self.SETTINGS = load_settings()
        super().__init__(master, fg_color=self.SETTINGS["BACKGROUND"], **kwargs)
        self.master = master
        self.remaining_time = datetime.timedelta(seconds=0)
        self.total_minutes = 0
        self.previous_remaining_time = None
        self.timer_running = False
        self.timer_paused = False
        self.current_percentage = 100
        self.place(relx=0.65, rely=0.75, relwidth=0.35, relheight=0.25, anchor="nw")
        self.update_timer()
        self.create_widgets()
        self.progress_meter = self.ProgressMeter(self)  # Instantiate ProgressMeter
        self.progress_meter.update()

    def create_widgets(self):
        # Progress Canvas
        self.progress_canvas = ctk.CTkCanvas(self, background=self.SETTINGS["BACKGROUND"], bd=0, highlightthickness=0)
        self.progress_canvas.place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.98, anchor="nw")

        # Clock Label
        self.clock = ctk.CTkLabel(self, text_color=self.SETTINGS["BORDER_COLOR"], text="0:00", font=("JetBrains Mono", 40), anchor="w")
        self.clock.place(relx=0.11, rely=0.35)

        # Other Labels and Entry
        ctk.CTkLabel(self, text_color=self.SETTINGS["BORDER_COLOR"], text="Record to beat: 1:45", font=(self.SETTINGS["FONT_FAMILY"][2], 14), anchor="w").place(relx=0.42, rely=0.1)
        ctk.CTkLabel(self, text_color=self.SETTINGS["BORDER_COLOR"], text="Selected Lesson:", font=(self.SETTINGS["FONT_FAMILY"][2], 14), anchor="w").place(relx=0.42, rely=0.23)
        self.lang = ctk.StringVar(value="Qt")
        ctk.CTkLabel(self, text_color="#666666", textvariable=self.lang, font=(self.SETTINGS["FONT_FAMILY"][2], 14), anchor="w").place(relx=0.42, rely=0.37)
        ctk.CTkLabel(self, text_color=self.SETTINGS["self.SETTINGS["BORDER_COLOR"]"], text="Desired Duration:", font=(self.SETTINGS["FONT_FAMILY"][2], 14), anchor="w").place(relx=0.42, rely=0.52)

        self.entry_value = ctk.StringVar()
        ctk.CTkEntry(self, textvariable=self.entry_value, corner_radius=3, placeholder_text="1:45").place(relx=0.82, rely=0.48, relwidth=0.16)

        #Images
        start_img = ImageTk.PhotoImage(Image.open("./Images/Icons/start.png").resize((50, 50)))
        pause_img = ImageTk.PhotoImage(Image.open("./Images/Icons/pause.png").resize((50, 50)))
        reset_img = ImageTk.PhotoImage(Image.open("./Images/Icons/reset.png").resize((50, 50)))
        # Buttons
        ctk.CTkButton(self, corner_radius=3,image=start_img ,text="", command=self.start_timer, hover_color=self.SETTINGS["BACKGROUND"],fg_color=self.SETTINGS["BACKGROUND"]).place(relx=0.5, rely=0.65, relwidth=0.14)
        ctk.CTkButton(self, corner_radius=3, image=pause_img ,text="", command=self.pause_timer,hover_color=self.SETTINGS["BACKGROUND"],fg_color=self.SETTINGS["BACKGROUND"]).place(relx=0.69, rely=0.65, relwidth=0.14)
        ctk.CTkButton(self, corner_radius=3, image=reset_img ,text="", command=self.stop_timer,hover_color=self.SETTINGS["BACKGROUND"],fg_color=self.SETTINGS["BACKGROUND"]).place(relx=0.84, rely=0.65, relwidth=0.14)

    def start_timer(self):
        if not self.timer_running:
            current_time  = datetime.datetime.now()
            self.start_time=  f"{current_time.time().hour}:{current_time.time().minute}"
            desired_time = self.entry_value.get()
            self.entry_value.set("")
            try:
                hours, minutes = map(int, desired_time.split(':'))
            except ValueError:
                hours, minutes = 0, 0
            
            self.total_minutes = hours * 60 + minutes
            if self.previous_remaining_time is None:
                self.remaining_time = datetime.timedelta(minutes=self.total_minutes)
            else:
                self.remaining_time = self.previous_remaining_time
            
            self.clock.configure(text=self.format_time(self.remaining_time))
            self.timer_running = True
            self.timer_paused = False
            self.update_timer()

    def pause_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.previous_remaining_time = self.remaining_time
            self.after_cancel(self.timer_id)
            self.timer_paused = True

    def stop_timer(self):
        CATEGORY = None
        if self.timer_running or self.timer_paused:
            duration = ((self.total_minutes * 60) - self.remaining_time.total_seconds()) / 3600
            with open("./SaveFiles/lessons.json", '+r') as rf:
                lessons_dict = json.load(rf)
                for category, lessons in lessons_dict.items():
                    for name, properties in lessons.items():
                        if name == self.lang.get():
                            properties["duration"] += duration
                            properties["total_count"] += 1
                            CATEGORY = category
                rf.seek(0)
                rf.writelines(json.dumps(lessons_dict, indent=2))
                rf.truncate()
                
            with open("./SaveFiles/Stats.json", "+r") as file:
                stats_dict = json.load(file)
                current_time = datetime.datetime.now()
                current_date = str(current_time.date())
                stop_time = f"{current_time.time().hour}:{current_time.time().minute}"
                style = {
                    self.start_time : {
                        "lesson": self.lang.get(),
                        "Category": CATEGORY,
                        "TO": stop_time,
                        "Duration": duration * 60
                    }
                }

                style2 = {
                        "lesson": self.lang.get(),
                        "Category": CATEGORY,
                        "TO": stop_time,
                        "Duration": duration * 60
                    }
                found = False
                for date, details in stats_dict.items():
                    if date == current_date:
                        found = True
                        details.update({self.start_time : style2})
                if found == False:
                    stats_dict.update({current_date : style})
                        
                file.seek(0)
                file.writelines(json.dumps(stats_dict, indent=2))
                file.truncate()
                
            self.master.side_stats.destroy()
            self.master.side_stats = StatsWrapper(self.master)
            self.master.statistics.destroy()
            self.master.statistics = Statistics(self.master)
            self.timer_running = False
            self.remaining_time = None
            self.previous_remaining_time = None
            self.clock.configure(text="0:00")
            self.after_cancel(self.timer_id)

    def update_timer(self):
        if self.timer_running and self.remaining_time.total_seconds() > 0:
            self.remaining_time -= datetime.timedelta(seconds=1)
            self.current_percentage = ((self.remaining_time.total_seconds() / (self.total_minutes * 60)) * 100)
            self.progress_meter.update()
            self.clock.configure(text=self.format_time(self.remaining_time))
            self.timer_id = self.after(1000, self.update_timer)
        else:
            self.stop_timer()

    def format_time(self, time_delta):
        # Format timedelta to HH:MM
        hours, remainder = divmod(time_delta.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{hours}:{minutes:02d}"
    
    class ProgressMeter:
        def __init__(self, parent):
            self.SETTINGS = load_settings()
            self.parent = parent
            self.padding_inline = 0
            self.padding_block = 10
            self.radius = 12
            self.coordinates = (5, 130)

        def update(self):
            self.parent.progress_canvas.delete("all")  # Clear previous drawings

            extent = (290 * (100 - self.parent.current_percentage)) / 100

            # Draw outer circular background
            self.parent.progress_canvas.create_arc(
                self.coordinates[0] + self.padding_inline,
                self.coordinates[0] + self.padding_block,
                self.coordinates[1] + self.padding_inline,
                self.coordinates[1] + self.padding_block,
                fill="#666666",
                start=30,
                extent=290,
                outline=self.SETTINGS["BACKGROUND"]
            )

            # Draw inner progress arc
            self.parent.progress_canvas.create_arc(
                self.coordinates[0] + self.padding_inline,
                self.coordinates[0] + self.padding_block,
                self.coordinates[1] + self.padding_inline,
                self.coordinates[1] + self.padding_block,
                fill=self.SETTINGS["BORDER_COLOR"],
                start=30,
                extent=extent
            )

            # Draw circular indicator
            self.parent.progress_canvas.create_oval(
                self.coordinates[0] + self.padding_inline + self.radius,
                self.coordinates[0] + self.padding_block + self.radius,
                self.coordinates[1] + self.padding_inline - self.radius,
                self.coordinates[1] + self.padding_block - self.radius,
                fill=self.SETTINGS["BACKGROUND"],
                outline=self.SETTINGS["BACKGROUND"]
            )
