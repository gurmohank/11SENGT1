import customtkinter as ctk
from PIL import Image

#set some window properties
app_home = ctk.CTk()
app_home.title("Math Magic") #window title

#specific colours
lightbg = "#f1e5d2"
darkbg = "#000000"
pastel_green = "#C8E6C9"
forest_green = "#1B5E20"
berry_pink = "#EC407A"
light_butter = "#faf1b9"

#get current mode for system using custom tkinters pre-built function
appearance_mode = ctk.get_appearance_mode()

#default visuals based on systems current mode
if appearance_mode == "light":
    app_home.config(bg=lightbg)
    widget_bg_col = lightbg
    bg_image = "bg_light.png"
    setting_icon_image = "settings_icon_light.png"
    launch_icon_image = "launch_icon_light.png"
    help_icon_image = "help_icon_light.png"
    back_icon_image = "back_icon_light.png"
    cross_icon_image = "cross_icon_light.png"
    guide_char_image = "guide_character_light.png"
    speech_image = "speech_light.png"
else:
    app_home.config(bg=darkbg)
    widget_bg_col = darkbg
    bg_image = "bg_dark.png"
    setting_icon_image = "settings_icon_dark.png"
    launch_icon_image = "launch_icon_dark.png"
    help_icon_image = "help_icon_dark.png"
    back_icon_image = "back_icon_dark.png"
    cross_icon_image = "cross_icon_dark.png"
    guide_char_image = "guide_character_dark.png"
    speech_image = "speech_dark.png"

#all images and icons used
bg = ctk.CTkImage(Image.open(bg_image),size=(900, 700))
settingicon = ctk.CTkImage(Image.open(setting_icon_image), size=(100,100))
helpicon = ctk.CTkImage(Image.open(help_icon_image), size=(115,115))
launchicon = ctk.CTkImage(Image.open(launch_icon_image), size=(102,102))
backicon = ctk.CTkImage(Image.open(back_icon_image), size=(115,115))
crossicon = ctk.CTkImage(Image.open(cross_icon_image), size=(115,115))
guidechar = ctk.CTkImage(Image.open(guide_char_image), size=(330,330))
speech = ctk.CTkImage(Image.open(speech_image), size=(400,250))

#placing the background image (home page)
lightbg_label = ctk.CTkLabel(app_home, text="", image=bg)
lightbg_label.place(x=300, y=-100)

#placing settings icon (home page)
settingicon_label = ctk.CTkLabel(app_home, text="", image=settingicon, bg_color=widget_bg_col)
settingicon_label.place(x=0, y=0)

#placing help icon (home page)
helpicon_label = ctk.CTkLabel(app_home, text="", image=helpicon, bg_color=widget_bg_col)
helpicon_label.place(x=1340, y=0)

#placing web launch icon (home page)
launchicon_label = ctk.CTkLabel(app_home, text="", image=launchicon, bg_color=widget_bg_col)
launchicon_label.place(x=1270, y=0)

#placing guide character (home page)
guidechar_label = ctk.CTkLabel(app_home, text="", image=guidechar, bg_color=widget_bg_col)
guidechar_label.place(x=-20, y=530)

#placing speech bubble (home page)
speech_label = ctk.CTkLabel(app_home, text="", image=speech, bg_color=widget_bg_col)
speech_label.place(x=210, y=400)

#buttons for modules
num_basic_mod = ctk.CTkButton(app_home, text="Number\nBasics", 
                              font=ctk.CTkFont(family="Fredoka", size=25, weight="bold"), 
                              width=230, height=180,
                              corner_radius=50,
                              fg_color=pastel_green,
                              text_color=forest_green,
                              border_width=8,
                              border_color=forest_green,
                              hover_color=light_butter,
                              bg_color=widget_bg_col)
num_basic_mod.place(x=665, y=530)

addition_mod = ctk.CTkButton(app_home, text="Addition",
                              font=ctk.CTkFont(family="Fredoka", size=25, weight="bold"), 
                              width=230, height=180,
                              corner_radius=50,
                              fg_color=pastel_green,
                              text_color=forest_green,
                              border_width=8,
                              border_color=forest_green,
                              hover_color=light_butter,
                              bg_color=widget_bg_col)
addition_mod.place(x=915, y=530)

subtraction_mod = ctk.CTkButton(app_home, text="Subtraction",
                                 font=ctk.CTkFont(family="Fredoka", size=24, weight="bold"), 
                                 width=180, height=180,
                                 corner_radius=45,
                                 fg_color=pastel_green,
                                 text_color=forest_green,
                                 border_width=8,
                                 border_color=forest_green,
                                 hover_color=light_butter,
                                 bg_color=widget_bg_col)
subtraction_mod.place(x=1165, y=530)


#run the application
app_home.mainloop()







