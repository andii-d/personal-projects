# Importing necessary libaries and making necessary variables global
import random
import time
global lives
lives = 2

# Welcomes the player 
def code_start():
    print("Welcome To Rock Paper Scissors!")
    menu()

# Main menu of which the player can select whatever they wish to
def menu():
    menu_select = input("a) Start Game\nb) Quit\n")
    if menu_select == 'a':
        print("Rules:\nThere's 8 rounds, for each round you must enter rock, paper or scissors.\nGame will begin in 5 seconds.")
        time.sleep(5)
        game()
    elif menu_select == 'b':
        quit()
    else:
        print("Invalid option, please select 'a' or 'b'")
        menu()

def game():
    for i in range (8):
        global lives
        
        # Array of the 3 choices, and a function to randomise the choices
        choices = ['rock','paper','scissors']
        random_choice = random.choice(choices)
        user_choice = input("Enter your choice:\n")
        
        # Conditions on rock
        if user_choice == random_choice:
            print("DRAW! Bot picked", random_choice)
        
        elif user_choice == 'rock' and random_choice == 'scissors':
            print("YOU WIN! Bot picked", random_choice)
        
        elif user_choice == 'rock' and random_choice == 'paper':
            print("YOU LOST! Bot picked", random_choice)
            lives -= 1
            if lives == 0:
                game_loss()
        
        # Conditions on scissors
        elif user_choice == 'scissors' and random_choice == 'rock':
            print("YOU LOST! Bot picked", random_choice)
            lives -=  1
            if lives == 0:
                game_loss()
        
        elif user_choice == 'scissors' and random_choice == 'paper':
            print("YOU WIN! Bot picked", random_choice)
        
       # Conditions on paper
        elif user_choice == 'paper' and random_choice == 'scissors':
            print("YOU LOST! Bot picked", random_choice)
            lives -= 1
            if lives == 0:
                game_loss()
        
        elif user_choice == 'paper' and random_choice == 'rock':
            print("YOU WIN! Bot picked", random_choice)
        
        
        else:
            print("Invalid option, please select rock, paper or scissors")
        time.sleep(2)
    
    game_end()

# Ends the program within 5 seconds once the player's 2 lives are gone
def game_loss():
    print("You ran out of lives :(\nGame will end in 5 seconds")
    time.sleep(5)
    quit()

# Ends the program once the player has survived the game
def game_end():
    print("GZ! You got through all 5 rounds!")
    time.sleep(2)
    quit()


code_start()