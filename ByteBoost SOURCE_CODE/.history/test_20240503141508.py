import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class TransparentWidget:
    def __init__(self, parent, widget_type, image_path, transparent_color=None, **kwargs):
        """
        Initialize the TransparentWidget.

        Args:
            parent (tk.Widget): The parent widget to place the TransparentWidget within.
            widget_type (tk.Widget): The type of Tkinter widget to create (e.g., tk.Label, tk.Button, tk.Frame).
            image_path (str): The path to the image file to display on the widget.
            transparent_color (tuple, optional): The RGB tuple specifying the color to make transparent. Defaults to None.
            **kwargs: Additional keyword arguments to configure the widget (e.g., text, width, height, bg).
        """
        self.parent = parent
        self.widget_type = widget_type
        self.image_path = "./Images/Black.png"
        self.transparent_color = transparent_color
        self.widget = self.create_widget(**kwargs)

    def create_widget(self, **kwargs):
        """
        Dynamically create the specified Tkinter widget and load the image on it.

        Args:
            **kwargs: Additional keyword arguments to configure the widget.

        Returns:
            tk.Widget: The created Tkinter widget with the image displayed.
        """
        # Create the specified Tkinter widget instance
        widget = self.widget_type(self.parent, **kwargs)

        # Load and display the image on the widget
        self.load_and_display_image(widget)

        return widget

    def load_and_display_image(self, widget):
        """
        Load the image from the specified path and display it on the widget with transparency.

        Args:
            widget (tk.Widget): The Tkinter widget on which to display the image.
        """
        # Open the image using Pillow
        image = Image.open(self.image_path)

        # Make specified transparent color (if provided)
        if self.transparent_color:
            image = self.make_color_transparent(image, self.transparent_color)

        # Convert the modified image to a Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image)

        # Configure the widget to display the image
        widget.configure(image=photo)
        widget.image = photo  # Keep a reference to prevent garbage collection

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
    root.title("Transparent Widget Example")

    # Specify the path to the image file
    image_path = "path_to_your_image_file.png"

    # Specify the transparent color (RGB tuple) - e.g., (0, 0, 255) for blue
    transparent_color = (0, 0, 255)  # Example: Blue color (RGB value)

    # Create a TransparentWidget instance with a Label widget
    transparent_label = TransparentWidget(root, ctk.CTkLabel, image_path, transparent_color)
    transparent_label.widget.pack(padx=10, pady=10)

    # Create a TransparentWidget instance with a Button widget
    transparent_button = TransparentWidget(root, tk.Button, image_path, transparent_color, text="Click Me")
    transparent_button.widget.pack(padx=10, pady=10)

    # Create a TransparentWidget instance with a Frame widget
    transparent_frame = TransparentWidget(root, tk.Frame, image_path, transparent_color, width=200, height=200, bg="white")
    transparent_frame.widget.pack(padx=10, pady=10)

    root.mainloop()
