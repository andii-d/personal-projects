"""
Task 5 : Password Reminder

Skills Required:
Using variables, operators, inputs, outputs and assignments
Using sequences, selection and iteration
Using count controlled loops (for) and condition controlled loops (while)
Using different types of data, i.e. integer, string, float and Boolean
Basic string manipulation
Basic file handling operations
Using lists
Using subroutines

People often struggle to remember their passwords for different accounts. One potential solution is to store the
passwords on your computer securely, using an encryption algorithm.

A relatively straightforward encryption algorithm is the Caesar Cipher. This cipher works by shifting each letter by
a number of characters. E.g. if the shift is 3 then a becomes d, b becomes e, etc.

The finished program should allow a user to enter an account, username and password. The password should be encrypted
using a Caesar Cipher that uses the length of the password as the key (i.e. if a password is 5 letters long,
the key will be 5). The account, username and encrypted password should then be saved to a file or files.

The program should also allow the user to recover their password by entering the account and username. The program
should then decrypt and display the password to the user.

Analyse the requirements for this system and design, develop, test and evaluate a program to help users store their
passwords securely.

Extension

At the moment it would be easy for someone else to gain access to the password by examining the text file and
entering the account and username to get the password. To make the program more secure, encrypt the account and
username as well.

Further Extension 

Implement a self-destruct sequence. If someone enters a password incorrectly 3 times in a row then the data file
should be deleted. Closing the program and re-running it should not reset the number of incorrect attempts.

"""

import re
import string
import time

# Creates an instance of an account
class Account:
    # Holds all the accounts within a class dictionary
    allAccounts = {}

    def __init__(self, username, password):
        self.allAccounts[username] = self
        self.username = username
        self.password = password
        

def accounts():
    # Loading all accounts in
    with open('a.txt', 'r') as file:
        for line in file:
            # Strips the line of any new lines
            line = line.rstrip()
            # Splits the line by a : and assigns it into the corresponding variables
            username, password = re.split('[:]', line)
            # Initialising the Account object
            Account(username, password)
            
def register():
    print('\nWelcome to the registration page.')

    # Setting the user's new account with their sign in credentials
    while True:
        username = input('Please create a username: ')
        if username in Account.allAccounts.keys():
            print('The username is already taken. Please choose another username.\n')
        else:
            break

    password = input('Please create a password: ')

    # Saving the account to the 'accounts.txt' file
    with open('database.txt', 'a') as f:
        f.write(username + ':' + password + '\n')

    # Creating a new Account object with the given details
    Account(username, password)
    print('Your account has been created!\n')

    # Redirecting the user back to the Music Quiz Menu
    menu()            
            
def login():
    print('\nWelcome to the login page.')

    # Ask the user to enter their credentials
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')

    try:
        # Checks the value (password) to see if it would match the key (username), and if so then it grants access
        authenticatedUser = (Account.allAccounts[username].password == password)
    except KeyError:
        # In the case the username doesn't exist, then deny access
        authenticatedUser = False
    finally:
        if authenticatedUser:
            print('\nWelcome ', username, '!')
            quit()

        else:
            print('The account credentials are incorrect. You will be returned to the menu.\n')
            menu()          
            
def menu():
    print('\nWelcome to your personal password reminder!'
          '\n1. Register an account'
          '2. Login'
          '3. Quit')
    
    while True:
        try:
            mainmenu = int(input('Please enter an option: '))
    
        except ValueError:
            print('Please enter an integer.')
            continue
        
        else:
            if mainmenu == 1:
                register()
            
            elif mainmenu == 2:
                login()
            
            elif mainmenu == 3:
                print('Quitting.'), time.sleep(0.5)
                print('.'), time.sleep(0.5)
                print('.'), time.sleep(0.5)
                quit()
            
                
accounts()
menu()