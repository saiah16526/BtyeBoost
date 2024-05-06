from modules import *

border_color = "#88aa77"
border_width = 1
border_radius = 4
Daily_background = "#111"
font_color = border_color
font_family = ['JetBrains Mono', "unionagrochem"]
percentage_color = border_color
percentage_background = "#6666"

class ProgressFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)  # Initialize the frame using the parent class (CTkFrame)

    def create_canvas(self, **kwargs):
        # Create a canvas within the frame with specified keyword arguments
        canvas = ProgressCanvas(self, **kwargs)  # Create a CTkCanvas widget
        canvas.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98, anchor="nw")  # Place the canvas within the frame
        return canvas  # Return the canvas widget

class ProgressCanvas(ctk.CTkCanvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)  # Initialize the canvas with the provided master widget and additional keyword arguments

    def draw_progress_meter(self):
        # Draw the outer circular progress meter background
          # Define parameters for the progress meter
        padding_inline = 90
        padding_block = 60
        radius = 12
        coordinates = (30, 170)
        
        # Draw the outer circular progress meter background (gray)
        self.create_arc(
            coordinates[0] + padding_inline,
            coordinates[0] + padding_block,
            coordinates[1] + padding_inline,
            coordinates[1] + padding_block,
            fill=percentage_color,  # Gray color
            start=-325,
            extent=280,  # Define the extent of the arc (full circle minus 40 degrees)
            outline=Daily_background  # Background color of the canvas
        )
        
        # Draw the inner circular progress meter (border)
        self.create_arc(
            coordinates[0] + padding_inline,
            coordinates[0] + padding_block,
            coordinates[1] + padding_inline,
            coordinates[1] + padding_block,
            fill=percentage_color,  # Border color
            start=-325,
            extent=180  # Define the extent of the arc (half circle minus 40 degrees)
        )
        
        # Draw a small circular indicator (dot) in the progress meter
        self.create_oval(
            coordinates[0] + padding_inline + radius,
            coordinates[0] + padding_block + radius,
            coordinates[1] + padding_inline - radius,
            coordinates[1] + padding_block - radius,
            fill=Daily_background,  # Background color
            outline=Daily_background  # Background color (no visible outline)
        )

class DailyProgressApp:
    def __init__(self, master):
        self.master = master
        self.create_widgets()  # Call the method to create widgets

    def create_widgets(self):
        # Create the daily progress frame
        frame = ProgressFrame(self.master, border_color=border_color, border_width=border_width, corner_radius=border_radius, fg_color=Daily_background)
        frame.place(relx=0.33, rely=0.597, relwidth=0.32, relheight=0.403, anchor="nw")

        # Create a canvas within the frame for the progress meter
        canvas_progress = frame.create_canvas(background=Daily_background, bd=0, highlightthickness=0)

        # Draw the progress meter on the canvas
        canvas_progress.draw_progress_meter()

        # Define label configurations for daily progress information
        label_configs = [
            {"style": {'text': 'DAILY....', 'font': (font_family[0], 50)}, 'place': {'x': 10, 'rely': 0.077, 'relheight': 0.15, 'anchor': 'nw'}},
            {"style":{'text': 'Conquests and Endeavors Progress', 'font': ('Ubuntu-Title', 18)}, 'place': {'x': 10, 'rely': 0.23, 'relheight': 0.12, 'anchor': 'nw'}},
            {"style":{'text': '4', 'font': (font_family[0], 97)}, 'place': {'relx': 0.02, 'rely': 0.38, 'anchor': 'nw'}},
            {"style":{'text': '9', 'font': (font_family[0], 37)}, 'place': {'relx': 0.25, 'rely': 0.68, 'relheight': 0.15, 'anchor': 'nw'}},
            {"style":{'text': 'In Progress...', 'font': (font_family[1], 17, 'bold')}, 'place': {'relx': 0.02, 'rely': 0.85, 'relheight': 0.15, 'anchor': 'nw'}},
            {"style":{'text': '79%', 'font': (font_family[0], 50)}, 'place': {'relx': 0.55, 'rely': 0.52, 'anchor': 'nw'}}
        ]

        # Add labels to display daily progress information
        for config in label_configs:
            ctk.CTkLabel(frame,text_color=font_color, **config["style"]).place(**config["place"])  # Create and place labels with specified configurations
