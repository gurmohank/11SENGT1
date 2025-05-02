import tkinter as tk
from tkinter import *
import customtkinter #needed for class definition
import customtkinter as ctk #needed for function calls
from PIL import Image, ImageTk
from flask import Flask, render_template #'render_template' refers to built in flask function which helps display HTML content
import threading
import webbrowser
import pyttsx3
import os
import subprocess
import platform
import json
import random



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

    def back_page(self):
        self.clear_page()
        if self.page_status == "home":
            self.show_home_page()
        elif self.page_status == "add":
            self.show_addition_page()
        elif self.page_status == "num":
            self.show_number_basics_page()
        elif self.page_status == "sub":
            self.show_subtraction_page()

    def cross_page(self):
        self.clear_page()
        if self.page_on == "home":
            self.show_home_page()
        elif self.page_on == "add":
            self.show_addition_page()
        elif self.page_on == "num":
            self.show_number_basics_page()
        elif self.page_on == "sub":
            self.show_subtraction_page()

    def show_home_page(self):
        self.page_on = "home"

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
        helpicon_label.bind("<Button-1>", lambda event: self.show_help_page())


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
                                    bg_color=widget_bg_col,
                                    command=self.show_number_basics_page)
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
                                        bg_color=widget_bg_col,
                                        command=self.show_subtraction_page)
        subtraction_mod.place(x=1165, y=530)

    def show_settings_page(self):
        self.clear_page()
        self.page_status = "home"

        backicon_label = ctk.CTkLabel(self, text="", image=backicon, bg_color=widget_bg_col)
        backicon_label.place(x=1340, y=-10)
        backicon_label.bind("<Button-1>", lambda event: self.back_page())




    def show_help_page(self):
        self.clear_page()
        self.page_status = "home"

        crossicon_label = ctk.CTkLabel(self, text="", image=crossicon, bg_color=widget_bg_col)
        crossicon_label.place(x=1340, y=-10)
        crossicon_label.bind("<Button-1>", lambda event: self.cross_page())

        info_label = ctk.CTkLabel(self, 
                                  text="Hi there! Welcome to the Math Magic Help section! " 
                                  "This is where you can learn\nhow to use the app and have the best time exploring math. "
                                  "Here's what you need to know",
                                  font=ctk.CTkFont(family="Nunito", size=23),
                                       text_color=opp_bg)
        info_label.place(x=250, y=100)

        home_info_label = ctk.CTkLabel(self, text="Home Page:\nStart here! It's like your magic map."
                                       "Click the buttons to go to different math adventures."
                                       "\nWant to learn about numbers, addition, or subtraction? Pick a module and jump right in!",
                                       font=ctk.CTkFont(family="Nunito", size=23),
                                       text_color=opp_bg,
                                       justify = "left")
        home_info_label.place(x=250, y=200)
                                      
        modules_info_label = ctk.CTkLabel(self, text="Modules:\n\n Each modules is packed with cool stuff:"
                                          "\n - Videos: Watch fun and exciting videos to learn new things."
                                          "\n - Activities: Play games and solve puzzles to level up your math skills!"
                                          "\n - Back Button: Oops, need to go back? No problem! "
                                          "The back button lets you return to the last page you were on.")
        modules_info_label.place(x=250, y=300)


        lets_go_label = ctk.CTkLabel(self, text= "Remember, if you ever need help, just come back to this page."
                                     "\nReady to become a Math Magic superstar? Let's go!")

        lets_go_label.place(x=800, y=00)
