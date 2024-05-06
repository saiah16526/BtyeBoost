from modules import *

border_color = "#88aa77"
border_width = 1
border_radius = 4
Settings_background = "#111"
font_color = border_color
font_family = ['JetBrains Mono', "unionagrochem", "Poppins"]
percentage_color = border_color
percentage_background = "#666"

class Statistics(ctk.CTkScrollableFrame):
    row = 0
    def __init__(self, master):
        super().__init__(master, fg_color=Settings_background, border_width=border_width, corner_radius=border_radius, border_color=border_color)
        self.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)
        self.startup_load(self.row)
        self.row += 1
        
    def create_date_stats(self, date, details, row):
        frame = ctk.CTkFrame(self)
        frame.grid(column=0, row=row)
        frame.pack_propagate(flag=True)
        date_arr = (date.split("-"))
        months = ["tmp","january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
        
        date_frame = ctk.CTkFrame(frame)
        date_frame.pack(fill="x")
        self.date = ctk.CTkLabel(date_frame, text=f"DATE: {date_arr[2]}, {(months[int(date_arr[1])]).upper()} {date_arr[0]}", anchor="w",font=(font_family[0], 13))
        self.date.pack(side="left", fill="x")
        self.target = ctk.CTkLabel(date_frame, text="DAILY CHALLENGE: 100%",anchor="w", font=(font_family[0], 13))
        self.target.pack(side="right", fill="x")
        
        self.name_frame = ctk.CTkFrame(frame,corner_radius=0,width=160)
        self.category_frame = ctk.CTkFrame(frame,corner_radius=0, width=130)
        self.from_frame = ctk.CTkFrame(frame,corner_radius=0, width=80)
        self.to_frame = ctk.CTkFrame(frame,corner_radius=0, width=80)
        self.duration_frame = ctk.CTkFrame(frame,corner_radius=0)
        
        self.name_frame.pack(side="left")
        self.category_frame.pack(side="left")
        self.from_frame.pack(side="left")
        self.to_frame.pack(side="left")
        self.duration_frame.pack(side="left")
        
        self.name_frame.pack_propagate(flag=False)
        self.category_frame.pack_propagate(flag=False)
        self.from_frame.pack_propagate(flag=False)
        self.to_frame.pack_propagate(flag=False)
        self.duration_frame.pack_propagate(flag=False)
        
        ctk.CTkLabel(self.name_frame,text_color="#201" ,fg_color=font_color,text="LESSON", font=(font_family[0], 13)).pack(padx=1,fill="x")
        ctk.CTkLabel(self.category_frame,text_color="#201" ,fg_color=font_color,text="CATEGORY", font=(font_family[0], 13)).pack(padx=1,fill="x")
        ctk.CTkLabel(self.from_frame,text_color="#201" ,fg_color=font_color,text="FROM", font=(font_family[0], 13)).pack(padx=1,fill="x")
        ctk.CTkLabel(self.to_frame,text_color="#201" ,fg_color=font_color,text="TO", font=(font_family[0], 13)).pack(padx=1,fill="x")
        ctk.CTkLabel(self.duration_frame,text_color="#201" ,fg_color=font_color,text="DURATION", font=(font_family[0], 13)).pack(padx=1,fill="x")
        
        is_red = False
        for start , contents in details.items():
            color = None
            if is_red:
                color = "blue"
                is_red = False
            else:
                is_red = True
                color = "purple"
            self.update_stats(contents["lesson"], contents["Category"], start, contents["TO"], contents["Duration"], color)
    def update_stats(self, name, category, start, to, duration, color):
        ctk.CTkLabel(fg_color=color,master=self.name_frame, text=name, font=(font_family[0], 13)).pack(fill="x", padx=1)
        ctk.CTkLabel(fg_color=color,master=self.category_frame, text=category, font=(font_family[0], 13)).pack(fill="x", padx=1)
        ctk.CTkLabel(fg_color=color,master=self.from_frame, text=start, font=(font_family[0], 13)).pack(fill="x", padx=1)
        ctk.CTkLabel(fg_color=color,master=self.to_frame, text=to, font=(font_family[0], 13)).pack(fill="x", padx=1)
        ctk.CTkLabel(fg_color=color,master=self.duration_frame, text=duration, font=(font_family[0], 13)).pack(fill="x", padx=1)
        
    def startup_load(self, row):
        with open("./SaveFiles/Stats.json", "r") as file:
            stats_dict = json.load(file)
            for date, details in stats_dict.items():
                self.create_date_stats(date, details, row)
        
        
