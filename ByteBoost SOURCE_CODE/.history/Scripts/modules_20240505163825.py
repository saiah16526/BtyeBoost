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


def load_settings():
    global BACKGROUND , BORDER_COLOR,FONT_COLOR,FONT_FAMILY,PERCENTAGE_BACKGROUND,PERCENTAGE_COLOR,PROGRESS_THEME
    with open("./Settings/settings.json", 'r') as file:
        settings_dict = json.load(file)
    return settings_dict





class Lesson:
    def __init__(self, name, properties):
        self.name = name
        self.duration = properties["duration"]
        self.count = properties["total_count"]
        self.percentage = self.duration * self.count
        
        