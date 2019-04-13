# Jacob Hardman
# Intro To Programming
# Professor Marcus Longwell
# 4/10/19
# Python Version 3.7.3

# Credit for sound effects to Marianne Gagnon
# http://soundbible.com/1682-Robot-Blip.html
# http://soundbible.com/1669-Robot-Blip-2.html

# Importing pkgs
import tkinter as tk
import tkinter.font as tkFont
import ctypes
import sys
import winsound as sound

########################################################## GLOBAL VARIABLES ##############################################################

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
Display_String = tk.StringVar()
Display_String.set("")
History_String = tk.StringVar()
History_String.set("")

########################################################### PROGRAM LOGIC ###############################################################

### Setting up the GUI's layout (I reccomend minimizing this when not examining it)
def Init_GUI():
    # Importing Global Variables
    global Window
    global Keypad
    global Display_Text

    # Content Frame that holds all of the sub widgets
    Content = tk.Frame(Window, height="600", width="800")
    Content.pack(expand="true", fill="both")

    # Frame widget that displays what data the user is entering
    Display = tk.Frame(Content)
    Display.place(relwidth="0.7", relheight="0.1")

    Display_Text = tk.Label(Display, anchor="e", padx="5", font=Text_Font, textvariable=Display_String, fg="white", bg="#3f4349")
    Display_Text.place(relwidth="1", relheight="1")

    # Frame widget that shows the history of what calculations the user has performed
    History = tk.Frame(Content)
    History.place(anchor="ne", relx="1", relwidth="0.3", relheight="1")

    History_Text = tk.Label(History, anchor="nw", padx="10", pady="10", font=Text_Font, textvariable=History_String, 
    fg="white", bg="#33353a")
    History_Text.place(relwidth="1", relheight="1")

    # Frame widget that contains the keypad
    Keypad = tk.Frame(Content)
    Keypad.place(anchor="sw", rely="1", relwidth="0.7", relheight="0.9")

