# This file is for coding projects and personal challenges - feel free to delete anything that's not in use

import re
from tkinter import *

#class TextInputWindow():


# This is the setup for the main window
# I need these to be global so they can be accessed from anywhere

ui = Tk()

ui.title("You Went Out To Buy Some Milk")
ui.geometry("745x700")
ui.resizable(width=TRUE, height=TRUE)

# create and place chat window

# create and place the input window that has a placeholder

# maybe add a scrollbar for the sake of looks


def deamer():
    dream = input("WHAT WOULD YOU LIKE TO DREAM TONIGHT?\n")

    print("\nI HAVE LISTENED AND WILL GLADLY PROVIDE YOU WITH YOUR REQUEST\n")
    print("TONIGHT YOU WILL DREAM ABOUT " + dream.upper())

def getInput(text, isString, message):
    # will make sure the player's input is valid
    # text is the raw input, isString is a boolean, and message is a string

    if(isString == True):
        return text


    # if the input is supposed to be a number, make sure the string length is 1
    match = re.search("[0-9]", text)    
    while(match == None or len(text) != 1):
        # keep making this check while either of these conditions hold
        # checking against None as this object doesn't return True or False
        #print("This value for match failed: " + str(match))
        text = input(message)

        match = re.search("[0-9]", text)


    #print("The value for match was " + str(match))
    return int(text)

def windowInput(event):
    # this handles the first part of getting the input
    # takes the user input and returns it as a string
    print("This will return whatever string the user entered")


def displayText(message):
    # this will add whatever is in the variable message to the 
    # display window
    # message must be a string!

    message = "\n" + message



def main():

    # this is the place where the main stuff is called

    # setup and display the window
    print("This is the main function")
    


    # now acutally start the window
    ui.mainloop()

    # some more stuff about how it works
    # https://www.geeksforgeeks.org/python-tkinter-entry-widget/
    # https://www.geeksforgeeks.org/tkinter-adding-style-to-the-input-text-using-ttk-entry-widget/?ref=rp
    # https://stackoverflow.com/questions/27820178/how-to-add-placeholder-to-an-entry-in-tkinter

main()