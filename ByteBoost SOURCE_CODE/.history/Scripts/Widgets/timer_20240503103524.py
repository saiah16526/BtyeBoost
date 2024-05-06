import tkinter as tk
import datetime
import json
from Widgets.mini_stats import StatsWrapper

# Constants
BORDER_COLOR = "#88aa77"
TIMER_BACKGROUND = "#111"
FONT_COLOR = BORDER_COLOR
FONT_FAMILY = ['JetBrains Mono', "unionagrochem", "Poppins"]

class TimerFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg=TIMER_BACKGROUND, **kwargs)
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

    def create_widgets(self):
        # Progress Canvas
        self.progress_canvas = tk.Canvas(self, bg=TIMER_BACKGROUND, bd=0, highlightthickness=0)
        self.progress_canvas.place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.98, anchor="nw")

        # Clock Label
        self.clock = tk.Label(self, fg=FONT_COLOR, text="0:00", font=("JetBrains Mono", 40), anchor="w")
        self.clock.place(relx=0.11, rely=0.35)

        # Other Labels and Entry
        tk.Label(self, fg=FONT_COLOR, text="Record to beat: 1:45", font=(FONT_FAMILY[2], 14), anchor="w").place(relx=0.42, rely=0.1)
        tk.Label(self, fg=FONT_COLOR, text="Selected Lesson:", font=(FONT_FAMILY[2], 14), anchor="w").place(relx=0.42, rely=0.23)
        tk.Label(self, fg=FONT_COLOR, text="Desired Duration:", font=(FONT_FAMILY[2], 14), anchor="w").place(relx=0.42, rely=0.52)

        self.entry_value = tk.StringVar()
        tk.Entry(self, textvariable=self.entry_value, font=("JetBrains Mono", 12), bd=2, relief=tk.FLAT).place(relx=0.82, rely=0.52, relwidth=0.16)

        # Buttons
        tk.Button(self, text="Start", command=self.start_timer).place(relx=0.5, rely=0.75, relwidth=0.1)
        tk.Button(self, text="Pause", command=self.pause_timer).place(relx=0.65, rely=0.75, relwidth=0.1)
        tk.Button(self, text="Stop", command=self.stop_timer).place(relx=0.8, rely=0.75, relwidth=0.1)

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
            
            self.clock.config(text=str(self.remaining_time)[:-3])
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
            self.clock.config(text="0:00")
            self.after_cancel(self.timer_id)

    def update_timer(self):
        if self.timer_running and self.remaining_time.total_seconds() > 0:
            self.remaining_time -= datetime.timedelta(seconds=1)
            self.current_percentage = ((self.remaining_time.total_seconds() / (self.total_minutes * 60)) * 100)
            self.progress_meter()
            self.clock.config(text=str(self.remaining_time))
            self.timer_id = self.after(1000, self.update_timer)
        else:
            self.stop_timer()

    def progress_meter(self):
        canvas_progress = tk.Canvas(self, bg=TIMER_BACKGROUND, bd=0, highlightthickness=0)
        canvas_progress.place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.98, anchor="nw")

        padding_inline = 0
        padding_block = 10
        radius = 12
        coordinates = (5, 130)
        extent = (290 * (100 - self.current_percentage)) / 100
        
        canvas_progress.create_arc(
            coordinates[0] + padding_inline,
            coordinates[0] + padding_block,
            coordinates[1] + padding_inline,
            coordinates[1] + padding_block,
            fill="#666666",
            start=30,
            extent=290,
            outline=TIMER_BACKGROUND
        )
        
        canvas_progress.create_arc(
            coordinates[0] + padding_inline,
            coordinates[0] + padding_block,
            coordinates[1] + padding_inline,
            coordinates[1] + padding_block,
            fill=BORDER_COLOR,
            start=30,
            extent=extent
        )
        
        canvas_progress.create_oval(
            coordinates[0] + padding_inline + radius,
            coordinates[0] + padding_block + radius,
            coordinates[1] + padding_inline - radius,
            coordinates[1] + padding_block - radius,
            fill=TIMER_BACKGROUND,
            outline=TIMER_BACKGROUND
        )
