from modules import *

border_color = "#88aa77"
border_width = 1
border_radius = 4
Img_background = "#111"
font_color = border_color
font_family = ['JetBrains Mono', "unionagrochem"]
percentage_color = border_color
percentage_background = "#666"
    
    
class ImgWrapper(ctk.CTkFrame):
    def __init__(self, master, fg_color=Img_background):
        super().__init__(master)
        # Image Wrapper
        self.place(relx=0.03, rely=0, relwidth=0.62, relheight=0.6, anchor="nw")
        canvas = tk.Canvas(self, bd=0, highlightthickness=0, background=Img_background)
        canvas.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.99, anchor="nw")
        # Loading and displaying image
        image = Image.open("./Images/land-rover-defender-5120x2880-15603.jpg").resize((590, 400))
        image_Tk = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, image=image_Tk, anchor="nw")
        # Text overlay on the image
        # canvas.create_text(10, 315, anchor="nw", justify="left", text="Unreal Engine", fill=font_color, font=("Poppins", 20))
        # canvas.create_text(10, 350, anchor="nw", justify="left", text="Has Just Resealed the new version", fill=font_color, font=("Poppins", 10))
        # End of Image Wrapper