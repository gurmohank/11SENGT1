import customtkinter as ctk
from PIL import Image

#set some window properties
app_home = ctk.CTk()
app_home.title("Math Magic") #window title

#specific colours
lightbg = "#f1e5d2"
darkbg = "#000000"

appearance_mode = ctk.get_appearance_mode()

#default visuals based on systems current mode
if appearance_mode == "light":
    app_home.config(bg=lightbg)
    bg_image = "bg_light.png"
    setting_icon_image = "settings_icon_light.png"
    label_bg_col = lightbg
else:
    app_home.config(bg=darkbg)
    bg_image = "bg_dark.png"
    setting_icon_image = "settings_icon_dark.png"
    label_bg_col = darkbg


#all images and icons used
bg = ctk.CTkImage(Image.open(bg_image),size=(800, 600))
settingicon = ctk.CTkImage(Image.open(setting_icon_image), size=(100,100))


#placing the background image (light mode)
lightbg_label = ctk.CTkLabel(app_home, text="", image=bg)
lightbg_label.place(x=300, y=0)

#placing settings icon
settingicon_label = ctk.CTkLabel(app_home, text="", image=settingicon, bg_color=label_bg_col)
settingicon_label.place(x=0, y=0)

#run the application
app_home.mainloop()







