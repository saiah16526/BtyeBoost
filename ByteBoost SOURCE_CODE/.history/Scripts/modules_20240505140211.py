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
import itertools
# print("Current Directory:", os.getcwd())


#####SETTINGS####3
BORDER_COLOR = "#88aa77"
BACKGROUND = "#111"
DAILY_BACKGROUND = BACKGROUND
IMG_BACKGROUND = BACKGROUND
INTRO_BACKGROUND = BACKGROUND
SETTINGS_BACKGROUND = BACKGROUND
PANEL_BACKGROUND = BACKGROUND
SETTINGS_BACKGROUND = BACKGROUND
TIMER_BACKGROUND = BACKGROUND
STATS_BACKGROUND = BACKGROUND
FONT_COLOR = BORDER_COLOR
FONT_FAMILY = ['JetBrains Mono', "unionagrochem", "Poppins"]
PERCENTAGE_COLOR = BORDER_COLOR
PERCENTAGE_BACKGROUND = "#666666"
PROGRESS_THEME = "#ccc"

def load_settings():
    with open("./Settings/settings.json", 'r') as file:
        settings_dict = json.load(file)
        

class Lesson:
    def __init__(self, name, properties):
        self.name = name
        self.duration = properties["duration"]
        self.count = properties["total_count"]
        self.percentage = self.duration * self.count
        
        