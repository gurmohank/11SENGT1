import tkinter as tk
import customtkinter #needed for class definition
import customtkinter as ctk #needed for function calls
from PIL import Image, ImageTk
from flask import Flask, render_template #'render_template' refers to built in flask function which helps display HTML content
import threading
import webbrowser
import pyttsx3
import os

#initialises app and informs it that default folders (template and static) named have been modified to following
app_home = Flask(__name__, template_folder="weblaunch", static_folder="mediaassets") #window title

#specific colours
lightbg = "#f1e5d2"
darkbg = "#000000"
pastel_green = "#C8E6C9"
forest_green = "#1B5E20"
berry_pink = "#EC407A"
light_butter = "#faf1b9"
speech_light = "#fbf4e9"
speech_dark = "#feb3e4"

#folder where media is stores
media_folder = "mediaassets/"  

#get current mode for system using custom tkinters pre-built function
appearance_mode = ctk.get_appearance_mode()

#default visuals based on systems current mode
if appearance_mode == "light":
    bg_colour=lightbg
    opp_bg = darkbg
    widget_bg_col = lightbg
    bg_image = "bg_light.png"
    setting_icon_image = "settings_icon_light.png"
    launch_icon_image = "launch_icon_light.png"
    help_icon_image = "help_icon_light.png"
    back_icon_image = "back_icon_light.png"
    cross_icon_image = "cross_icon_light.png"
    guide_char_image = "guide_character_light.png"
    speech_image = "speech_light.png"
    ten_image = "ten_light.png"
    nine_image = "nine_light.png"
    eight_image = "eight_light.png"
    seven_image = "seven_light.png"
    six_image = "six_light.png"
    five_image = "five_light.png"
    four_image = "four_light.png"
    three_image = "three_light.png"
    two_image = "two_light.png"
    one_image = "one_light.png"
else:
    bg_colour = darkbg
    opp_bg = lightbg
    widget_bg_col = darkbg
    bg_image = "bg_dark.png"
    setting_icon_image = "settings_icon_dark.png"
    launch_icon_image = "launch_icon_dark.png"
    help_icon_image = "help_icon_dark.png"
    back_icon_image = "back_icon_dark.png"
    cross_icon_image = "cross_icon_dark.png"
    guide_char_image = "guide_character_dark.png"
    speech_image = "speech_dark.png"
    ten_image = "ten_dark.png"
    nine_image = "nine_dark.png"
    eight_image = "eight_dark.png"
    seven_image = "seven_dark.png"
    six_image = "six_dark.png"
    five_image = "five_dark.png"
    four_image = "four_dark.png"
    three_image = "three_dark.png"
    two_image = "two_dark.png"
    one_image = "one_dark.png"

#all images and icons used
bg = ctk.CTkImage(Image.open(os.path.join(media_folder, bg_image)),size=(900, 700))
settingicon = ctk.CTkImage(Image.open(os.path.join(media_folder,setting_icon_image)), size=(100,100))
helpicon = ctk.CTkImage(Image.open(os.path.join(media_folder,help_icon_image)), size=(115,115))
launchicon = ctk.CTkImage(Image.open(os.path.join(media_folder,launch_icon_image)), size=(102,102))
backicon = ctk.CTkImage(Image.open(os.path.join(media_folder,back_icon_image)), size=(115,115))
crossicon = ctk.CTkImage(Image.open(os.path.join(media_folder,cross_icon_image)), size=(115,115))
guidechar = ctk.CTkImage(Image.open(os.path.join(media_folder,guide_char_image)), size=(330,330))
resized_guidechar = ctk.CTkImage(Image.open(os.path.join(media_folder,guide_char_image)), size=(230,230))
speech = ctk.CTkImage(Image.open(os.path.join(media_folder,speech_image)), size=(400,250))
ten = ctk.CTkImage(Image.open(os.path.join(media_folder,ten_image)), size=(290,300))
nine = ctk.CTkImage(Image.open(os.path.join(media_folder,nine_image)), size=(290,270))
eight = ctk.CTkImage(Image.open(os.path.join(media_folder,eight_image)), size=(290,240))
seven = ctk.CTkImage(Image.open(os.path.join(media_folder,seven_image)), size=(290,210))
six = ctk.CTkImage(Image.open(os.path.join(media_folder,six_image)), size=(290,185))
five = ctk.CTkImage(Image.open(os.path.join(media_folder,five_image)), size=(290,150))
four = ctk.CTkImage(Image.open(os.path.join(media_folder,four_image)), size=(290,120))
three = ctk.CTkImage(Image.open(os.path.join(media_folder,three_image)), size=(290,90))
two = ctk.CTkImage(Image.open(os.path.join(media_folder,two_image)), size=(290,60))
one = ctk.CTkImage(Image.open(os.path.join(media_folder,one_image)), size=(290,30))    

