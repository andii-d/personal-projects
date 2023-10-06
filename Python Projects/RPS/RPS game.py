import random
import time
# How many times the game will run before prompting the user to run the game again
global counter
counter = 5

def game():
    while True:
        global counter
        rps = ['rock', 'paper', 'scissors']
        
        player = ('Please enter an option here').casefold()
        computer = random.choice(rps)
        
        if counter < 1:
            play = input('Would you like to play again? (Y/N)').casefold()
            if play == 'y'.casefold():
                while counter < 5:
                    counter += 1
                if counter == 5:
                    break
                game()
            
            elif play == 'n'.casefold():
                print('Goodbye!'), time.sleep(0.75)
                quit()

            else:
                print('Please pick a correct option.')
             
            
        if player == 'rock':
            if computer == 'paper':
                print('\nYou lost! Paper wraps up rock.\n'), time.sleep(0.75)
                counter -= 1
            else:
                print('\nYou won! Rock crushes scissors.\n'), time.sleep(0.75)
                counter -= 1
                game()
                
        
        elif player == 'paper':
            if computer == 'scissors':
                print('\nYou lost! Scissors cuts up paper.\n'), time.sleep(0.75)
                counter -= 1
            else:
                print('\nYou won! Paper wraps up rock.\n'), time.sleep(0.75)
                counter -= 1
                game()
        
        elif player == 'scissors':
            if computer == 'rock':
                print('\nYou lost! Rock crushes scissors.\n'), time.sleep(0.75)
                counter -= 1
            else:
                print('\nYou won! Scissors cut up paper.\n'), time.sleep(0.75)
                counter -= 1
                game()

player = ('Please enter an option here')

print('test'), time.sleep(0.5)         
game()
