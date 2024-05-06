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
        self.geometry("910x650")
        self.resizable(width=False, height=False)
        self.title("ByteBoost")
        self.intro = Into_page(self)
        self.daily = DailyProgressApp(self)
        self.side_stats = StatsWrapper(self)
        self.counter = TimerFrame(self)
        ImgWrapper(self)
        self.panel = Panel(self)
        self.settings = Settings(self)
        self.statistics = Statistics(self)
        self.mainloop()
        
ByteBoost()