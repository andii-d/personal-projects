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
import os

global counter
counter = 3


# Creates an instance of an account
class Accounts:
    # Holds all the accounts within a class dictionary
    allAccounts = {}

    def __init__(self, username, password):
        self.allAccounts[username] = self
        self.username = username
        self.password = password



def load_accounts_and_songs_and_scores():
    # Loading all accounts in
    with open('accounts.txt') as file:
        for line in file:
            # Strips the line of any new lines
            line = line.rstrip()
            # Splits the line by a : and assigns it into the corresponding variables
            username, password = re.split('[:]', line)
            # Initialising the Account object
            Accounts(username, password)


def register():
    print('\nWelcome to the registration page.')

    # Setting the user's new account with their sign in credentials
    while True:
            username = input('Please create a username: ')
            if username in Accounts.allAccounts.keys():
                print('The username is already taken. Please choose another username.\n')
            else:
                break

    password = input('Please create a password: ')

    encrypt_pw = password
    # Shifts the password by the length of itself
    shift = len(password)
    # Gets the string of ascii letters
    alphabet = string.ascii_letters
    # Shifts the ascii letters by the number given
    shifted = alphabet[shift:] + alphabet[:shift]

    table = str.maketrans(alphabet, shifted)

    encrypted = encrypt_pw.translate(table)

    # Saving the account to the 'accounts.txt' file
    with open('database.txt', 'a') as f:
        f.write(username + ':' + encrypted + '\n')

    # Creating a new Account object with the given details
    Accounts(username, password)
    print('\nYour account has been created!')

    # Redirecting the user back to the Music Quiz Menu
    menu()


def login():
    print('\nWelcome to the login page.')

    username = input('Please enter your username: ')
    if username in [acc.username for acc in Accounts.allAccounts.values()]:
        with open('database.txt', 'r') as f:
            f.read(username)

        password1 = username

        encrypt_pw = password1
        # Shifts the password by the length of itself
        shift = len(password) - len(password) - len(password)
        # Gets the string of ascii letters
        alphabet = string.ascii_letters
        # Shifts the ascii letters by the number given
        shifted = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet, shifted)
        decrypted = encrypt_pw.translate(table)
        print('Account accessed. Your password is:', decrypted)


def menu():
    print('\nWelcome to your personal password reminder!\n'
          '\n1. Enter your username and password'
          '\n2. Recover your account'
          '\n3. Quit\n')

    while True:
        try:
            menu1 = int(input('Please enter an option: '))

        except ValueError:
            print('Please enter an integer.')
            continue

        else:
            if menu1 == 1:
                register()

            elif menu1 == 2:
                login()

            elif menu1 == 3:
                print('Quitting.', end=''), time.sleep(0.5)
                print('.', end=''), time.sleep(0.5)
                print('.'), time.sleep(0.5)
                quit()


menu()
