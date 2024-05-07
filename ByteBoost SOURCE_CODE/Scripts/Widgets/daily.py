from modules import *

BORDER_WIDTH = 0
BORDER_RADIUS = 4

class ProgressFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        self.SETTINGS = load_settings()
        super().__init__(master, **kwargs)  # Initialize the frame using the parent class (CTkFrame)

    def create_canvas(self, **kwargs):
        # Create a canvas within the frame with specified keyword arguments
        canvas = ProgressCanvas(self, **kwargs)  # Create a CTkCanvas widget
        canvas.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98, anchor="nw")  # Place the canvas within the frame
        return canvas  # Return the canvas widget

class ProgressCanvas(ctk.CTkCanvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)  # Initialize the canvas with the provided master widget and additional keyword arguments
        self.SETTINGS = load_settings()
        self.progress_meter = ProgressMeter(self)
    
class ProgressMeter:
    def __init__(self, parent):
        self.SETTINGS = load_settings()
        self.parent = parent
        self.padding_inline = 100
        self.padding_block = 100
        self.radius = 12
        self.coordinates = (5, 150)

    def update(self, percentage):
        self.parent.delete("all")  # Clear previous drawings
        percentage =int( (percentage.split("%"))[0])
        extent = (290 * (percentage)) /100

        # Draw outer circular background
        self.parent.create_arc(
            self.coordinates[0] + self.padding_inline,
            self.coordinates[0] + self.padding_block,
            self.coordinates[1] + self.padding_inline,
            self.coordinates[1] + self.padding_block,
            fill = self.SETTINGS["PERCENTAGE_BACKGROUND"],
            start=30,
            extent=290,
            outline=self.SETTINGS["BACKGROUND"]
        )

        # Draw inner progress arc
        self.parent.create_arc(
            self.coordinates[0] + self.padding_inline,
            self.coordinates[0] + self.padding_block,
            self.coordinates[1] + self.padding_inline,
            self.coordinates[1] + self.padding_block,
            fill=self.SETTINGS["PROGRESS_THEME"],
            start=30,
            extent=extent
        )

        # Draw circular indicator
        self.parent.create_oval(
            self.coordinates[0] + self.padding_inline + self.radius,
            self.coordinates[0] + self.padding_block + self.radius,
            self.coordinates[1] + self.padding_inline - self.radius,
            self.coordinates[1] + self.padding_block - self.radius,
            fill=self.SETTINGS["BACKGROUND"],
            outline=self.SETTINGS["BACKGROUND"]
        )

class DailyProgressApp:
    def __init__(self, master):
        self.SETTINGS = load_settings()
        self.master = master
        self.done = ctk.StringVar()
        self.total = ctk.StringVar()
        self.percentage = ctk.StringVar()
        self.frame = ProgressFrame(self.master, border_color=self.SETTINGS["BORDER_COLOR"], border_width=BORDER_WIDTH, corner_radius=BORDER_RADIUS, fg_color=self.SETTINGS["BACKGROUND"])
        self.create_widgets()  # Call the method to create widgets
        self.update_progress()
    def create_widgets(self):
        # Create the daily progress frame
        self.frame.place(relx=0.33, rely=0.6, relwidth=0.32, relheight=0.403, anchor="nw")

        # Create a canvas within the frame for the progress meter
        self.canvas_progress = self.frame.create_canvas(background=self.SETTINGS["BACKGROUND"], bd=0, highlightthickness=0)

        # Draw the progress meter on the canvas
        self.canvas_progress.progress_meter.update("0%")

        # Define label configurations for daily progress information
        label_configs = [
            {"style": {'text': 'DAILY....', 'font': (self.SETTINGS["FONT_FAMILY"][1], 50)}, 'place': {'x': 10, 'rely': 0.077, 'relheight': 0.15, 'anchor': 'nw'}},
            {"style":{'text': 'Conquests and Endeavors Progress', 'font': (self.SETTINGS["FONT_FAMILY"][2], 13)}, 'place': {'x': 10, 'rely': 0.23, 'relheight': 0.12, 'anchor': 'nw'}},
            {"style":{'text': '5',"textvariable": self.done ,'font': (self.SETTINGS["FONT_FAMILY"][0], 100)}, 'place': {'relx': 0.02, 'rely': 0.38, 'anchor': 'nw'}},
            {"style":{'text': '9',"textvariable": self.total ,'font': (self.SETTINGS["FONT_FAMILY"][0], 37)}, 'place': {'relx': 0.25, 'rely': 0.68, 'relheight': 0.15, 'anchor': 'nw'}},
            {"style":{'text': 'In Progress...', 'font': (self.SETTINGS["FONT_FAMILY"][2], 17, 'bold')}, 'place': {'relx': 0.02, 'rely': 0.85, 'relheight': 0.15, 'anchor': 'nw'}},
            {"style":{'text': '79%',"textvariable": self.percentage, 'font': (self.SETTINGS["FONT_FAMILY"][0], 50)}, 'place': {'relx': 0.55, 'rely': 0.58, 'anchor': 'nw'}}
        ]

        # Add labels to display daily progress information
        for config in label_configs:
            ctk.CTkLabel(self.frame,text_color=self.SETTINGS["BORDER_COLOR"], **config["style"]).place(**config["place"])  # Create and place labels with specified configurations

    def update_progress(self):
        current_time = datetime.datetime.now()
        current_date = str(current_time.date())
        tasks = []
        self.provide_daily_tasks()
        with open(resource_path(".\\SaveFiles\\Stats.json"), "r") as file:
            stats_dict = json.load(file)
            for date, details in stats_dict.items():
                if date == current_date:
                    tasks = list(details.keys())
        with open(resource_path(".\\Settings\\settings.json"), "r") as file:
            settings_dict = json.load(file)
            self.total.set(settings_dict["TASKS"][current_date])
            self.done.set(len(tasks))
            self.percentage.set(f"{int(((len(tasks))/settings_dict["TASKS"][current_date]) * 100)}%")
        self.canvas_progress.progress_meter.update(self.percentage.get())
        self.frame.after(1000, lambda: self.update_progress())
        
    def provide_daily_tasks(self):
        current_time = datetime.datetime.now()
        current_date = str(current_time.date())
        rand_tasks  = random.randint(4,9)
        with open(resource_path(".\\Settings\\settings.json"), "+r") as file:
            settings_dict = json.load(file)
            date =list( settings_dict["TASKS"].keys())
            if date[0] != current_date:
                style = {
                            current_date : rand_tasks
                                     }
                settings_dict.update({"TASKS" : style})
            file.seek(0)
            file.write(json.dumps(settings_dict, indent=2))
            file.truncate()
