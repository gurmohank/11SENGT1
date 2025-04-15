import customtkinter as ctk
from PIL import Image

#set some window properties
app_home = ctk.CTk()
app_home.title("Math Magic") #window title

lightbg = "#f1e5d2"
app_home.config(bg=lightbg)

bg1 = ctk.CTkImage(Image.open("bg_light.png"), size=(800, 600))
lightbgimg = ctk.CTkLabel(app_home, text="", image=bg1)
lightbgimg.pack()

#run the application
app_home.mainloop()







