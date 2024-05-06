from modules import *

BORDER_WIDTH = 1
BORDER_RADIUS = 4
    
    
class ImgWrapper(ctk.CTkFrame):
    def __init__(self, master):
        self.SETTINGS = load_settings()
        super().__init__(master, border_width=BORDER_WIDTH, border_color=self.SETTINGS["BORDER_COLOR"], corner_radius=BORDER_RADIUS)
        # Image Wrapper
        global image,image_Tk
        self.place(relx=0.03, rely=0, relwidth=0.62, relheight=0.6, anchor="nw")
        canvas = tk.Canvas(self, bd=0, highlightthickness=0, background=self.SETTINGS["BACKGROUND"])
        canvas.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.99, anchor="nw")
        # Loading and displaying image
        image = Image.open(resource_path(".\\Images\\python-futuristic-5120x2880-15994.png")).resize((590, 400))
        image_Tk = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, image=image_Tk, anchor="nw")
        # Text overlay on the image
        canvas.create_text(10, 315, anchor="nw", justify="left", text="Unreal Engine", fill=self.SETTINGS["BORDER_COLOR"], font=("Poppins", 20))
        canvas.create_text(10, 350, anchor="nw", justify="left", text="Has Just Resealed the new version", fill=self.SETTINGS["BORDER_COLOR"], font=("Poppins", 10))
        # End of Image Wrapper