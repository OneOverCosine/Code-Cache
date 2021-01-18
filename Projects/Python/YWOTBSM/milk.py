# This file is for project LAMBENT or 'the milk game'
# It's a small text based thing that I hope will help my
# learning process
# https://www.tumblr.com/blog/magwnrpk 

import re

class Scene():
    
    def __init__(self, index, text, leftChild, rightChild):
        self.index = index
        self.text = text # this scenes's text, including the choices - will need further formatting to display
        self.leftChild = leftChild # the index of the left child
        self.rightChild = rightChild # the index of the right child

    def formatText(self):
        # This formats the text so that the scene is set
        # then the player choices are displayed next
        # still need to get the lines to display as I want them to

        temp = self.text.split(" + ")

        newText = "\n"

        for i in range(len(temp)):
            newText = newText + temp[i] + "\n"

        #print("This is the new text: " + newText)

        self.text = newText

def loadDialogue(filepath):
    # reads dialogue from a text file and creates a Scene object for each one
    # these Scenes are stored in an array to be accessed later

    dialogueDump = []
    dialoguesTemp = []

    textDump = open(filepath, "r")# 'r' means read

    # now split at each \n to create an array of 'dialogues'

    # read through each line of the file

    for line in textDump:

        dialogueDump.append(line)


    for dialogue in dialogueDump:
        dialoguesTemp.append(dialogue.split(" | "))
    # this all works... now to get the dialogues into 'scenes'

    # go through the temp dialogues array and create a list of Scene objects
    scenes = []

    for i in range(len(dialoguesTemp)):
        # 0 = id, 1 = text, 2 = left child id, 3 = right child id
        idIndex = int(dialoguesTemp[i][0])
        leftIndex = int(dialoguesTemp[i][2])
        rightIndex = int(dialoguesTemp[i][3])

        tempScene = Scene(idIndex, dialoguesTemp[i][1], leftIndex, rightIndex)
        scenes.append(tempScene)
    
    # for debugging
    # print("There are currently " + str(len(scenes)) + " scenes")
    #print(scenes[2].displayText()) #for testing

    return scenes

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

def playGame():
    # this is where the main gameplay loop will run
    # print("This is the main game loop!")

    # first load the dialogue
    # and make an array of the scenes
    filepath = "./resources/dialogue.txt"
    #filepath = "./resources/testDialogue.txt" # for testing
    allScenes = loadDialogue(filepath) # this array holds Scene objects

    # Initialise the two types of input I'll be taking
    intPlayerInput = -1
    #strPlayerInput = ""

    # PROBABLY JUST TESTING - changes are likely
    message = ""
    currentScene = allScenes[0]# get and display the first scene
    currentSceneIndex = 0

    while(currentSceneIndex != -1): # doesn't trigger a break
        # keep on loading and displaying scenes until an ending is reached
    
        currentScene.formatText()
        message = currentScene.text + "\n"
        rawPlayerInput = input(message)

        # INPUT TESTING AREA - to work on the help() and exit commands
        # These checks happen first since the input for the game are ints
        if(rawPlayerInput == "exit" or rawPlayerInput == "quit"):
            # the player wants to exit the game, so breaking out of the while will take them
            # back to the main menu
            break
        elif(rawPlayerInput == "help"):
            help() # run the help function, then continue this one

        intPlayerInput = getInput(rawPlayerInput, False, message)

        while(intPlayerInput > 2 or intPlayerInput < 1):
            rawPlayerInput = input(message)

            intPlayerInput = getInput(rawPlayerInput, False, message)

        # if the choice was 1 go for the left child, else go for right child
        if(intPlayerInput == 1):
            currentSceneIndex = currentScene.leftChild
        else:
            currentSceneIndex = currentScene.rightChild

        if(currentSceneIndex == -1):
            # apparently while loops won't break halfway if the checked condition changes
            # i need to remember that the check only happens at the start...
            break # outer while didn't break loop so this is needed (for now)

        # now for the costly / dangerous part
        i = 0 # this is the index that is used in the *list*
        # currentSceneIndex if used for the search
        while(True):
            if(allScenes[i].index == currentSceneIndex):
                currentScene = allScenes[i]
                break
            i = i + 1

    #print(currentScene.text) #end of first test

def help():
    # this is where general help is displayed
    print("""           === Help ===
    
    This is a text base game that requires the keyboard for interactions.
    Most prompts will ask for you to enter the number that corresponds
    to the option you want to select. In most cases, this will be either
    1 or 2.

    If you want to exit the game, enter 'exit' or 'quit'. This will take
    you back to the main menu.

    Entering 'help' while playing the game will bring you here.
    
    --------""")

def credits():
    # just print the credits
    # this doesn't even need to be a function, but I love doing this
    print("\n*Programming and story by [whatever my name is on this site]*\n")

def main():

    # filepath = "./resources/dialogue.txt"
    
    # the main menu
    message = """== You Went Out To Buy Some Milk ==\n
    1. Start game
    2. Help
    3. Credits
    4. Exit\n"""

    # get the initial input then check it
    menu = input(message)
    choice = getInput(menu, False, message)
   
    while(choice != 4):

        while(choice > 4 or choice < 1):

            choice = getInput(menu, False, message)

        if(choice == 1):
            choice = -1 # reset the value so we go back to the menu
            playGame()
        elif(choice == 2):
            choice = -1 
            help()
        elif(choice == 3):
            choice = -1 
            credits()
        else:
            print("Goodbye!")
            break
        
        menu = "" # also reset this as it determines the value for choice 

main()