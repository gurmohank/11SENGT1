import customtkinter as ctk
from PIL import Image

#set some window properties
app_home = ctk.CTk()
app_home.title("Math Magic")  #window title
app_home.geometry("700x400")  #set the window size

lightbg = ctk.CTkImage(Image.open("bg_light.png"), size=(600, 400))

my_label = ctk.CTkLabel(app_home, text="", image=lightbg)
my_label.pack(pady=10)

# Run the application
app_home.mainloop()







