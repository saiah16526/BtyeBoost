from modules import *

BORDER_WIDTH = 1
BORDER_RADIUS = 4


class Panel(ctk.CTkFrame):
        def __init__(self, master):
            super().__init__(master,fg_color=BACKGROUND, border_width=BORDER_WIDTH, border_color=BORDER_COLOR, corner_radius=BORDER_RADIUS)
            self.is_collapsed = True  # Boolean variable to track the panel state (collapsed or expanded)
            # Create the main frame for the panel
            #image
            self.expand_img = ImageTk.PhotoImage(Image.open("./Images/Icons/expand.png").resize((40, 40)))
            self.collapse_img = ImageTk.PhotoImage(Image.open("./Images/Icons/collapse.png").resize((40, 40)))
            settings_img = ImageTk.PhotoImage(Image.open("./Images/Icons/settings.png").resize((30, 30)))
            
            self.toggle_button = ctk.CTkButton(self,fg_color=BACKGROUND, hover_color=BACKGROUND, text="",image=self.expand_img ,corner_radius=5, command=self.toggle_panel_view)
            self.settings_button = ctk.CTkButton(self, text="",fg_color=BACKGROUND, hover_color=BACKGROUND, image=settings_img,font=(FONT_FAMILY[0], 13),width=10, corner_radius=5, command=self.toggle_settings_view)
            self.place(relx=0, rely=0, relwidth=0.037, relheight=1, anchor="nw")
            self.toggle_button.place(relx=-0.05, rely=0, anchor="nw", relwidth=1)
            self.lessons_panel = self.LessonGrid(self, master)  # Create the lesson panel
            self.parent = master
        def toggle_panel_view(self):
            self.is_collapsed = not self.is_collapsed
            self.update_panel_layout()

        def update_panel_layout(self):
            if self.is_collapsed:
                # Collapse the panel
                self.place(relx=0, rely=0, relwidth=0.037, relheight=1, anchor="nw")
                self.toggle_button.place(relx=-0.05, rely=0, anchor="nw", relwidth=1)
                self.toggle_button.configure(image = self.expand_img)
                self.lessons_panel.frame.place_forget()  # Hide lessons panel
                self.settings_button.place_forget()
            else:
                # Expand the panel
                self.place(relx=0, rely=0, relwidth=0.3, relheight=1, anchor="nw")
                self.toggle_button.place(relx=0.99, rely=0.001, anchor="ne", relwidth=0.2)
                self.toggle_button.configure(image = self.collapse_img)
                self.settings_button.place(relx=0.01, rely=0.001, anchor="nw")
                self.lessons_panel.frame.place(relwidth=0.98, relheight=0.94, rely=0.06)  # Show lessons panel
                
        def toggle_settings_view(self):
            (self.parent.settings.show_panel())
                
        class LessonGrid:
            def __init__(self, master, parent):
                self.parent = parent
                self.frame = ctk.CTkScrollableFrame(master, fg_color=
                BACKGROUND, corner_radius=BORDER_RADIUS)
                self.frame.place(relx=0.01, rely=0.07, relwidth=0, relheight=0.93, anchor="nw")
                self.frame.columnconfigure((0, 1), weight=1)
                ctk.CTkLabel(self.frame, text="Available Lessons").grid(column=0, row=0, columnspan=2)

                self.load_lessons()  # Load lessons data on initialization

            def load_lessons(self):
                # Load lessons data from a JSON file
                lessons_dict = {}
                try:
                    with open("./SaveFiles/lessons.json", 'r') as r:
                        lessons_dict = json.load(r)
                except FileNotFoundError:
                    print("Lessons file not found.")

                self.create_language_packs(lessons_dict)

            def create_language_packs(self, lessons_dict):
                col = 0
                row = 1
                # Create multiple language pack widgets (grid layout)
                for key, value in lessons_dict.items():
                    if col > 1:
                        row += 1
                        col = 0
                    LangPack(self.frame, col=col, row=row, title=key, subtitles=value, parent=self.parent)  # Create a language pack widget
                    col += 1  # Increment column for the next widget

class LangPack:
    def __init__(self, master, col, row, title, subtitles, parent):
        self.frame = ctk.CTkFrame(master, fg_color=BACKGROUND, border_color=BORDER_COLOR, border_width=BORDER_WIDTH, corner_radius=BORDER_RADIUS)
        self.frame.grid(column=col, row=row, sticky="nswe")
        ctk.CTkLabel(self.frame, text=f"{title.upper()}", fg_color=PERCENTAGE_BACKGROUND, text_color="#201").pack(fill="both")
        self.grand_parent = parent
        self.rad_btn = tk.StringVar()
        self.create_radio_buttons(subtitles)

    def create_radio_buttons(self, subtitles):
        for key in subtitles.keys():
            ctk.CTkRadioButton(
                self.frame,
                text_color=FONT_COLOR,
                radiobutton_height=15,
                radiobutton_width=15,
                border_color=BORDER_COLOR,
                text=key,
                fg_color="#FFA500",
                bg_color=BACKGROUND,
                border_width_checked=2,
                border_width_unchecked=2,
                variable=self.rad_btn,
                value=key,
                command=lambda : self.update_selection(self.grand_parent)
            ).pack(fill="both", expand=True)

    def update_selection(self, parent):
        parent.counter.lang.set(self.rad_btn.get())
