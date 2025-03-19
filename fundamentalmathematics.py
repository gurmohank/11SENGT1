import customtkinter as ctk
from PIL import Image
import sys  

#set some window properties
app_home = ctk.CTk()

# Set some window properties
app_home.title("Math Magic")  #window title
app_home.geometry("700x400")  #set the window size

#load images for both modes (light and dark)
try:
    lightbg_img = ctk.CTkImage(Image.open("home_image_lightm.png"))
except Exception as e:
    print(f"Error loading light mode image: {e}")
    lightbg_img = None  # sets to None if image loading fails
try:
    darkbg_img = ctk.CTkImage(Image.open("home_image_darkm.png"))
except Exception as e:
    print(f"Error loading dark mode image: {e}")
    darkbg_img = None

# Check if images are loaded properly
if lightbg_img is None or darkbg_img is None:
    print("One or both images failed to load. Exiting application.")
    sys.exit()  # Gracefully exit the program
else:
    current_mode = "light"  # Default mode to light

    # Set the background image based on the mode
    bg_label = ctk.CTkLabel(app_home, image=lightbg_img if current_mode == "light" else darkbg_img)
    bg_label.place(relwidth=1, relheight=1)

# Run the application
app_home.mainloop()
