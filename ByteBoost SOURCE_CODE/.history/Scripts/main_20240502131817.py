from typing import Tuple
from modules import *
from Widgets.daily import *
from Widgets.Into import *
from Widgets.daily import *

windows_background = "#111"

class Analytic(ctk.CTk):
    def __init__(self, fg_color=windows_background, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry("900x630")
        self.resizable(width=False, height=False)
        self.title("Analytic")
        Intro
        DailyProgressApp(self)
        
        self.mainloop()
        
Analytic()