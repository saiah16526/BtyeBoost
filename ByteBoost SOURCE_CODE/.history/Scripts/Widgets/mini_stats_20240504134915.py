from modules import *

border_color = "#88aa77"
border_width = 1
border_radius = 4
Stats_background = "#111"
font_color = border_color
font_family = ['JetBrains Mono', "unionagrochem"]
percentage_color = border_color
percentage_background = "#666"


class StatsWrapper(ctk.CTkFrame):
    def __init__(self, master, stats_background=Stats_background, border="#88aa77"):
        super().__init__(master, fg_color=Stats_background, border_width=border_width, border_color=border_color)  # Initialize the parent class (tk.Frame)
        self.stats_background = stats_background  # Set the background color
        # Place the frame relative to the master widget
        self.place(relx=0.65, rely=0, relwidth=0.355, relheight=0.75, anchor="nw")
        self.create_progress_display()  # Create the progress display
        
        frame = ctk.CTkFrame(self, border_color=border_color, border_width=border_width, corner_radius=border_radius)
        frame.place(relx=0.01, rely=0, relwidth=0.97, relheight=0.1)

    def create_progress_display(self):
        # Create a canvas for displaying progress bars
        canvas_stats = tk.Canvas(self, background=self.stats_background, bd=0, highlightthickness=0)
        canvas_stats.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.89)

        # Add a scrollbar to the canvas
        scrollbar = self.add_scrollbar(canvas_stats)
        canvas_stats.configure(yscrollcommand=scrollbar.set)

        # Load lessons data from JSON file
        lessons_data = self.load_lessons_data()
        if lessons_data:
            self.draw_progress_bars(canvas_stats, lessons_data)  # Draw progress bars

        # Update canvas to get the correct scroll region
        canvas_stats.update_idletasks()
        # Adjust scroll region based on the canvas content
        canvas_stats.configure(scrollregion=canvas_stats.bbox("all"))

    def add_scrollbar(self, canvas):
        # Add a vertical scrollbar to the canvas
        scrollbar = ctk.CTkScrollbar(canvas, command=canvas.yview, width=14)
        scrollbar.place(anchor="ne", relx=1, rely=0.01, relheight=0.98)
        return scrollbar

    def load_lessons_data(self):
        # Load lessons data from a JSON file
        try:
            with open("./SaveFiles/lessons.json", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: Lessons file not found.")
            return None

    def draw_progress_bars(self, canvas, lessons_dict):
        y_increment = 0
        # Calculate total percentage from lessons data
        total_percentage = sum((value['duration'] * value['total_count']) for lesson_list in lessons_dict.values() for value in lesson_list.values())
        lessons_list = []
        # Iterate through lessons data and draw progress bars
        for category, lessons in lessons_dict.items():
            for lesson_name, properties in lessons.items():
                lessons_list.append(Lesson(lesson_name, properties))
        lessons_list = sorted(lessons_list, key=lambda x: x.percentage, reverse=True)
        for lesson_class in lessons_list:
            # Draw a progress bar for each lesson
            try:
                percentage =( lesson_class.percentage/total_percentage)
            except:
                percentage = 0
            self.draw_language_bar(canvas, lesson_class.name, (percentage * 100), y_increment)
            y_increment += 20  # Increment y position for the next progress bar
        canvas.create_rectangle(106, 5, 108, y_increment, fill="#4fa", outline=Stats_background)

    def draw_language_bar(self, canvas, text, percentage, y_increment):
        x = 103  # Initial x position for the progress bar
        y = 8 + y_increment  # Calculate y position based on y_increment
        max_x = 240  # Maximum x position for the progress bar
        # Calculate current x position based on the percentage
        current_x = ((max_x - x + 10) * percentage) / 100 + x + 10

        # Draw text (lesson name) on the canvas
        self.draw_text(canvas, x, y, text, anchor="ne", font=("Arial", 10), fill=font_color)
        # Draw a green rectangle representing the progress
        self.draw_rectangle(canvas, x + 10, y + 3.5, current_x, y + 10.5, fill="#0f0")
        # Display the percentage value next to the progress bar
        self.draw_text(canvas, current_x + 35, y, f"{int(percentage)}%", font=(font_family[0], 9, 'bold'), anchor="ne", fill="#0f0")

    def draw_text(self, canvas, x, y, text, **kwargs):
        # Draw text on the canvas with specified attributes
        canvas.create_text(x, y, text=text, justify="left", **kwargs)

    def draw_rectangle(self, canvas, x1, y1, x2, y2, **kwargs):
        # Draw a rectangle on the canvas with specified attributes
        canvas.create_rectangle(x1, y1, x2, y2, outline=self.stats_background, **kwargs)
