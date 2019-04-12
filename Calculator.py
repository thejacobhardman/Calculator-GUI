# Jacob Hardman
# Intro To Programming
# Professor Marcus Longwell
# 4/10/19
# Python Version 3.7.3

# Importing pkgs
import tkinter as tk
import tkinter.font as tkFont
import ctypes
import os
import sys

# Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

########################################################## GLOBAL VARIABLES ##############################################################

# Tracks if the program is still running
Is_Running = True

# Stores the User's input
User_Input = ""

# Tracks if the User has made a decision
User_Confirm = False

# Initializing the main window
Window = tk.Tk()
Window.title("Calculator")

# I wanted the buttons on the keypad to change color when you mouse over them so I found this code on Stack Overflow:
# https://stackoverflow.com/questions/49888623/tkinter-hovering-over-button-color-change
class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

# Creating a custom font for the program to use
Text_Font = tkFont.Font(family='Helvetica', size=12, weight='bold')

# Strings that store what is being displayed on the two labels
Display_String = "0"
History_String = "There's no history yet."

########################################################### PROGRAM LOGIC ###############################################################

### Messing around with the functions of tkinter
def Application_Loop():

    # This code fixes the blurry text that tkinter has when being used on Windows. I got this solution from Stack Overflow:
    # https://stackoverflow.com/questions/36514158/tkinter-output-blurry-for-icon-and-text-python-2-7/43033405
    if __name__ == "__main__":   
        if 'win' in sys.platform:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)

    # Creating the GUI
    Init_GUI()

    # Looping in the main window to accept User input
    Window.mainloop()

### Setting up the GUI's layout (I reccomend minimizing this when not examining it)
def Init_GUI():
    # Importing Global Variables
    global Window

    # Content Frame that holds all of the sub widgets
    Content = tk.Frame(Window, height="600", width="800")
    Content.pack(expand="true", fill="both")

    # Frame widget that displays what data the user is entering
    Display = tk.Frame(Content)
    Display.place(relwidth="0.7", relheight="0.1")

    Display_Text = tk.Label(Display, anchor="e", padx="5", font=Text_Font, text=Display_String, fg="white", bg="#3f4349")
    Display_Text.place(relwidth="1", relheight="1")

    # Frame widget that shows the history of what calculations the user has performed
    History = tk.Frame(Content)
    History.place(anchor="ne", relx="1", relwidth="0.3", relheight="1")

    History_Text = tk.Label(History, anchor="nw", padx="10", pady="10", font=Text_Font, text=History_String, 
    fg="white", bg="#33353a")
    History_Text.place(relwidth="1", relheight="1")

    # Frame widget that contains the keypad
    Keypad = tk.Frame(Content)
    Keypad.place(anchor="sw", rely="1", relwidth="0.7", relheight="0.9")

    ### KEYPAD BUTTONS
    Clear_All = HoverButton(Keypad, text="CE", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Clear_All.place(relwidth="0.25", relheight="0.2")

    Clear = HoverButton(Keypad, text="C", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Clear.place(relx="0.25", relwidth="0.25", relheight="0.2")

    Delete = HoverButton(Keypad, text="Del", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Delete.place(relx="0.5", relwidth="0.25", relheight="0.2")

    Divide = HoverButton(Keypad, text=chr(247), font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Divide.place(relx="0.75", relwidth="0.25", relheight="0.2")

    Seven = HoverButton(Keypad, text="7", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Seven.place(rely="0.2", relwidth="0.25", relheight="0.2")

    Eight = HoverButton(Keypad, text="8", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Eight.place(rely="0.2", relx="0.25", relwidth="0.25", relheight="0.2")

    Nine = HoverButton(Keypad, text="9", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Nine.place(rely="0.2", relx="0.5", relwidth="0.25", relheight="0.2")

    Multiply = HoverButton(Keypad, text="X", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Multiply.place(rely="0.2", relx="0.75", relwidth="0.25", relheight="0.2")

    Four = HoverButton(Keypad, text="4", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Four.place(rely="0.4", relwidth="0.25", relheight="0.2")

    Five = HoverButton(Keypad, text="5", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Five.place(rely="0.4", relx="0.25", relwidth="0.25", relheight="0.2")

    Six = HoverButton(Keypad, text="6", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Six.place(rely="0.4", relx="0.5", relwidth="0.25", relheight="0.2")

    Subtract = HoverButton(Keypad, text="-", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Subtract.place(rely="0.4", relx="0.75", relwidth="0.25", relheight="0.2")

    One = HoverButton(Keypad, text="1", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    One.place(rely="0.6", relwidth="0.25", relheight="0.2")

    Two = HoverButton(Keypad, text="2", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Two.place(rely="0.6", relx="0.25", relwidth="0.25", relheight="0.2")

    Three = HoverButton(Keypad, text="3", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Three.place(rely="0.6", relx="0.5", relwidth="0.25", relheight="0.2")

    Add = HoverButton(Keypad, text="+", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Add.place(rely="0.6", relx="0.75", relwidth="0.25", relheight="0.2")

    Invert_Sign = HoverButton(Keypad, text=chr(177), font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Invert_Sign.place(rely="0.8", relwidth="0.25", relheight="0.2")

    Zero = HoverButton(Keypad, text="0", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Zero.place(rely="0.8", relx="0.25", relwidth="0.25", relheight="0.2")

    Decimal = HoverButton(Keypad, text=".", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Decimal.place(rely="0.8", relx="0.5", relwidth="0.25", relheight="0.2")

    Equals = HoverButton(Keypad, text="=", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Equals.place(rely="0.8", relx="0.75", relwidth="0.25", relheight="0.2")

########################################################### PROGRAM FLOW ################################################################

Application_Loop()