@app_home.route("/math_magic") #informs flask to run below function, displaying following web page
def load_webpage():
     return render_template("web_fundamentalmathematics.html") #retrieves and displays the file contents

#creates python gui window, where #content inside this class directly controls functions and appearance of the gui
class App(customtkinter.CTk):
    
    #'__init__' is a built-in function used to initialise a class
    #'self' makes sure this class can track its own attributes and functions
    def __init__(self):
        super().__init__() #makes sure the app functions as a CTK window and is properly set up before any customisations
        self.title("Math Magic")
        self.geometry("1200x800")
        self.configure(fg_color=bg_colour)
        self.current_page = "main"
        self.show_home_page()
        self.web_thread = None

    def clear_page(self):
            for widget in self.winfo_children(): #gets list of all widgets (children) inside window (parent)
                widget.destroy() #loop iterates through each widget and destroys it (removes it)

    def open_web_app(self):
        web_address = "http://127.0.0.1:5000/math_magic"
        webbrowser.open_new_tab(web_address)
        print(f"Opening {web_address} in your browser!")

    

    def show_home_page(self):
        #placing the background image (home page)
        lightbg_label = ctk.CTkLabel(self, text="", image=bg)
        lightbg_label.place(x=300, y=-100)

        #placing settings icon (home page)
        settingicon_label = ctk.CTkLabel(self, text="", image=settingicon, bg_color=widget_bg_col)
        settingicon_label.place(x=0, y=0)
        settingicon_label.bind("<Button-1>", lambda event: self.show_settings_page())


        #placing help icon (home page)
        helpicon_label = ctk.CTkLabel(self, text="", image=helpicon, bg_color=widget_bg_col)
        helpicon_label.place(x=1340, y=0)

        #placing web launch icon (home page)
        launchicon_label = ctk.CTkLabel(self, text="", image=launchicon, bg_color=widget_bg_col)
        launchicon_label.place(x=1270, y=0)
        #binds a left-click (represented as 'Button-1') to stated lambda function
        #hence executing the function, transforming label into function of a button
        launchicon_label.bind("<Button-1>", lambda event: self.open_web_app())

        #placing guide character (home page)
        guidechar_label = ctk.CTkLabel(self, text="", image=guidechar, bg_color=widget_bg_col)
        guidechar_label.place(x=-20, y=530)

        #placing speech bubble (home page)
        speech_label = ctk.CTkLabel(self, text="", image=speech, bg_color=widget_bg_col)
        speech_label.place(x=210, y=400)
        speech_text_label = ctk.CTkLabel(self, text="Hello there! Welcome to Math Magic. \nPick an option to get started!",
                                         font=ctk.CTkFont(family="Nunito", size=19),
                                         text_color=darkbg,
                                         width=55, height=70,
                                         fg_color=speech_light)
        speech_text_label.place(x=250, y=470)

        #buttons for modules
        num_basic_mod = ctk.CTkButton(self, text="Number\nBasics", 
                                    font=ctk.CTkFont(family="Fredoka", size=25, weight="bold"), 
                                    width=230, height=180,
                                    corner_radius=50,
                                    fg_color=pastel_green,
                                    text_color=forest_green,
                                    border_width=8,
                                    border_color=forest_green,
                                    hover_color=light_butter,
                                    bg_color=widget_bg_col,)
        num_basic_mod.place(x=665, y=530)

        addition_mod = ctk.CTkButton(self, text="Addition",
                                    font=ctk.CTkFont(family="Fredoka", size=25, weight="bold"), 
                                    width=230, height=180,
                                    corner_radius=50,
                                    fg_color=pastel_green,
                                    text_color=forest_green,
                                    border_width=8,
                                    border_color=forest_green,
                                    hover_color=light_butter,
                                    bg_color=widget_bg_col,
                                    command=self.show_addition_page)
        addition_mod.place(x=915, y=530)

        subtraction_mod = ctk.CTkButton(self, text="Subtraction",
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

    def show_settings_page(self):
        self.clear_page()

    def show_addition_page(self):
        self.clear_page()

        backicon_label = ctk.CTkLabel(self, text="", image=backicon, bg_color=widget_bg_col)
        backicon_label.place(x=1250, y=-10)

        helpicon_label = ctk.CTkLabel(self, text="", image=helpicon, bg_color=widget_bg_col)
        helpicon_label.place(x=1340, y=0)

        #placing guide character (home page)
        guidechar_label = ctk.CTkLabel(self, text="", image=guidechar, bg_color=widget_bg_col)
        guidechar_label.place(x=-20, y=530)

        number_stacker_a1 = ctk.CTkButton(self, text="Number Stacker",
                                        font=ctk.CTkFont(family="Fredoka", size=24, weight="bold"), 
                                        width=180, height=180,
                                        corner_radius=45,
                                        fg_color=pastel_green,
                                        text_color=forest_green,
                                        border_width=8,
                                        border_color=forest_green,
                                        hover_color=light_butter,
                                        bg_color=widget_bg_col,
                                        command=self.show_number_stacker_page)
        number_stacker_a1.place(x=450, y=500)

        sort_the_mail_a2 = ctk.CTkButton(self, text="Sort the Mail",
                                        font=ctk.CTkFont(family="Fredoka", size=24, weight="bold"), 
                                        width=270, height=180,
                                        corner_radius=45,
                                        fg_color=pastel_green,
                                        text_color=forest_green,
                                        border_width=8,
                                        border_color=forest_green,
                                        hover_color=light_butter,
                                        bg_color=widget_bg_col)
        sort_the_mail_a2.place(x=750, y=500)

    def show_number_stacker_page(self):
        self.clear_page()

        #main frame covering whole page
        main_frame = tk.Frame(self, bg=bg_colour)
        main_frame.pack(fill=tk.BOTH, expand=True)

        backicon_label = ctk.CTkLabel(main_frame, text="", image=backicon, bg_color=widget_bg_col)
        backicon_label.place(x=1340, y=-10)

        #placing guide character (number stacker page)
        guidechar_label = ctk.CTkLabel(main_frame, text="", image=resized_guidechar, bg_color=widget_bg_col)
        guidechar_label.place(x=-10, y=630)

        #speech label (number stacker page)
        speech_label = ctk.CTkLabel(main_frame, text="", image=speech, bg_color=widget_bg_col)
        speech_label.place(x=150, y=450)
        speech_text_label = ctk.CTkLabel(main_frame, text="Drag and drop different\nnumbers into the box.\nExplore how different numbers add\ntogether to give you bigger numbers!",
                                         font=ctk.CTkFont(family="Nunito", size=19),
                                         text_color=darkbg,
                                         width=55, height=70,
                                         fg_color=speech_light)
        speech_text_label.place(x=200, y=510)

        #dictionary to store og-positions for images to reset
        self.start_positions = {}

        def drag_start(event):
            widget = event.widget  # Get the widget that triggered the event
            # Save the relative position of the click inside the widget
            widget.start_x = event.x
            widget.start_y = event.y
            widget.lift()

        def drag_motion(event):
            widget = event.widget  # Get the widget that triggered the event
            # Calculate new positions relative to the cursor movement
            x = widget.winfo_x() + (event.x - widget.start_x)
            y = widget.winfo_y() + (event.y - widget.start_y)
            widget.place(x=x, y=y)

        self.ten_tkv = ImageTk.PhotoImage(Image.open(os.path.join(media_folder, ten_image)).convert("RGB").resize((435, 450)))        
        self.nine_tkv = ImageTk.PhotoImage(Image.open(os.path.join(media_folder, nine_image)).convert("RGB").resize((435, 405)))
        self.eight_tkv = ImageTk.PhotoImage(Image.open(os.path.join(media_folder, eight_image)).convert("RGB").resize((435, 360)))
        self.seven_tkv = ImageTk.PhotoImage(Image.open(os.path.join(media_folder, seven_image)).convert("RGB").resize((435, 315)))
        self.six_tkv = ImageTk.PhotoImage(Image.open(os.path.join(media_folder, six_image)).convert("RGB").resize((435, 270)))
        self.five_tkv = ImageTk.PhotoImage(Image.open(os.path.join(media_folder, five_image)).convert("RGB").resize((435, 225)))
        self.four_tkv = ImageTk.PhotoImage(Image.open(os.path.join(media_folder, four_image)).convert("RGB").resize((435, 180)))
        self.three_tkv = ImageTk.PhotoImage(Image.open(os.path.join(media_folder, three_image)).convert("RGB").resize((435, 135)))
        self.two_tkv = ImageTk.PhotoImage(Image.open(os.path.join(media_folder, two_image)).convert("RGB").resize((435, 90)))
        self.one_tkv = ImageTk.PhotoImage(Image.open(os.path.join(media_folder, one_image)).convert("RGB").resize((435, 45)))
        


        #placing all numbers
        ten_label = tk.Label(main_frame, text="", image=self.ten_tkv)
        ten_label.place(x=30, y=20)
        ten_label.bind("<Button-1>", drag_start)
        ten_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[ten_label] = (30, 20)  # add the label and its original position to dictionary


        nine_label = tk.Label(main_frame, text="", image=self.nine_tkv)
        nine_label.place(x=360, y=20)
        nine_label.bind("<Button-1>", drag_start)
        nine_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[nine_label] = (360, 20)  # add the label and its original position to dictionary

        
        eight_label = tk.Label(main_frame, text="", image=self.eight_tkv)
        eight_label.place(x=660, y=20)
        eight_label.bind("<Button-1>", drag_start)
        eight_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[eight_label] = (660, 20)  # add the label and its original position to dictionary

        
        seven_label = tk.Label(main_frame, text="", image=self.seven_tkv)
        seven_label.place(x=960, y=20)
        seven_label.bind("<Button-1>", drag_start)
        seven_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[seven_label] = (960, 20)  # add the label and its original position to dictionary

    
        six_label = tk.Label(main_frame, text="", image=self.six_tkv)
        six_label.place(x=1140, y=250)
        six_label.bind("<Button-1>", drag_start)
        six_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[six_label] = (1140, 20)  # add the label and its original position to dictionary


        five_label = tk.Label(main_frame, text="", image=self.five_tkv)
        five_label.place(x=845, y=285)
        five_label.bind("<Button-1>", drag_start)
        five_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[five_label] = (845, 285)  # add the label and its original position to dictionary


        four_label = tk.Label(main_frame, text="", image=self.four_tkv)
        four_label.place(x=550, y=315)
        four_label.bind("<Button-1>", drag_start)
        four_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[four_label] = (550, 315)  # add the label and its original position to dictionary


        three_label = tk.Label(main_frame, text="", image=self.three_tkv)
        three_label.place(x=255, y=345)
        three_label.bind("<Button-1>", drag_start)
        three_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[three_label] = (225, 345)  # add the label and its original position to dictionary


        two_label = tk.Label(main_frame, text="", image=self.two_tkv)
        two_label.place(x=-40, y=345)
        two_label.bind("<Button-1>", drag_start)
        two_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[two_label] = (-40, 345)  # add the label and its original position to dictionary


        one_label = tk.Label(main_frame, text="", image=self.one_tkv)
        one_label.place(x=-40, y=410)
        one_label.bind("<Button-1>", drag_start)
        one_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[one_label] = (-40, 410)  # add the label and its original position to dictionary


        def reset_pos(start_positions):
            for label, (x, y) in start_positions.items():
                label.place(x=x, y=y)

        reset_pos_button = ctk.CTkButton(main_frame, text="Reset", command=lambda: reset_pos(self.start_positions))        
        reset_pos_button.place(x=600, y=700)

        #canvas set up
        num_canvas = ctk.CTkCanvas(main_frame, width=905, height=455, bg=opp_bg)
        num_canvas.place(x=1250, y=930)
        
        def draw_vertical_line(event=None):
            canvas_width = num_canvas.winfo_width()
            canvas_height = num_canvas.winfo_height()
            middle_x = canvas_width // 2
            num_canvas.create_line(middle_x, 0, middle_x, canvas_height, fill="black", width=2)

        num_canvas.bind("<Configure>", draw_vertical_line)



#all of the following runs the application

#ensures code is only executed if run directly, not if its imported as a module
if __name__ == "__main__":

    #creates instance of the 'App' class, essentially initliasing it
    app = App()

    #starts flask in seperate thread so it doesn't interfere with the gui, as gui would freeze while flask ran
    #'target=app_home' launches flask web server
    #kwargs (keyboard arguments) passes parameters to a function
    #'"debug":True' enables the debug mode, meaning any changes in code are automatically reflected as server reloads (reflects a proper production for users)
    #'' stops flask from reloading twice, avoiding redundancy/duplicate processes
    app.web_thread = threading.Thread(target=app_home.run, kwargs={"debug":True, "use_reloader": False})
    
    #marks thread as a daemon, meaning it will automatically close when gui is closed (needed so flask doesn't continue to run after gui is closed)
    app.web_thread.daemon = True

    #starts flask thread
    app.web_thread.start()

    #begins GUI event loop (keeps app running until user closes it)
    app.mainloop()