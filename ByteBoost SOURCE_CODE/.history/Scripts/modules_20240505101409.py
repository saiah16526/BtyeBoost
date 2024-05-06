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

# print("Current Directory:", os.getcwd())

class Lesson:
    def __init__(self, name, properties):
        self.name = name
        self.duration = properties["duration"]
        self.count = properties["total_count"]
        self.percentage = self.duration * self.count
        
        