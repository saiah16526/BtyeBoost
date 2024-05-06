from modules import *
from Widgets.daily import *
from Widgets.Into import *
from Widgets.panel import *
from Widgets.mini_stats import *
from Widgets.timer import *
from Widgets.img_wrapper import *
from Widgets.settings_panel import *
from Widgets.mega_stats import *

windows_background = "#111"

class ByteBoost(ctk.CTk):
    def __init__(self, fg_color=windows_background, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry("900x630")
        # self.resizable(width=False, height=False)
        self.title("ByteBoost")
        Into_page(self)
        DailyProgressApp(self)
        self.side_stats = StatsWrapper(self)
        self.counter = TimerFrame(self)
        ImgWrapper(self)
        Panel(self)
        self.settings = Settings(self)
        # Statistics(self)
        self.mainloop()
        
ByteBoost()