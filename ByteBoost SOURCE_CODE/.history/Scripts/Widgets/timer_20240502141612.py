from modules import *
from Widgets.mini_stats import *


border_color = "#88aa77"
border_width = 0
border_radius = 4
Timer_background = "#111"
font_color = border_color
font_family = ['JetBrains Mono', "unionagrochem"]
percentage_color = border_color
percentage_background = "#666"



class TimerFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,fg_color=Timer_background, **kwargs)  # Initialize the Frame with its master and other kwargs
        self.master = master  # Set the master attribute to the passed master widget
        self.remaining_time = datetime.timedelta(seconds=0)  # Initialize remaining_time to 0 seconds
        self.total_minutes = 0  # Initialize total_minutes to 0
        self.temp = None
        self.timer_running = False  # Set timer_running to False initially
        self.timer_paused = False
        self.current_Percentage = 100
        self.place(relx=0.65, rely=0.75, relwidth=0.35, relheight=0.25, anchor="nw")
        # Initial setup: update the timer display
        self.update_timer()
        self.create_widgets()  # Call the method to create widgets

    def create_widgets(self):
        # Create and place the progress canvas
        self.progress_canvas = tk.Canvas(self, bg=Timer_background, bd=0, highlightthickness=0)
        self.progress_canvas.place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.98, anchor="nw")
        self.ProgressMeter(self)

        # Create and place the clock label
        self.clock = ctk.CTkLabel(self, text_color=font_color, text="0:00", font=("JetBrains Mono", 40), anchor="w")
        self.clock.place(relx=0.11, rely=0.35)
        
        record = ctk.CTkLabel(self, text_color=font_color, text="Record to beat: 1:45", font=(font_family[2], 14), anchor="w")
        record.place(relx=0.42, rely=0.1)

        ctk.CTkLabel(self, text_color=font_color, text="Selected Lesson:", font=(font_family[2], 14), anchor="w").place(relx=0.42, rely=0.23)

        self.lang = ctk.StringVar()
        self.current_lang = ctk.CTkLabel(self ,text_color="#333333", text="selected_lesson", textvariable=self.lang,font=("JetBrains Mono", 16), anchor="w")
        self.current_lang.place(relx=0.42, rely=0.36)

        
        label_input = ctk.CTkLabel(self, text_color=font_color, text="Desired Duration:", font=(font_family[2], 14), anchor="w")
        label_input.place(relx=0.42, rely=0.52)

        self.entry = ctk.StringVar()
        ctk.CTkEntry(self,textvariable=self.entry ,corner_radius=3, placeholder_text="1:45").place(relx=0.82, rely=0.52, relwidth=0.16)
        
        # Create and place controls for start, pause, and stop
        start_btn = ctk.CTkButton(self, corner_radius=3, text="Start", command=self.start_timer)
        start_btn.place(relx=0.5, rely=0.75, relwidth=0.1)

        pause_btn = ctk.CTkButton(self, corner_radius=3, text="Pause", command=self.pause_timer)
        pause_btn.place(relx=0.65, rely=0.75, relwidth=0.1)

        stop_btn = ctk.CTkButton(self, corner_radius=3, text="Stop", command=self.stop_timer)
        stop_btn.place(relx=0.8, rely=0.75, relwidth=0.1)

        

    def start_timer(self):
        
        if not self.timer_running:
            desired_time = self.entry.get()  # Get the desired duration from the entry widget
            self.entry.set("")
            try:
                # Parse the desired time into hours and minutes
                hours, minutes = map(int, desired_time.split(':'))
            except ValueError:
                # Handle invalid input gracefully (e.g., non-numeric characters)
                hours, minutes = 0, 0
            
            # Calculate the total duration in minutes
            self.total_minutes = hours * 60 + minutes
            if self.temp is None:
                self.remaining_time = datetime.timedelta(minutes=self.total_minutes)
            else:
                self.remaining_time = self.temp
            # Update the clock label with the formatted time remaining
            self.clock.configure(text=str(self.remaining_time)[:-3])  # Format as MM:SS
            # Start the timer update loop
            self.timer_running = True
            self.timer_paused = False
            self.update_timer()

    def pause_timer(self):
        
        if self.timer_running:
            # Stop the timer update loop
            self.timer_running = False
            self.temp = self.remaining_time
            self.after_cancel(self.timer_id)
            self.timer_paused = True

    def stop_timer(self):
        if self.timer_running or self.timer_paused:
            # Reset timer state
            print(f"{(self.total_minutes * 60) - self.remaining_time.total_seconds()} ::: {self.lang.get()}")
            duration = ((self.total_minutes * 60) - self.remaining_time.total_seconds())/3600
            print(duration)
            with open("./Scripts/lessons.json", '+r') as rf:
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
            self.temp = None
            self.lang.set("")
            self.clock.configure(text="0:00")  # Reset clock display
            self.after_cancel(self.timer_id)

    def update_timer(self):
        if self.timer_running and self.remaining_time.total_seconds() > 0:
            # Update the remaining time
            self.remaining_time -= datetime.timedelta(seconds=1)
            self.current_Percentage = ((self.remaining_time.total_seconds()/(self.total_minutes * 60)) * 100)
            self.ProgressMeter(self)
            self.clock.destroy()
            self.clock = ctk.CTkLabel(self, text_color=border, text="0:00", font=("JetBrains Mono", 40), anchor="w")
            self.clock.place(relx=0.11, rely=0.35, relwidth=0.3)
            self.clock.configure(text=str(self.remaining_time))  # Format as MM:SS
            # Schedule the next update after 1000ms (1 second)
            self.timer_id = self.after(1000, self.update_timer)
        else:
            # Timer finished, stop the timer
            self.stop_timer()

    def ProgressMeter(self,master):
        # Function to display the timer progress visually
        canvas_progress = ctk.CTkCanvas(master, background=Timer_background, bd=0, highlightthickness=0)
        canvas_progress.place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.98, anchor="nw")
        
        # Draw the progress meter components (arc and oval)
        padding_inline = 0
        padding_block = 10
        radius = 12
        coordinates = (5, 130)
        extent =(( 290 * (100-self.current_Percentage))/100)
        
        # Draw the outer circular background of the progress meter
        canvas_progress.create_arc(
            coordinates[0] + padding_inline,
            coordinates[0] + padding_block,
            coordinates[1] + padding_inline,
            coordinates[1] + padding_block,
            fill="#666666",  # Gray color
            start=30,
            extent=290,  # Define the extent of the arc (full circle minus 40 degrees)
            outline=Timer_background  # Background color of the canvas
        )
        
        # Draw the inner circular progress meter (border)
        canvas_progress.create_arc(
            coordinates[0] + padding_inline,
            coordinates[0] + padding_block,
            coordinates[1] + padding_inline,
            coordinates[1] + padding_block,
            fill=border_color,  # Border color
            start=30,
            extent=extent  # Define the extent of the arc (half circle minus 40 degrees)
        )
        
        # Draw a small circular indicator (dot) in the progress meter
        canvas_progress.create_oval(
            coordinates[0] + padding_inline + radius,
            coordinates[0] + padding_block + radius,
            coordinates[1] + padding_inline - radius,
            coordinates[1] + padding_block - radius,
            fill=Timer_background,  # Background color
            outline=Timer_background  # Background color (no visible outline)
        )

