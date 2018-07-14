"""
This code was made by Ismael Filipe for python training propose. It's a 
a simple structured implementation of fork game.
"""

import random

WORDS_FILE = "words.dat"
USED_WORDS_FILE = "used_words_file.dat"
MAX_ATTEMPTS = 8
DEBUG = True

def main():
    header()
    gameLoop()

def header():
    print("###############################################################################")
    print("#                          Welcome to fork game!                              #")
    print("###############################################################################")

def congratulationsPrint():
    print("###############################################################################")
    print("#                     Congratulations you won the game!                       #")
    print("###############################################################################")

def gameoverPrint():
    print("###############################################################################")
    print("#                                Gaveover!                                    #")
    print("###############################################################################")

def gameLoop():    
    user_won = False
    used_letters = []    
    
    try:
        random_word = randomWord(loadWords(WORDS_FILE))
    except ValueError as error:
        print(error.args[0])
        return;

    guess_word = ["_" for letter in random_word]

    saveWordAtUsed(random_word)
    print(random_word)

    att = 1
    miss_att = 0

    printFork(att, guess_word, used_letters)
    
    while (miss_att < MAX_ATTEMPTS):
        guess_letter = requestUserLetter(used_letters)
        used_letters.append(guess_letter)

        if (matchLetterWithWord(guess_letter, random_word, guess_word)):
            print("Congratulations you got a letter!")
            printProgress(att, guess_word, used_letters)
        else:            
            print("\n\nYou missed the letter...")
            printFork(miss_att + 1, guess_word, used_letters)
            printProgress(att, guess_word, used_letters)
            miss_att += 1

        if (not ("_" in guess_word)):
            user_won = True
            break;

        att += 1

    if (user_won == True):
        congratulationsPrint()
    else:
        gameoverPrint()
      
def matchLetterWithWord(guess_letter, random_word, guess_word):
    letter_found = False

    for index, letter in enumerate(random_word):
        if (letter == guess_letter):            
            guess_word[index] = letter
            letter_found = True

    return letter_found

def printFork(attempt, guess_word, used_letters):
    print()
    if(attempt == 0):
        print("   _____    ")
        print("  |     |   ")
        print("  |         ")
        print("  |         ")
        print("  |         ")
        print("  |         ")
        print("__|_________")
        print(" |        | ")
    elif(attempt == 1):
        print("   _____    ")
        print("  |     |   ")
        print("  |     O   ")
        print("  |         ")
        print("  |         ")
        print("  |         ")
        print("__|_________")
        print(" |        | ")
    elif(attempt == 2):
        print("   _____    ")
        print("  |     |   ")
        print("  |     O   ")
        print("  |     |   ")
        print("  |         ")
        print("  |         ")
        print("__|_________")
        print(" |        | ")
    elif(attempt == 3):
        print("   _____    ")
        print("  |     |   ")
        print("  |     O   ")
        print("  |     |   ")
        print("  |    /    ")
        print("  |         ")
        print("__|_________")
        print(" |        | ")
    elif(attempt == 4):
        print("   _____    ")
        print("  |     |   ")
        print("  |     O   ")
        print("  |     |   ")
        print("  |    / \  ")
        print("  |         ")
        print("__|_________")
        print(" |        | ")
    elif(attempt == 5):
        print("   _____    ")
        print("  |     |   ")
        print("  |     O   ")
        print("  |     |\  ")
        print("  |    / \  ")
        print("  |         ")
        print("__|_________")
        print(" |        | ")
    elif(attempt == 7):
        print("   _____    ")
        print("  |     |   ")
        print("  |     O   ")
        print("  |    /|\  ")
        print("  |    / \  ")
        print("  |         ")
        print("__|_________")
        print(" |        | ")
    elif(attempt == 8):
        print("   _____    ")
        print("  |     |   ")
        print("  |     |   ")
        print("  |     O   ")
        print("  |    /|\  ")
        print("  |    / \  ")        
        print("__|_________")
        print(" |        | ")
    print()    

def printProgress(attempt, guess_word, used_letters):
    print("Attempts: {}".format(attempt))
    print("Guess word: {}".format("".join(guess_word)))
    print("Used letter(s): {}".format("".join(used_letters)))

def loadWords(words_file):
    words_list = []

    try:
        with open(words_file) as words_file:
            for line in words_file:
                words_list.append(line.strip().lower())
    except IOError as error:
        print("A error ocurred during the file reading. errno: ({}) error: ({})".format(error.errno, error.strerror))

    return words_list

def saveWordAtUsed(word):    
    try:
        with open(USED_WORDS_FILE, "a") as words_file:
            words_file.write(word + "\n")
    except IOError as error:
        print("A error ocurred during the file reading. errno: ({}) error: ({})".format(error.errno, error.strerror))

def randomWord(words_list):
    used_word_list = loadWords(USED_WORDS_FILE)

    words_diff_list = list(set(used_word_list).symmetric_difference(words_list))

    if (len(words_diff_list) == 0):
        raise ValueError("There is no words to play, please add more words or delete used words file.")

    return words_diff_list[random.randrange(0, len(words_diff_list))]

def requestUserLetter(used_letters):

    is_valid_letter = False

    while (not is_valid_letter):

        letter = input("\nInsert a precious letter: ").strip().lower()
    
        if (not len(letter)):
            print("You should type a letter!")
        elif (len(letter) > 1):
            print("You must type only one letter!") 
        elif (letter in used_letters):
            print("Already used letter, try another one!")
        else:
            is_valid_letter = True

    return letter

def debugPrint(msg):
    if (DEBUG):
        print(msg)

if (__name__ == "__main__"):
    main()