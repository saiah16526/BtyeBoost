import tkinter as tk
from PIL import Image, ImageTk

class TransparentImageWidget(tk.Label):
    def __init__(self, parent, image_path, transparent_color=None, **kwargs):
        """
        Initialize the TransparentImageWidget.

        Args:
            parent (tk.Widget): The parent widget to place the TransparentImageWidget within.
            image_path (str): The path to the image file to display on the widget.
            transparent_color (tuple, optional): The RGB tuple specifying the color to make transparent. Defaults to None.
            **kwargs: Additional keyword arguments to configure the widget (e.g., text, width, height, bg).
        """
        super().__init__(parent, **kwargs)
        self.image_path = image_path
        self.transparent_color = transparent_color
        self.load_and_display_image()

    def load_and_display_image(self):
        """
        Load the image from the specified path and display it on the widget with transparency.
        """
        # Open the image using Pillow
        image = Image.open(self.image_path)

        # Make specified transparent color (if provided)
        if self.transparent_color:
            image = self.make_color_transparent(image, self.transparent_color)

        # Convert the modified image to a Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image)

        # Configure the widget to display the image
        self.configure(image=photo)
        self.image = photo  # Keep a reference to prevent garbage collection

    def make_color_transparent(self, image, transparent_color):
        """
        Make the specified color transparent in the given image.

        Args:
            image (PIL.Image.Image): The input PIL image.
            transparent_color (tuple): The RGB tuple specifying the color to make transparent.

        Returns:
            PIL.Image.Image: The modified PIL image with transparency.
        """
        # Convert the image to RGBA mode (with alpha channel)
        image = image.convert("RGBA")

        # Get the image data as a list of pixels
        data = image.getdata()

        # Create a new list to store modified pixel data
        new_data = []
        for item in data:
            # Check if the pixel color matches the transparent color
            if item[:3] == transparent_color:
                # If the color matches, set the alpha value to 0 (transparent)
                new_data.append((item[0], item[1], item[2], 0))
            else:
                # Otherwise, keep the original pixel color
                new_data.append(item)

        # Update the image data with the modified pixel list
        image.putdata(new_data)
        return image

# Usage example:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Transparent Image Widget Example")

    # Specify the path to the image file
    image_path = "./Images/Black.png"

    # Specify the transparent color (RGB tuple) - e.g., (255, 255, 255) for white
    transparent_color = (255, 255, 255)  # White color (RGB value)

    # Create a TransparentImageWidget instance
    transparent_widget = TransparentImageWidget(root, image_path, transparent_color)
    transparent_widget.pack(padx=10, pady=10)

    root.mainloop()
