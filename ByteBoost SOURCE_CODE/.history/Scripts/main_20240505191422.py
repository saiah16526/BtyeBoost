from modules import *
from Widgets.daily import *
from Widgets.Into import *
from Widgets.panel import *
from Widgets.mini_stats import *
from Widgets.timer import *
from Widgets.img_wrapper import *
from Widgets.settings_panel import *
from Widgets.mega_stats import *

windows_background = "transparent"

class ByteBoost(ctk.CTk):
    def __init__(self, **kwargs):
        self.SETTINGS = load_settings()
        super().__init__(fg_color = self.SETTINGS["BACKGROUND"], **kwargs)
        self.geometry("910x660")
        self.resizable(width=False, height=False)
        self.title("ByteBoost")
        self.intro = Into_page(self)
        self.daily = DailyProgressApp(self)
        self.side_stats = StatsWrapper(self)
        self.counter = TimerFrame(self)
        self.img = ImgWrapper(self)
        self.panel = Panel(self)
        self.settings = Settings(self)
        self.statistics = Statistics(self)
        self.mainloop()
        
ByteBoost()