#\n\n- Modules:\n- Each module is packed with cool stuff:\n - Videos: 
# Watch fun and exciting videos to learn new things.\n - **Games and Challenges**: Play 
# games and solve puzzles to level up your math skills!\n - Choose your favorite activity and 
# have lots of fun learning.\n\nBack Button:\n - Oops, need to go back? No problem! The 
# back button lets you return to the last page you were on.\n - It’s super easy—click 
# it to go back to the home page or the module you were just in!\n\nThis app is all about 
# having fun while you learn. If you ever need help, just come back to this page.


    def show_number_basics_page(self):
        self.clear_page()

        self.page_on = "num"
        self.page_status = "home"

        backicon_label = ctk.CTkLabel(self, text="", image=backicon, bg_color=widget_bg_col)
        backicon_label.place(x=1250, y=-10)
        backicon_label.bind("<Button-1>", lambda event: self.back_page())


        helpicon_label = ctk.CTkLabel(self, text="", image=helpicon, bg_color=widget_bg_col)
        helpicon_label.place(x=1340, y=0)

        #placing guide character (home page)
        guidechar_label = ctk.CTkLabel(self, text="", image=guidechar, bg_color=widget_bg_col)
        guidechar_label.place(x=-20, y=530)

        number_video_a1 = ctk.CTkButton(self, text="Video: Numbers 1 to 30",
                                        font=ctk.CTkFont(family="Fredoka", size=24, weight="bold"), 
                                        width=180, height=180,
                                        corner_radius=45,
                                        fg_color=pastel_green,
                                        text_color=forest_green,
                                        border_width=8,
                                        border_color=forest_green,
                                        hover_color=light_butter,
                                        bg_color=widget_bg_col,
                                        command=self.show_number_video)
        number_video_a1.place(x=350, y=350)

        number_match_a2 = ctk.CTkButton(self, text="Match the Number!",
                                        font=ctk.CTkFont(family="Fredoka", size=24, weight="bold"), 
                                        width=180, height=180,
                                        corner_radius=45,
                                        fg_color=pastel_green,
                                        text_color=forest_green,
                                        border_width=8,
                                        border_color=forest_green,
                                        hover_color=light_butter,
                                        bg_color=widget_bg_col,
                                        command=self.show_number_match)
        number_match_a2.place(x=750, y=350)

    def show_number_video(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))  #identifies directory of the script
        video_path = os.path.join(current_dir, "mediaassets", "number_basics_video.mp4")  #establishes relative path
        # Check the operating system
        if platform.system() == "Windows":
            print(f"Video path being used: {video_path}")
            os.startfile(video_path)  #opens on default media player - windows
        elif platform.system() == "Darwin": 
            subprocess.call(["open", video_path])  #opens on default media player - macOS 
        elif platform.system() == "Linux":  
            subprocess.call(["xdg-open", video_path])  #opens on default media player - linux
        else:
            print("Unsupported OS. Cannot open the video file.")        
        

    def show_number_match(self):
        self.clear_page()

        backicon_label = ctk.CTkLabel(self, text="", image=backicon, bg_color=widget_bg_col)
        backicon_label.place(x=1340, y=-10)
        backicon_label.bind("<Button-1>", lambda event: self.back_page())

        self.number_match_quiz("mediaassets/content_library.json")


    def number_match_quiz(self, json_file):
        # Back icon setup
        backicon_label = ctk.CTkLabel(self, text="", image=backicon, bg_color=widget_bg_col)
        backicon_label.place(x=1340, y=-10)
        backicon_label.bind("<Button-1>", lambda event: self.back_page())

        # Load JSON data
        with open(json_file, "r") as file:
            content = json.load(file)

        # Select questions and affirmations
        selected_questions = random.sample(content["activity_1"][1:], 6)  # Skip the "a1_instructions" entry
        correct_affirmations = random.sample(content["on_point"], 6)
        incorrect_affirmations = random.sample(content["not_quite"], 6)

        score = 0
        question_index = 0
        all_options = []

        # Question label setup
        question_label = ctk.CTkLabel(self, text="", font=("Arial", 18), wraplength=600)
        question_label.pack(pady=20)

        # Radio buttons setup
        radio_var = tk.IntVar()
        radio_buttons = [
            ctk.CTkRadioButton(self, text="", variable=radio_var, value=i, font=("Arial", 14))
            for i in range(3)
        ]
        for rb in radio_buttons:
            rb.pack(anchor="w", padx=20)

        # Feedback label
        feedback_label = ctk.CTkLabel(self, text="", font=("Arial", 12), fg_color="blue")
        feedback_label.pack(pady=10)

        # Check and Next buttons
        check_button = ctk.CTkButton(self, text="Check", command=lambda: validate_answer())
        check_button.pack(pady=10)

        next_button = ctk.CTkButton(self, text="Next", state="disabled", command=lambda: next_question())
        next_button.pack(pady=10)

        def display_question():
            nonlocal question_index, all_options

            if question_index >= len(selected_questions):
                question_label.configure(text=f"Quiz Complete! Your score: {score}/{len(selected_questions)}")
                check_button.pack_forget()
                next_button.pack_forget()
                for rb in radio_buttons:
                    rb.pack_forget()
                return

            # Prepare current question
            question_data = selected_questions[question_index]
            question_label.configure(
                text=f"Match the number for: {question_data['word']}"
            )

            all_options = [question_data["number"]] + question_data["options"]
            random.shuffle(all_options)

            for i, option in enumerate(all_options):
                radio_buttons[i].configure(text=option, state="normal")

            radio_var.set(-1)
            feedback_label.configure(text="")
            check_button.configure(state="normal")
            next_button.configure(state="disabled")

        def validate_answer():
            nonlocal score, all_options

            selected_index = radio_var.get()

            if selected_index == -1:
                feedback_label.configure(text="Please select an option!", fg_color="red")
                return

            correct_option = selected_questions[question_index]["number"]

            if all_options[selected_index] == correct_option:
                score += 1
                affirmation = random.choice(correct_affirmations)
                feedback_label.configure(text=f"Correct! {affirmation}", fg_color="green")
            else:
                feedback = random.choice(incorrect_affirmations)
                feedback_label.configure(
                    text=f"Incorrect! {feedback} The correct answer was {correct_option}.",
                    fg_color="red",
                )

            check_button.configure(state="disabled")
            next_button.configure(state="normal")

        def next_question():
            nonlocal question_index
            question_index += 1
            display_question()

        display_question()

    def show_addition_page(self):
        self.clear_page()

        self.page_on = "add"
        self.page_status = "home"

        backicon_label = ctk.CTkLabel(self, text="", image=backicon, bg_color=widget_bg_col)
        backicon_label.place(x=1250, y=-10)
        backicon_label.bind("<Button-1>", lambda event: self.back_page())


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
        number_stacker_a1.place(x=600, y=350)

    def show_number_stacker_page(self):
        self.clear_page()
        self.page_status = "add"

        #main frame covering whole page
        main_frame = tk.Frame(self, bg=bg_colour)
        main_frame.pack(fill=tk.BOTH, expand=True)

        backicon_label = ctk.CTkLabel(main_frame, text="", image=backicon, bg_color=widget_bg_col)
        backicon_label.place(x=1340, y=-10)
        backicon_label.bind("<Button-1>", lambda event: self.back_page())

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
        ten_label.place(x=250, y=150)
        ten_label.bind("<Button-1>", drag_start)
        ten_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[ten_label] = (250, 150)  # add the label and its original position to dictionary


        nine_label = tk.Label(main_frame, text="", image=self.nine_tkv)
        nine_label.place(x=715, y=150)
        nine_label.bind("<Button-1>", drag_start)
        nine_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[nine_label] = (715, 150)  # add the label and its original position to dictionary

        
        eight_label = tk.Label(main_frame, text="", image=self.eight_tkv)
        eight_label.place(x=1180, y=150)
        eight_label.bind("<Button-1>", drag_start)
        eight_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[eight_label] = (1180, 150)  # add the label and its original position to dictionary

        
        seven_label = tk.Label(main_frame, text="", image=self.seven_tkv)
        seven_label.place(x=1645, y=150)
        seven_label.bind("<Button-1>", drag_start)
        seven_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[seven_label] = (1645, 150)  # add the label and its original position to dictionary

    
        six_label = tk.Label(main_frame, text="", image=self.six_tkv)
        six_label.place(x=2110, y=150)
        six_label.bind("<Button-1>", drag_start)
        six_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[six_label] = (2110, 150)  # add the label and its original position to dictionary


        five_label = tk.Label(main_frame, text="", image=self.five_tkv)
        five_label.place(x=2110, y=440)
        five_label.bind("<Button-1>", drag_start)
        five_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[five_label] = (2110, 440)  # add the label and its original position to dictionary


        four_label = tk.Label(main_frame, text="", image=self.four_tkv)
        four_label.place(x=1645, y=485)
        four_label.bind("<Button-1>", drag_start)
        four_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[four_label] = (1645, 485)  # add the label and its original position to dictionary


        three_label = tk.Label(main_frame, text="", image=self.three_tkv)
        three_label.place(x=1180, y=530)
        three_label.bind("<Button-1>", drag_start)
        three_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[three_label] = (1180, 530)  # add the label and its original position to dictionary


        two_label = tk.Label(main_frame, text="", image=self.two_tkv)
        two_label.place(x=715, y=575)
        two_label.bind("<Button-1>", drag_start)
        two_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[two_label] = (715, 575)  # add the label and its original position to dictionary


        one_label = tk.Label(main_frame, text="", image=self.one_tkv)
        one_label.place(x=250, y=620)
        one_label.bind("<Button-1>", drag_start)
        one_label.bind("<B1-Motion>", drag_motion)
        self.start_positions[one_label] = (250, 620)  # add the label and its original position to dictionary
        

        def reset_pos(start_positions):
            for label, (x, y) in start_positions.items():
                label.place(x=x, y=y)

        reset_pos_button = ctk.CTkButton(main_frame, text="Reset", 
                                         font=ctk.CTkFont(family="Fredoka", size=24, weight="bold"), 
                                        width=180, height=90,
                                        corner_radius=45,
                                        fg_color=pastel_green,
                                        text_color=forest_green,
                                        border_width=8,
                                        border_color=forest_green,
                                        hover_color=light_butter,
                                        bg_color=widget_bg_col,command=lambda: reset_pos(self.start_positions))        
        reset_pos_button.place(x=860, y=730)

        #canvas set up
        num_canvas = ctk.CTkCanvas(main_frame, width=905, height=455, bg=opp_bg)
        num_canvas.place(x=1450, y=930)
        
        def draw_vertical_line(event=None):
            canvas_width = num_canvas.winfo_width()
            canvas_height = num_canvas.winfo_height()
            middle_x = canvas_width // 2
            num_canvas.create_line(middle_x, 0, middle_x, canvas_height, fill="black", width=2)

        num_canvas.bind("<Configure>", draw_vertical_line)

    def show_subtraction_page(self):
        self.clear_page()

        self.page_status == "sub"
        self.page_status = "home"

        backicon_label = ctk.CTkLabel(self, text="", image=backicon, bg_color=widget_bg_col)
        backicon_label.place(x=1250, y=-10)
        backicon_label.bind("<Button-1>", lambda event: self.back_page())


        helpicon_label = ctk.CTkLabel(self, text="", image=helpicon, bg_color=widget_bg_col)
        helpicon_label.place(x=1340, y=0)

        #placing guide character (home page)
        guidechar_label = ctk.CTkLabel(self, text="", image=guidechar, bg_color=widget_bg_col)
        guidechar_label.place(x=-20, y=530)

        subtraction_video_a1 = ctk.CTkButton(self, text="Video: Subtraction with Dinosaurs",
                                        font=ctk.CTkFont(family="Fredoka", size=24, weight="bold"), 
                                        width=180, height=180,
                                        corner_radius=45,
                                        fg_color=pastel_green,
                                        text_color=forest_green,
                                        border_width=8,
                                        border_color=forest_green,
                                        hover_color=light_butter,
                                        bg_color=widget_bg_col,
                                        command=self.show_subtraction_video)
        subtraction_video_a1.place(x=300, y=350)

        take_away_a1 = ctk.CTkButton(self, text="Take some away!",
                                        font=ctk.CTkFont(family="Fredoka", size=24, weight="bold"), 
                                        width=180, height=180,
                                        corner_radius=45,
                                        fg_color=pastel_green,
                                        text_color=forest_green,
                                        border_width=8,
                                        border_color=forest_green,
                                        hover_color=light_butter,
                                        bg_color=widget_bg_col,
                                        command=self.show_take_away)
        take_away_a1.place(x=800, y=350)


    def show_subtraction_video(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))  #identifies directory of the script
        video_path = os.path.join(current_dir, "mediaassets", "subtraction_video.mp4")  #establishes relative path
        # Check the operating system
        if platform.system() == "Windows":
            print(f"Video path being used: {video_path}")
            os.startfile(video_path)  #opens on default media player - windows
        elif platform.system() == "Darwin": 
            subprocess.call(["open", video_path])  #opens on default media player - macOS 
        elif platform.system() == "Linux":  
            subprocess.call(["xdg-open", video_path])  #opens on default media player - linux
        else:
            print("Unsupported OS. Cannot open the video file.") 

    def show_take_away(self):
        self.clear_page()

        self.page_status = "sub"

        backicon_label = ctk.CTkLabel(self, text="", image=backicon, bg_color=widget_bg_col)
        backicon_label.place(x=1340, y=-10)
        backicon_label.bind("<Button-1>", lambda event: self.back_page())

        self.take_away_quiz("mediaassets/content_library.json")

    def take_away_quiz(self, json_file):
        with open(json_file, "r") as file:
            content = json.load(file)

        selected_questions = random.sample(content["activity_3"], 6)
        correct_affirmations = random.sample(content["on_point"], 6)
        incorrect_affirmations = random.sample(content["not_quite"], 6)

        score = 0
        question_index = 0

        # Declare all_options within the take_away_quiz scope
        all_options = []

        self.clear_page()

        question_label = ctk.CTkLabel(self, text="", font=("Arial", 18), wraplength=600)
        question_label.pack(pady=20)

        radio_var = tk.IntVar()
        radio_buttons = [
            ctk.CTkRadioButton(self, text="", variable=radio_var, value=i, font=("Arial", 14))
            for i in range(3)
        ]
        for rb in radio_buttons:
            rb.pack(anchor="w", padx=20)

        feedback_label = ctk.CTkLabel(self, text="", font=("Arial", 12), fg_color="blue")
        feedback_label.pack(pady=10)

        check_button = ctk.CTkButton(self, text="Check", command=lambda: validate_answer())
        check_button.pack(pady=10)

        next_button = ctk.CTkButton(self, text="Next", state="disabled", command=lambda: next_question())
        next_button.pack(pady=10)

        def display_question():
            nonlocal question_index, all_options

            backicon_label = ctk.CTkLabel(self, text="", image=backicon, bg_color=widget_bg_col)
            backicon_label.place(x=1340, y=-10)
            backicon_label.bind("<Button-1>", lambda event: self.back_page())

            if question_index >= len(selected_questions):
                feedback_label.configure(text="")
                question_label.configure(text=f"Quiz Complete! Your score: {score}/{len(selected_questions)}")
                check_button.pack_forget()
                next_button.pack_forget()
                for rb in radio_buttons:
                    rb.pack_forget()
                return

            question_data = selected_questions[question_index]
            question_label.configure(text=f"Q{question_index + 1}: {question_data['question']}")

            all_options = [question_data["answer"]] + question_data["options"]
            random.shuffle(all_options)

            for i, option in enumerate(all_options):
                radio_buttons[i].configure(text=option, state="normal")

            radio_var.set(-1)
            feedback_label.configure(text="")
            check_button.configure(state="normal")
            next_button.configure(state="disabled")

        def validate_answer():
            nonlocal score, all_options

            selected_index = radio_var.get()

            if selected_index == -1:
                feedback_label.configure(text="Please select an option!", fg_color="red")
                return

            correct_option = selected_questions[question_index]["answer"]

            if all_options[selected_index] == correct_option:
                score += 1
                affirmation = random.choice(correct_affirmations)
                feedback_label.configure(text=f"Correct! {affirmation}", fg_color="green")
            else:
                feedback = random.choice(incorrect_affirmations)
                feedback_label.configure(
                    text=f"Incorrect! {feedback} The correct answer was {correct_option}.",
                    fg_color="red",
                )

            check_button.configure(state="disabled")
            next_button.configure(state="normal")

        def next_question():
            nonlocal question_index
            question_index += 1
            display_question()

        display_question()


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


    