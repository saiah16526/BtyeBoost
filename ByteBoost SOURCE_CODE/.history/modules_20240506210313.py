import tkinter as tk
from tkinter import filedialog, messagebox
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
import sys
# print("Current Directory:", os.getcwd())

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def load_settings(window = ""):
    global BACKGROUND , BORDER_COLOR,FONT_COLOR,FONT_FAMILY,PERCENTAGE_BACKGROUND,PERCENTAGE_COLOR,PROGRESS_THEME
    with open(resource_path("./Settings/settings.json"), 'r') as file:
        settings_dict = json.load(file)
    if window != "":
        window.configure(fg_color=settings_dict["BACKGROUND"])
    return settings_dict




class Lesson:
    def __init__(self, name, properties):
        self.name = name
        self.duration = properties["duration"]
        self.count = properties["total_count"]
        self.percentage = self.duration * self.count
        
        