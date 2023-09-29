
# the list of the hangman graphic in a list
HANGMANPICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# list of imports
import sys
import random
import time
import os
import re


global lives
lives = 0

# word bank of animals
global words
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra mix temporary north enlarge permissible receive chemical gruesome '
         'imagine crime milk learned various split ring stitch output complex religion butter crown '
         'thin opposite synonymous expensive tender gaping pour rest display thumb stick hair happen '
         'incredible car important mean conscious cart choose spy sign finish hurt damaging '
         'inflect exuberant ocean encircle telling hiss cruel look '
         'flag dirt frogs war tub oven chess glass channel badge slope fang').split()

global insults
insults = ('stupid retard dumbass fatass cunt idiot wankstain faggot jackass jerk asshole cow dipshit twat wanker ').split()



def instructions():
  os.system('cls')
  instr = '''\n
  The objective of the game is for a human/bot to
  guess or select a word and the player has to guess it.

  The game ends when the hangman is fully drawn out.

  You will have 6 chances to guess the word.

  A word will be picked at random or by a human.
  You must guess it yourself.

  However if the user guesses the word before the hangman
  is complete, then they wxin!

  (Press enter when you finish reading.)'''

   # For every character in the instruction string,
  for char in instr:
    # Write out each character
    sys.stdout.write(char)
    # Print out any buffered text (in this case the .write() function)
    sys.stdout.flush()
    # Give it a time delay so that it gives off a cool animation of printing text
    time.sleep(0.005)

  noneInput = input("")
  os.system('cls')

def gameHuman():
  os.system('cls')
  # Uses word given by human
  hiddenWord = input("Enter your hidden word: ")
  # For every character in hiddenWord, replace it with an underscore
  guessedWord = ['_' for _ in hiddenWord]  # Initialize with underscores
  # Put all the guessed letters in a set to track what letters have already been guessed
  guessedLetters = set()


  while True:
    global lives
    os.system('cls')
    # Prints the hangman based on whatever life
    print(HANGMANPICS[lives])

    # Prints a space between each underscore to allow for easier readability of length of word
    displayWord = ' '.join(guessedWord)
    print(displayWord)

    # Input for the player to guess a letter
    guessRandom = input("Guess a letter: ").casefold()

    if guessRandom == hiddenWord:
        os.system('cls')
        print(f"You Win! The word was: {hiddenWord}")
        time.sleep(2)
        break

    # If the letter guessed is not a single letter then it tells the player to enter only one letter
    if len(guessRandom) != 1 or not guessRandom.isalpha():
      print("\nEnter only ONE letter.\n"), time.sleep(0.8)
      continue

    # If the player guesses a correct letter it replaces the underscores with the letters guessed
    if guessRandom in hiddenWord:
        for letter in range(len(hiddenWord)):
            # For every letter in the word, it uses the len() function to check what letters match within the range of
            # the word
            if hiddenWord[letter] == guessRandom:
                # If the hidden word has a mathcing letter to the one guessed,
                guessedWord[letter] = guessRandom
                # It assigns each correct letter to the right positions and overwrites the underscores

    else:
        # Increment lives if the guessed letter is incorrect
        lives += 1

    if ''.join(guessedWord) == hiddenWord:
        os.system('cls')
        print(f"You Win! The word was: {hiddenWord}")
        time.sleep(2)
        lives = 0
        break

    if lives >= 6:
        os.system('cls')
        print(f"{HANGMANPICS[6]}\nYou lost the game. The word was: {hiddenWord}")
        time.sleep(2)
        lives = 0
        break

def gameBot():
  # Randomises the word in the given list of words
  hiddenWord = random.choice(words)
  # For every character in hiddenWord, replace it with an underscore
  guessedWord = ['_' for _ in hiddenWord]  # Initialize with underscores
  # Put all the guessed letters in a set to track what letters have already been guessed
  guessedLetters = set()


  while True:
    global lives
    os.system('cls')
    # Prints the hangman based on whatever life
    print(HANGMANPICS[lives])

    # Prints a space between each underscore to allow for easier readability of length of word
    displayWord = ' '.join(guessedWord)
    print(displayWord)

    # Input for the player to guess a letter
    guessRandom = input("Guess a letter: ").casefold()

    if guessRandom == hiddenWord:
        os.system('cls')
        print(f"You Win! The word was: {hiddenWord}")
        time.sleep(2)
        break

    # If the letter guessed is not a single letter then it tells the player to enter only one letter
    if len(guessRandom) != 1 or not guessRandom.isalpha():
      print("\nEnter only ONE letter.\n"), time.sleep(0.8)
      continue

    # If the player guesses a correct letter it replaces the underscores with the letters guessed
    if guessRandom in hiddenWord:
        for letter in range(len(hiddenWord)):
            # For every letter in the word, it uses the len() function to check what letters match within the range of
            # the word
            if hiddenWord[letter] == guessRandom:
                # If the hidden word has a mathcing letter to the one guessed,
                guessedWord[letter] = guessRandom
                # It assigns each correct letter to the right positions and overwrites the underscores

    else:
        # Increment lives if the guessed letter is incorrect
        lives += 1

    if ''.join(guessedWord) == hiddenWord:
        os.system('cls')
        print(f"You Win! The word was: {hiddenWord}")
        time.sleep(2)
        lives = 0
        break

    if lives >= 6:
        os.system('cls')
        print(f"{HANGMANPICS[6]}\nYou lost the game. The word was: {hiddenWord}")
        time.sleep(2)
        lives = 0
        break


# Main menu function that displays the main menu
def mainMenu():
  while True:
    try:
      mainMenuSelection = int(input(

      '''
      ┬ ┬┌─┐┌┐┌┌─┐
      ├─┤├─┤││││ ┬
      ┴ ┴┴ ┴┘└┘└─┘
      ____________
     |            |
     |            |
     |    +---+   |
     |    |   |   |
     |    •   |   |
     |   /|\  |   |
     |   / \  |   |
     |   ======   |
     |            |
     |____________|

      ┌┬┐┌─┐┌┐┌
      │││├─┤│││
      ┴ ┴┴ ┴┘└┘

      1. Instructions
      2. Play w/ a bot
      3. Play w/ a human
      4. Quit

      '''
      "Enter your option here: "))

      if mainMenuSelection == 1:
        instructions()

      elif mainMenuSelection == 2:
        gameBot()

      #elif mainMenuSelection == 3:
        gameHuman()

      elif mainMenuSelection == 4:
        quit()

      # Insults you personally if you incorrectly pick an option
      else:
        os.system('cls')
        print(f"\n Pick a given option, {random.choice(insults)}."), os.system('cls')
    # Insults you personally if you don't even pick a number
    except ValueError:
      os.system('cls')
      print(f"Enter a number within the given options, {random.choice(insults)}."), os.system('cls')

mainMenu()
