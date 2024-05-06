from modules import *
 
from Scripts.Widgets.Into import *
from Scripts.Widgets.panel import *
from Scripts.Widgets.mini_stats import *
from Scripts.Widgets.timer import *
from Scripts.Widgets.img_wrapper import *
from Scripts.Widgets.settings_panel import *
from Scripts.Widgets.mega_stats import *


class ByteBoost(ctk.CTk):
    def __init__(self, **kwargs):
        self.SETTINGS = load_settings()
        super().__init__(fg_color = self.SETTINGS["BACKGROUND"], **kwargs)
        self.geometry("910x660")
        self.resizable(width=False, height=False)
        self.title("ByteBoost")
        self.iconbitmap(resource_path(".\\Images\\icon.ico"))
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