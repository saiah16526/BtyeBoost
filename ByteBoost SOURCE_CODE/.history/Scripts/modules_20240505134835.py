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
DAILY_BACKGROUND = "#111"
IMG_BACKGROUND = "#111"
INTRO_BACKGROUND = "#111"
FONT_COLOR = BORDER_COLOR
FONT_FAMILY = ['JetBrains Mono', "unionagrochem"]
PERCENTAGE_COLOR = BORDER_COLOR
PERCENTAGE_BACKGROUND = "#666666"

class Lesson:
    def __init__(self, name, properties):
        self.name = name
        self.duration = properties["duration"]
        self.count = properties["total_count"]
        self.percentage = self.duration * self.count
        
        