def Track_Keypad():
    # Importing Global Variables
    global Keypad

    ### KEYPAD BUTTONS
    Clear_All = HoverButton(Keypad, command=lambda: [Key_Pressed(10), Play_Sound(2)],
     text="CE", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Clear_All.place(relwidth="0.25", relheight="0.2")

    Clear = HoverButton(Keypad, command=lambda: [Key_Pressed(11), Play_Sound(2)],
    text="C", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Clear.place(relx="0.25", relwidth="0.25", relheight="0.2")

    Delete = HoverButton(Keypad, command=lambda: [Key_Pressed(12), Play_Sound(2)],
     text="Del", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Delete.place(relx="0.5", relwidth="0.25", relheight="0.2")

    Divide = HoverButton(Keypad, command=lambda: [Key_Pressed(13), Play_Sound(1)],
    text="/", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Divide.place(relx="0.75", relwidth="0.25", relheight="0.2")

    Seven = HoverButton(Keypad, command=lambda: [Key_Pressed(7), Play_Sound(1)],
    text="7", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Seven.place(rely="0.2", relwidth="0.25", relheight="0.2")

    Eight = HoverButton(Keypad, command=lambda: [Key_Pressed(8), Play_Sound(1)],
     text="8", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Eight.place(rely="0.2", relx="0.25", relwidth="0.25", relheight="0.2")

    Nine = HoverButton(Keypad, command=lambda: [Key_Pressed(9), Play_Sound(1)],
     text="9", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Nine.place(rely="0.2", relx="0.5", relwidth="0.25", relheight="0.2")

    Multiply = HoverButton(Keypad, command=lambda: [Key_Pressed(14), Play_Sound(1)],
     text="*", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Multiply.place(rely="0.2", relx="0.75", relwidth="0.25", relheight="0.2")

    Four = HoverButton(Keypad, command=lambda: [Key_Pressed(4), Play_Sound(1)],
     text="4", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Four.place(rely="0.4", relwidth="0.25", relheight="0.2")

    Five = HoverButton(Keypad, command=lambda: [Key_Pressed(5), Play_Sound(1)],
     text="5", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Five.place(rely="0.4", relx="0.25", relwidth="0.25", relheight="0.2")

    Six = HoverButton(Keypad, command=lambda: [Key_Pressed(6), Play_Sound(1)],
     text="6", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Six.place(rely="0.4", relx="0.5", relwidth="0.25", relheight="0.2")

    Subtract = HoverButton(Keypad, command=lambda: [Key_Pressed(15), Play_Sound(1)],
     text="-", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Subtract.place(rely="0.4", relx="0.75", relwidth="0.25", relheight="0.2")

    One = HoverButton(Keypad, command=lambda: [Key_Pressed(1), Play_Sound(1)],
    text="1", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    One.place(rely="0.6", relwidth="0.25", relheight="0.2")

    Two = HoverButton(Keypad, text="2", command=lambda: [Key_Pressed(2), Play_Sound(1)],
    font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Two.place(rely="0.6", relx="0.25", relwidth="0.25", relheight="0.2")

    Three = HoverButton(Keypad, command=lambda: [Key_Pressed(3), Play_Sound(1)],
    text="3", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Three.place(rely="0.6", relx="0.5", relwidth="0.25", relheight="0.2")

    Add = HoverButton(Keypad, command=lambda: [Key_Pressed(16), Play_Sound(1)],
     text="+", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Add.place(rely="0.6", relx="0.75", relwidth="0.25", relheight="0.2")

    Invert_Sign = HoverButton(Keypad, command=lambda: [Key_Pressed(19), Play_Sound(1)],
     text=chr(177), font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Invert_Sign.place(rely="0.8", relwidth="0.25", relheight="0.2")

    Zero = HoverButton(Keypad, command=lambda: [Key_Pressed(0), Play_Sound(1)],
    text="0", font=Text_Font, fg="white", activeforeground="white", bg="black", activebackground="#303338")
    Zero.place(rely="0.8", relx="0.25", relwidth="0.25", relheight="0.2")

    Decimal = HoverButton(Keypad, command=lambda: [Key_Pressed(18), Play_Sound(1)],
     text=".", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Decimal.place(rely="0.8", relx="0.5", relwidth="0.25", relheight="0.2")

    Equals = HoverButton(Keypad, command=lambda: [Key_Pressed(17), Play_Sound(2)],
     text="=", font=Text_Font, fg="white", activeforeground="white", bg="#191a1c", activebackground="#303338")
    Equals.place(rely="0.8", relx="0.75", relwidth="0.25", relheight="0.2")

### Updates the Display area with the numbers that the User enters based on input from Key_Track
def Key_Pressed(arg):
    # Importing global variables
    global Display_String
    global History_String

    if arg == 0:
        Display_String.set(Display_String.get() + "0")
    elif arg == 1:
        Display_String.set(Display_String.get() + "1")
    elif arg == 2:
        Display_String.set(Display_String.get() + "2")
    elif arg == 3:
        Display_String.set(Display_String.get() + "3")
    elif arg == 4:
        Display_String.set(Display_String.get() + "4")
    elif arg == 5:
        Display_String.set(Display_String.get() + "5")
    elif arg == 6:
        Display_String.set(Display_String.get() + "6")
    elif arg == 7:
        Display_String.set(Display_String.get() + "7")
    elif arg == 8:
        Display_String.set(Display_String.get() + "8")
    elif arg == 9:
        Display_String.set(Display_String.get() + "9")
    elif arg == 10:
        Display_String.set("")
        History_String.set("")
    elif arg == 11:
        Display_String.set("")
    elif arg == 12:
        Display_String.set(Display_String.get()[0:-1])
    elif arg == 13:
        Display_String.set(Display_String.get() + "/")
    elif arg == 14:
        Display_String.set(Display_String.get() + "*")
    elif arg == 15:
        Display_String.set(Display_String.get() + "-")
    elif arg == 16:
        Display_String.set(Display_String.get() + "+")
    elif arg == 17:
        result = eval(Display_String.get())
        History_String.set(History_String.get() + Display_String.get() + " = " + str(result) + "\n")
        Display_String.set(result)
    elif arg == 18:
        Display_String.set(Display_String.get() + ".")
    elif arg == 19:
        result = eval(Display_String.get()) * -1
        Display_String.set(result)

### Plays a sound when a button is pushed
def Play_Sound(arg):
    if arg == 1:
        sound.PlaySound("Robot_blip-Marianne_Gagnon.wav", 1)
    elif arg == 2:
        sound.PlaySound("Robot_blip_2-Marianne_Gagnon.wav", 1)

########################################################### PROGRAM FLOW ################################################################

# This code fixes the blurry text that tkinter has when being used on Windows. I got this solution from Stack Overflow:
# https://stackoverflow.com/questions/36514158/tkinter-output-blurry-for-icon-and-text-python-2-7/43033405
if __name__ == "__main__":   
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

Init_GUI() # Creating the GUI
Track_Keypad() # Creates and places the Keypad buttons while also tracking which button is pressed

# Looping in the main window to accept User input
Window.mainloop()