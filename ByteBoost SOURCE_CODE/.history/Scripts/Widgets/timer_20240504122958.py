from Widgets.mini_stats import StatsWrapper
from modules import *
# Constants
BORDER_COLOR = "#88aa77"
TIMER_BACKGROUND = "#111"
FONT_COLOR = BORDER_COLOR
FONT_FAMILY = ['JetBrains Mono', "unionagrochem", "Poppins"]

class TimerFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color=TIMER_BACKGROUND, **kwargs)
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

    def create_widgets(self):
        # Progress Canvas
        self.progress_canvas = ctk.CTkCanvas(self, background=TIMER_BACKGROUND, bd=0, highlightthickness=0)
        self.progress_canvas.place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.98, anchor="nw")

        self.progress_meter.update()
        # Clock Label
        self.clock = ctk.CTkLabel(self, text_color=FONT_COLOR, text="0:00", font=("JetBrains Mono", 40), anchor="w")
        self.clock.place(relx=0.11, rely=0.35)

        # Other Labels and Entry
        ctk.CTkLabel(self, text_color=FONT_COLOR, text="Record to beat: 1:45", font=(FONT_FAMILY[2], 14), anchor="w").place(relx=0.42, rely=0.1)
        ctk.CTkLabel(self, text_color=FONT_COLOR, text="Selected Lesson:", font=(FONT_FAMILY[2], 14), anchor="w").place(relx=0.42, rely=0.23)
        self.lang = ctk.StringVar()
        ctk.CTkLabel(self, text_color=FONT_COLOR, textvariable=self.lang, font=(FONT_FAMILY[2], 14), anchor="w").place(relx=0.42, rely=0.3)
        ctk.CTkLabel(self, text_color=FONT_COLOR, text="Desired Duration:", font=(FONT_FAMILY[2], 14), anchor="w").place(relx=0.42, rely=0.52)

        self.entry_value = ctk.StringVar()
        ctk.CTkEntry(self, textvariable=self.entry_value, corner_radius=3, placeholder_text="1:45").place(relx=0.82, rely=0.52, relwidth=0.16)

        # Buttons
        ctk.CTkButton(self, corner_radius=3, text="Start", command=self.start_timer).place(relx=0.5, rely=0.75, relwidth=0.1)
        ctk.CTkButton(self, corner_radius=3, text="Pause", command=self.pause_timer).place(relx=0.65, rely=0.75, relwidth=0.1)
        ctk.CTkButton(self, corner_radius=3, text="Stop", command=self.stop_timer).place(relx=0.8, rely=0.75, relwidth=0.1)

    def start_timer(self):
        if not self.timer_running:
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
        if self.timer_running or self.timer_paused:
            duration = ((self.total_minutes * 60) - self.remaining_time.total_seconds()) / 3600
            print(duration)
            with open("./SaveFiles/lessons.json", '+r') as rf:
                lessons_dict = json.load(rf)
                for category, lessons in lessons_dict.items():
                    for name, properties in lessons.items():
                        if name == self.lang.get():
                            properties["duration"] += duration
                            properties["total_count"] += 1
                rf.seek(0)
                rf.writelines(json.dumps(lessons_dict, indent=2))
                rf.truncate()
                
            self.master.side_stats.destroy()
            self.master.side_stats = StatsWrapper(self.master)
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
                outline=TIMER_BACKGROUND
            )

            # Draw inner progress arc
            self.parent.progress_canvas.create_arc(
                self.coordinates[0] + self.padding_inline,
                self.coordinates[0] + self.padding_block,
                self.coordinates[1] + self.padding_inline,
                self.coordinates[1] + self.padding_block,
                fill=BORDER_COLOR,
                start=30,
                extent=extent
            )

            # Draw circular indicator
            self.parent.progress_canvas.create_oval(
                self.coordinates[0] + self.padding_inline + self.radius,
                self.coordinates[0] + self.padding_block + self.radius,
                self.coordinates[1] + self.padding_inline - self.radius,
                self.coordinates[1] + self.padding_block - self.radius,
                fill=TIMER_BACKGROUND,
                outline=TIMER_BACKGROUND
            )
