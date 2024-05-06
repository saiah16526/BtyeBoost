import tkinter as tk
from tkinter import filedialog
import ttkbootstrap 
from ttkbootstrap import ttk
import customtkinter as ctk 
import random
import math
from PIL import Image, ImageTk
from time import strftime
import datetime
import json
import os
from Widgets.daily import *
from Widgets.Into import *
from Widgets.panel import *
from Widgets.mini_stats import *
from Widgets.timer import *
from Widgets.img_wrapper import *
from Widgets.settings_panel import *
from Widgets.mega_stats import *
# print("Current Directory:", os.getcwd())

class Lesson:
    def __init__(self, name, properties):
        self.name = name
        self.duration = properties["duration"]
        self.count = properties["total_count"]
        self.percentage = self.duration * self.count
        
        