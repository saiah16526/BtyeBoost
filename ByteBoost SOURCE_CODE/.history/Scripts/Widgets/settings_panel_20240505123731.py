from modules import *
from Widgets.daily import *
from Widgets.Into import *
from Widgets.panel import *
from Widgets.mini_stats import *
from Widgets.timer import *
from Widgets.settings_panel import *
from Widgets.mega_stats import *

border_color = "#88aa77"
border_width = 1
border_radius = 4
Settings_background = "#111"
font_color = border_color
font_family = ['JetBrains Mono', "unionagrochem", "Poppins"]
percentage_color = border_color
percentage_background = "#666"

class Settings(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=Settings_background, border_width=border_width, corner_radius=border_radius, border_color=border_color)
        frame = ctk.CTkFrame(self)
        frame.place(relx=0.01, rely=0.01, relwidth=(1/4), relheight=0.98)
        lesson = Lessons_panel(self)
        file = File_panel(self)
        theme = Theme_panel(self)
        
        #images
        reset_img = ImageTk.PhotoImage(Image.open("./Images/Icons/refresh.png").resize((50, 50)))
        
        self.create_buttons(frame, text="THEME", frame=theme)
        self.create_buttons(frame, text="LESSONS",frame= lesson)
        self.create_buttons(frame, text="FILE SYS", frame=file)
        self.create_buttons(frame, text="RESET", frame=file, image = reset_img)
        
        def close_panel(self):
            self.place_forget()
            self.close_btn.place_forget()
            def kill():
                self.master.daily.frame.destroy()
                self.master.panel.destroy()
                self.master.settings.destroy()
                self.master.statistics.destroy()
                self.master.side_stats.destroy()
                self.master.counter.destroy()
                self.master.intro.intro_frame.destroy()
                restart()
            def restart():
                self.master.intro = Into_page(self.master)
                self.master.daily = DailyProgressApp(self.master)
                self.master.side_stats = StatsWrapper(self.master)
                self.master.counter = TimerFrame(self.master)
                self.master.panel = Panel(self.master)
                self.master.settings = Settings(self.master)
                self.master.statistics = Statistics(self.master)
            kill()
            
        close_img = ImageTk.PhotoImage(Image.open("./Images/Icons/close.png").resize((30, 30)))
        self.close_btn = ctk.CTkButton(master,fg_color=border_color ,height=10,text="",image=close_img,corner_radius=3 ,font=(font_family[0], 13), command=lambda: close_panel(self))
        self.bring_self_to_front()
        
    def show_panel(self):
        self.close_btn.place(relx=0.83, rely=0.18, relwidth=0.045)
        self.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)
        
    def create_buttons(self, master, text, frame = None, **kwargs):
        self.theme_btn = ctk.CTkButton(master,corner_radius=0, text=text, compound="top",font=(font_family[0], 20), command=lambda: self.bring_frame_to_front(frame.main_frame), **kwargs)
        self.theme_btn.pack(expand=True, fill="both", pady=1)
        
    def bring_frame_to_front(self, frame):
        frame.lift()
    def bring_self_to_front(self):
        self.lift()
        self.close_btn.lift()
        self.after(1000, self.bring_self_to_front)
        
