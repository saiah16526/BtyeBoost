from modules import *

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
        self.place(relx=0.2, rely=0.2, relheight=0.6, relwidth=0.6)
        frame = ctk.CTkFrame(self)
        frame.place(relx=0.01, rely=0.01, relwidth=(1/4), relheight=0.98)
        self.create_buttons(frame, text="THEME")
        self.create_buttons(frame, text="LESSONS")
        self.create_buttons(frame, text="FILE SYS")
        self.create_buttons(frame, text="RESET")
        
        Lessons_panel(self)
        
    def create_buttons(self, master, text):
        self.theme_btn = ctk.CTkButton(master,corner_radius=0, text=text, font=(font_family[0], 20))
        self.theme_btn.pack(expand=True, fill="both", pady=1)
        
        
class Lessons_panel():
    def __init__(self, master):
        main_frame = ctk.CTkFrame(master, corner_radius=0)
        main_frame.place(relx=(1/4), rely=0.01, relwidth=(3/4)-0.01, relheight=0.98)
        self.create_add_frame(main_frame)
        self.create_del_frame(main_frame)
        
        #ADD menu
    def create_add_frame(self, main_frame):
        add_frame = ctk.CTkFrame(main_frame,corner_radius=0, border_color=border_color, border_width=border_width)
        add_frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.49)
        
        ctk.CTkLabel(add_frame, text=f"{("Wanna Add a new Lesson to track").title()}", font=(font_family[2], 13)).place(relx=0.01, rely=0.01)
        
        category_list = []
        def load_lessons():
            with open("./SaveFiles/Lessons.json", "+r") as file:
                category_dict = json.load(file)
                for category, _ in category_dict.items():
                    category_list.append(category)
        
        ctk.CTkLabel(add_frame, text=f"{("Category:").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.2)
        category = ctk.CTkComboBox(add_frame,values=category_list, corner_radius=0)
        category.place(relx=0.21, rely=0.2)
        
        ctk.CTkLabel(add_frame, text=f"{("New category:").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.39)
        new_category = ctk.CTkEntry(add_frame, placeholder_text="Category not Enlisted !!!", corner_radius=0, border_width=1)
        new_category.place(relx=0.3, rely=0.39)
        
        ctk.CTkLabel(add_frame, text=f"{("Lesson To Add:").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.58)
        new_lesson = ctk.CTkEntry(add_frame, placeholder_text="Node.js", corner_radius=0, border_width=1)
        new_lesson.place(relx=0.3, rely=0.58)
        
        
        save_btn = ctk.CTkButton(add_frame, text="SAVE",corner_radius=0,font=(font_family[0], 12))
        save_btn.place(anchor="ne", relx=0.99, rely=0.82, relwidth=0.1)
        
         #Remove menu
    def create_del_frame(self, main_frame):
        del_frame = ctk.CTkFrame(main_frame, corner_radius=0,border_color=border_color, border_width=border_width)
        del_frame.place(relx=0.01, rely=0.51, relwidth=0.98, relheight=0.49)
        
        ctk.CTkLabel(del_frame, text=f"{("Wanna DELETE something 😢").title()}", font=(font_family[2], 13)).place(relx=0.01, rely=0.01)
        
        ctk.CTkLabel(del_frame, text=f"{("Category:").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.2)
        category = ctk.CTkComboBox(del_frame, corner_radius=0)
        category.place(relx=0.21, rely=0.2)
        
        ctk.CTkLabel(del_frame, text=f"{("Just The category:").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.39)
        ctk.CTkCheckBox(del_frame, text="", border_width=1,checkbox_width=20,checkbox_height=20, corner_radius=5).place(relx=0.4, rely=0.4)
        
        ctk.CTkLabel(del_frame, text=f"{("Lesson To DElete:").upper()}", font=(font_family[0], 13)).place(relx=0.01, rely=0.58)
        del_lesson = ctk.CTkComboBox(del_frame, corner_radius=0)
        del_lesson.place(relx=0.37, rely=0.58)
        
        save_btn = ctk.CTkButton(del_frame, text="SAVE",corner_radius=0,font=(font_family[0], 12))
        save_btn.place(anchor="ne", relx=0.99, rely=0.82, relwidth=0.1)