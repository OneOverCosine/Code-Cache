# Hangman project
# select a word from a premade list and display n dashes where n is the length of the word
# let the player guess a letter
# if it's not been guessed yet and is in the word:
# display it in the correct position and add it to the 'guessed' list
# if it's not correct, remove 1 from guesses left and add letter to 'guessed' list
#-----------------------------------------------------------------------------------------

import re
import random

#----------------------------------------------------------------------------------------
    
def checkInput(text):
    # checks if the input is a single character in the english alphabet
    if(len(text) == 1 and re.search('[a-zA-Z]', text)):
        return 1 # valid input!
    else:
        return 0 # this means the input was invalid

def checkPlayerGuess(word, playerInput, displayWord, numGuesses):
    # returns two values - displayWord and numGuesses

    print("")
    # check to see if guessed letter is in word
    if(re.search(playerInput, word)):
        # letter is in the word

        wordToDisplay = "" # for testing, for now
        for i in range(len(word)):
            # Go through each letter in the word...
            if(word[i] == playerInput):
                # if the letter guessed is in this place, add the new letter to display
                wordToDisplay = wordToDisplay + playerInput + " "
                
            elif(word[i] == displayWord[2 * i]):
                # if this place already contains a visible letter, keep it visible
                wordToDisplay = wordToDisplay + word[i] + " "
                
            else:
                # otherwise, keep it blank
                wordToDisplay = wordToDisplay + "_ "

        # leave numGuesses unchanged, as the guess was correct

        print("The letter " + playerInput + " was correct!")
        return(wordToDisplay, numGuesses)
        
    else:
        # remove a guess and let the player know it was incorrect
        print("The letter " + playerInput + " was incorrect...")
        return(displayWord, numGuesses - 1)

def printHangman(numGuesses, playerGuesses):

    print("Letters guessed: " + playerGuesses)

    if(numGuesses == 7):
        print("""
|
|
|
|
|___""")
        
    elif(numGuesses == 6):
        
        print("""____
|  
|
|
|
|___""")
        
    elif(numGuesses == 5):
        print("""____
|  |
|
|
|
|___""")

    elif(numGuesses == 4):
        print("""____
|  |
|  o
|
|
|___""")
        
    elif(numGuesses == 3):
        print("""____
|  |
|  o
|  |
|
|___""")

    elif(numGuesses == 2):
        print("""____
|  |
|  o
| /|\\
|
|___""")

    elif(numGuesses == 1):
        print("""____
|  |
|  o
| /|\\
| / 
|___""")

        
    else:
        print("""____
|  |
|  o
| /|\\
| / \\
|___""")
        print("You've run out of guesses!")

def playLoop(hardMode):

    if(hardMode == False):

        words = ["fun", "strength", "fact", "necessary", "computer",
                "never", "crow", "mouse", "microphone", "desk",
                "game", "twelve", "comb", "internet", "street", "anger", "bandwagon"]
    else:
        words = ["unknown", "queue", "vortex", "zephyr",
                "gnarly", "nowadays", "oxygen"]

    word = words[random.randint(0, len(words) - 1)] # select a random word from the list to use

    #print(word)

    # the word to display
    displayWord = "" + ("_ " * len(word))

    #print(displayWord)

    # setup for the main game loop
    playerGuesses = ""
    numGuesses = 7
    guessed = False

    while(numGuesses > 0 and guessed == False):

        # first get the player input
        print(displayWord)
        playerInput = input("Enter your guess (a-z) \n")
    
        inputCheck = checkInput(playerInput)

        while(inputCheck != 1):

            print(" \n\nYour guess needs to be a single character")
            playerInput = input("Enter your guess (a-z) \n")

            inputCheck = checkInput(playerInput)

        # now see if the guess has already been made
        if(re.search(playerInput, playerGuesses)):
            # if the letter has already been guessed...
            print("You have already guessed the letter " + playerInput + "!")
            numGuesses = numGuesses - 1 #remove a guess and continue
        else:
            # if the letter hasn't been guessed... 
            playerGuesses = playerGuesses + playerInput
        
            # we'll check to see what to do
            result = checkPlayerGuess(word, playerInput, displayWord, numGuesses)
            displayWord = result[0]
            numGuesses = result[1]

            # check if player has guessed whole word
            answerCheck = ""
            for n in range(len(word)):
                answerCheck = answerCheck + displayWord[2 * n]

            if(answerCheck == word):
                guessed = True
                
        print("Before the hangman is printed, this is how many guesses there are left " + str(numGuesses) + "\n")
        printHangman(numGuesses, playerGuesses)


    if(numGuesses == 0):
        print("The word was " + word)

    else:
        print("You correctly guessed " + answerCheck + "!")

    print("")
    print("-------- THE GAME HAS ENDED --------")# for testing
    
        

def main():
    # for the menu and the like
    
    menuChoice = input("""=== HANGMAN ===
    
    1. Normal mode
    2. Hard mode
    3. Exit
    """)

    while(menuChoice != "3"):

        if(menuChoice == "1"):
            # play game (normal mode)
            playLoop(False)
            menuChoice = 3 # end the game once it's done
        
        elif(menuChoice == "2"):
            # play game (hard mode)
            playLoop(True)
            menuChoice = 3 # end the game once it's done

        else:
            # invalid input...
            print("Invalid input")
    
    #playLoop()

main()