class Lessons_panel():
    def __init__(self, master):
        self.main_frame = ctk.CTkFrame(master, corner_radius=0)
        self.main_frame.place(relx=(1/4), rely=0.01, relwidth=(3/4)-0.01, relheight=0.98)
        self.create_add_frame(self.main_frame)
        self.create_del_frame(self.main_frame)
        
        #ADD menu
    def create_add_frame(self, main_frame):
        add_frame = ctk.CTkFrame(main_frame,corner_radius=0, border_color=border_color, border_width=border_width)
        add_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.49)
        
        ctk.CTkLabel(add_frame, text=f"{("Wanna Add a new Lesson to track").title()}", font=(font_family[2], 13)).place(relx=0.01, rely=0.01)
        
        category_list = []
        def load_category():
            global category_dict
            with open("./SaveFiles/Lessons.json", "+r") as file:
                category_dict = json.load(file)
                for category, _ in category_dict.items():
                    category_list.append(category)
        
        load_category()
        def add_lesson():
            title = new_category.get().strip()
            lesson = new_lesson.get().strip()

            if not title:
                title = category.get().strip()

            if not lesson:
                return  # No lesson to add

            # Define the lesson style
            style = {
                lesson: {
                    "duration": 0,
                    "total_count": 0
                }
            }

            # Open the JSON file for reading and writing
            with open("./SaveFiles/Lessons.json", 'r+') as file:
                try:
                    category_dict = json.load(file)
                except json.JSONDecodeError:
                    category_dict = {}

                found = False
                for heading, details in category_dict.items():
                    if heading.lower() == title.lower():
                        found = True
                        if lesson not in details:
                            details[lesson] = style[lesson]
                        break

                if not found:
                    category_dict[title] = style

                # Move cursor to the beginning of the file to overwrite content
                file.seek(0)
                json.dump(category_dict, file, indent=2)
                file.truncate()
                
        ctk.CTkLabel(add_frame, text=f"{("Category:").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.2)
        category = ctk.CTkComboBox(add_frame,values=category_list, corner_radius=0)
        category.place(relx=0.21, rely=0.2)
        
        ctk.CTkLabel(add_frame, text=f"{("New category:").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.39)
        new_category = ctk.CTkEntry(add_frame, placeholder_text="Category not Enlisted !!!", corner_radius=0, border_width=1)
        new_category.place(relx=0.3, rely=0.39)
        
        ctk.CTkLabel(add_frame, text=f"{("Lesson To Add:").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.58)
        new_lesson = ctk.CTkEntry(add_frame, placeholder_text="Node.js", corner_radius=0, border_width=1)
        new_lesson.place(relx=0.3, rely=0.58)
        
        
        save_btn = ctk.CTkButton(add_frame, text="SAVE",corner_radius=0,font=(font_family[0], 12), command=add_lesson)
        save_btn.place(anchor="ne", relx=0.99, rely=0.82, relwidth=0.1)
        
         #Remove menu
    def create_del_frame(self, main_frame):
        del_frame = ctk.CTkFrame(main_frame, corner_radius=0,border_color=border_color, border_width=border_width)
        del_frame.place(relx=0.01, rely=0.51, relwidth=0.98, relheight=0.49)
        
        ctk.CTkLabel(del_frame, text=f"{("Wanna DELETE something 😢").title()}", font=(font_family[2], 13)).place(relx=0.01, rely=0.01)
        
        category_list = []
        lesson_list = []
        category_dict = {}  # Initialize as empty dictionary

        def load_category():
            nonlocal category_dict, category_list
            category_list.clear()
            with open("./SaveFiles/Lessons.json", 'r') as file:
                category_dict = json.load(file)
                category_list = list(category_dict.keys())  # Get category names
                
        load_category()

        def load_lesson(value):
            nonlocal lesson_list
            lesson_list.clear()
            if value in category_dict:
                details = category_dict[value]
                lesson_list = list(details.keys())
                del_lesson.configure(values = lesson_list)

        def del_function():
            title = category.get()
            lesson = del_lesson.get()

            if not title:
                return  # No category selected

            with open("./SaveFiles/Lessons.json", 'r+') as file:
                category_dict = json.load(file)

                if everything.get():  # Delete entire category
                    if title in category_dict:
                        del category_dict[title]
                else:  # Delete specific lesson in category
                    if title in category_dict and lesson in category_dict[title]:
                        del category_dict[title][lesson]

                file.seek(0)
                json.dump(category_dict, file, indent=2)
                file.truncate()
            # Reload category list and update dropdown widget
            load_category()
            category.configure(values=category_list)
                
        ctk.CTkLabel(del_frame, text=f"{("Category:").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.2)
        category = ctk.CTkComboBox(del_frame, corner_radius=0, values=category_list, command=lambda e: load_lesson(e))
        category.place(relx=0.21, rely=0.2)
        
        everything = ctk.BooleanVar(value=False)
        ctk.CTkLabel(del_frame, text=f"{("Just The category:").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.39)
        ctk.CTkCheckBox(del_frame, text="", border_width=1,variable=everything,checkbox_width=20,checkbox_height=20, corner_radius=5).place(relx=0.4, rely=0.4)
        
        ctk.CTkLabel(del_frame, text=f"{("Lesson To DElete:").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.58)
        del_lesson = ctk.CTkComboBox(del_frame, corner_radius=0, values=lesson_list)
        del_lesson.place(relx=0.37, rely=0.58)
        
        save_btn = ctk.CTkButton(del_frame, text="SAVE",corner_radius=0,font=(font_family[0], 12),command= del_function)
        save_btn.place(anchor="ne", relx=0.99, rely=0.82, relwidth=0.1)
        
class Theme_panel():
    def __init__(self, master):
        self.main_frame = ctk.CTkFrame(master, corner_radius=0)
        self.main_frame.place(relx=(1/4), rely=0.01, relwidth=(3/4)-0.01, relheight=0.98)

class File_panel():
    def __init__(self, master):
        self.main_frame = ctk.CTkFrame(master, corner_radius=0)
        self.main_frame.place(relx=(1/4), rely=0.01, relwidth=(3/4)-0.01, relheight=0.98)
        self.create_import_frame(self.main_frame)
        self.create_export_frame(self.main_frame)
        
    def create_import_frame(self, main_frame):
        import_frame = ctk.CTkFrame(main_frame,corner_radius=0, border_color=border_color, border_width=border_width)
        import_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.49)
        
        ctk.CTkLabel(import_frame, text=f"{("Wanna Import something 😊").title()}", font=(font_family[2], 13)).place(relx=0.01, rely=0.01)
        
        class Btn():
            def __init__(self, master,text, x, command=lambda: print("debug")):
                btn = ctk.CTkButton(import_frame, text=text, corner_radius=0, font=(font_family[0], 20), command=command)
                btn.place(relx=x, rely=0.94, relwidth=(1/3), relheight=(3/4), anchor="sw")
                
        settings_btn = Btn(import_frame,"SETTINGS", 0.005)
        lessons_btn = Btn(import_frame,"LESSONS", (1/3), lambda : import_function("./SaveFiles/lessons.json") )
        stats_btn = Btn(import_frame,"STATISTICS", (2/3))
        
        def import_function(path):
            with open(path, "+r") as rf:
                file = filedialog.askopenfile(filetypes=[("JSON", ".json")])
                rf.seek(0)
                rf.write(file.read())
                rf.truncate()
                
        
       
    
    def create_export_frame(self, main_frame):
        export_frame = ctk.CTkFrame(main_frame, corner_radius=0,border_color=border_color, border_width=border_width)
        export_frame.place(relx=0.01, rely=0.51, relwidth=0.98, relheight=0.49)
        
        ctk.CTkLabel(export_frame, text=f"{("Wanna Export something 😁").title()}", font=(font_family[2], 13)).place(relx=0.01, rely=0.01)
        
        class Btn():
                def __init__(self, master,text, x, command = lambda: print("here")):
                    btn = ctk.CTkButton(master, text=text, corner_radius=0, font=(font_family[0], 20), command=command)
                    btn.place(relx=x, rely=0.94, relwidth=(1/3), relheight=(3/4), anchor="sw")
                    
        settings_btn = Btn(export_frame,"SETTINGS", 0.005,lambda : export_function("./Settings/settings.json"))
        lessons_btn = Btn(export_frame,"LESSONS", (1/3), lambda : export_function("./SaveFiles/lessons.json"))
        stats_btn = Btn(export_frame,"STATISTICS", (2/3),lambda : export_function("./SaveFiles/Stats.json"))
        
        
        def export_function(path):
            with open(path, "r") as file:
                contents = file.read()
                export = filedialog.asksaveasfile(defaultextension=".json", filetypes=[
                   ( "JSON", ".json")])
                export.write(contents)
                export.close()